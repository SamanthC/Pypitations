# import des librairies et des datasets

import streamlit as st

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg

import seaborn as sns

import os


# import et fusion des datasets
ptbdb_normal = pd.read_csv("data/ptbdb_normal.csv", header=None)
ptbdb_abnormal = pd.read_csv("data/ptbdb_abnormal.csv", header=None)
ptbdb = pd.concat([ptbdb_normal, ptbdb_abnormal])
mitbih_train = pd.read_csv("data/mitbih_test.csv", header = None)
mitbih_test = pd.read_csv("data/mitbih_test.csv", header = None)
mitbih = pd.concat([mitbih_test, mitbih_train])

# sous jeux de données en fonction des cibles de mitbih
mitbih_0 = mitbih[mitbih.iloc[:,-1]==0]
mitbih_1 = mitbih[mitbih.iloc[:,-1]==1]
mitbih_2 = mitbih[mitbih.iloc[:,-1]==2]
mitbih_3 = mitbih[mitbih.iloc[:,-1]==3]
mitbih_4 = mitbih[mitbih.iloc[:,-1]==4]


# generateurs d'indices de lignes aléatoires suivant les différentes cibles

indices_mit = [
    [np.random.randint(0, len(mitbih_0)), np.random.randint(0, len(mitbih_0)), np.random.randint(0, len(mitbih_0))],
    [np.random.randint(0, len(mitbih_1)), np.random.randint(0, len(mitbih_1)), np.random.randint(0, len(mitbih_1))],
    [np.random.randint(0, len(mitbih_2)), np.random.randint(0, len(mitbih_2)), np.random.randint(0, len(mitbih_2))],
    [np.random.randint(0, len(mitbih_3)), np.random.randint(0, len(mitbih_3)), np.random.randint(0, len(mitbih_3))],
    [np.random.randint(0, len(mitbih_4)), np.random.randint(0, len(mitbih_4)), np.random.randint(0, len(mitbih_4))]
]

indices_ptb = [
    [np.random.randint(0, len(ptbdb_normal)), np.random.randint(0, len(ptbdb_normal))],
    [np.random.randint(0, len(ptbdb_abnormal)), np.random.randint(0, len(ptbdb_abnormal))],
]


def exploration():

    # Les données dons nous disposons
    st.header("Quelles données avons-nous à disposition?")    
    st.markdown("Deux bases de données contenant des ECGs, disponibles sur Kaggle ont été utilisées : la base MIT-BIH Arrhythmia et la base PTB Diagnostic ECG.")
    st.markdown("Les ECG figurant dans ces deux datasets ont été créés suivant le processus de rééchantillonnage à 125 Hz à partir d’un enregistrement initial à 360 Hz et ont été prétraités.")
    st.markdown(" - 1. Division du signal ECG continu en fenêtres de 10s et sélection d’une fenêtre de 10s à partir d'un signal ECG.")
    st.markdown(" - 2. Normalisation des valeurs d'amplitude (entre 0 et 1)")
    st.markdown(" - 3. Recherche de l'ensemble des maximums locaux caractérisés par les coordonnés de passages par zéro de la dérivée première du signal.")
    st.markdown(" - 4. Recherche de l'ensemble des pics R en appliquant un seuil de 0,9 sur la valeur normalisée des maximas.")
    st.markdown(" - 5. Recherche de la médiane des intervalles de temps R-R (T).")
    st.markdown("-  6. Sélection pour chaque crête R, d’une partie de signal avec la longueur égale à 1,2 T.")
    st.markdown(" - 7. Remplissage de chaque partie du dataset sélectionnée précédemment avec des zéros pour faire en sorte que la longueur du signal soit égale à une longueur fixe prédéfinie.")
    st.markdown("Toutes les observations ont été définies sur une plage de 187 colones de DataFrames.") 
 
    # La base de données MITBIH, généralités   
    st.subheader("La base données MITBIH :")         
    st.markdown("Fruit du travail depuis 1975 entre le laboratoire Beth Israel Medical Center, et le MIT pour la recherche et l'analyse de l'arythmie cardiaque.")
    st.markdown("Une bonne partie de ces données est requise par la norme ANSI pour tester les appareils ambulatoires d’enregistrements et de mesures des ECG.")
    st.markdown("Contient des signaux ECG annotés manuellement par des experts et classifiés en 5 catégories :")
    st.markdown(" - Classe 'N' (0) : *Normal, Left/Right bundle branch block, Atrial escape,  Nodal escape*")
    st.markdown(" - Classe 'S' (1) : *Atrial premature, Aberrant atrial premature, Nodal premature, Supra-ventricular premature*")
    st.markdown(" - Classe 'V' (2) : *Premature ventricular contraction, Ventricular escape*")
    st.markdown(" - Classe 'F' (3) : *Fusion of ventricular and normal*")
    st.markdown(" - Classe 'Q' (4) : *Paced, Fusion of paced and normal, Unclassifiable*")
       
    code = """
        # Les 5 classes du dataset mitbih :
        mit_class = {0 : "Normal",
                     1 : "Tachycardie supraventriculaire",
                     2 : "Extrasystole ventriculaire",
                     3 : "Fusion",
                     4 : "Non identifié"}
            """
    st.code(code, language='python')
         
    # Informations sur le dataset mitbih
    #mit_inf = mitbih.info()
    #st.write(mit_inf)
  
    st.write(
    """
    \n
    """
    )

    # Répartition des classes dans le data set MITBIH
    st.markdown("Observons d’abord la répartition des classes du dataset  MITBIH associé aux différentes valeurs de la cible")        
    liste = []
    for i in range(len(mitbih.iloc[:,-1].value_counts())):
        x = "Classe {} : {}%".format(round(mitbih.iloc[:,-1].value_counts(normalize = True).index[i]), 
                                     round(100*mitbih.iloc[:,-1].value_counts(normalize = True).iloc[i]))
        liste.append(x)
            
    fig = plt.figure(figsize = (16,9), dpi = 600)
    sns.set_theme()
    plt.title("Figure : Répartition des classes dans le data set MITBIH", fontsize = 15, y=0.05)
    plt.pie(mitbih.iloc[:,-1].value_counts(), labels = liste);
    fig.tight_layout()
    fig = plt.gcf()
    st.pyplot(fig)
    #st.markdown("<h1 style='text-align: center;'>*Figure 1 : Répartition des classes dans le data set MITBIH*</h1>", unsafe_allow_html=True)
    st.markdown("Nous observons un déséquilibre de classes que nous devrons traiter par rééchantillonage au moment de l'entraînement des modèles.")
    
    st.write(
    """
    \n
    """
    )
    
    indice=8
    fsa=25
    
    # Exemple de signal anoté
    st.markdown("Observons maintenant un ECG de classe normale et décomposons sa forme.")
    sns.set_theme()
    fig, ax = plt.subplots(1,1,figsize = (16,9))
    ax.plot(mitbih_train.iloc[indice][:-1].index, mitbih_train.iloc[indice][:-1])
    ax.plot([100, 120, 120, 100, 100],[0.015, 0.015, 1.025, 1.025, 0.015])
    ax.set_title("Exemple d'ECG de classe 'Normal'", fontsize = 20, y=-0.075, alpha = 0.8)
    ax.annotate("R peak", xy=(110, 1), xytext=(130, 1), arrowprops = {"facecolor": "red"}, fontsize = fsa)
    ax.annotate("T wave", xy=(40, 0.35), xytext=(25, 0.4), arrowprops = {"facecolor": "red"}, fontsize = fsa)
    ax.annotate("P wave", xy=(87, 0.3), xytext=(70, 0.4), arrowprops = {"facecolor": "red"}, fontsize = fsa)
    ax.annotate("QRS complex", xy=(120, 0.6), xytext=(140, 0.65), arrowprops = {"facecolor": "red"}, fontsize = fsa)
    fig.tight_layout()
    fig = plt.gcf()
    st.pyplot(fig)
    st.markdown("")
    st.write(
    """
    \n
    """
    )

    # Distance RR
    st.markdown("Une caractéristique importante des ECGs : la distance RR (distance entre deux pics).")
    #st.image("streamlit/images/dist_RR.png", caption = "Distance RR")
    fig, ax = plt.subplots(1,1,figsize=(16,9))
    ax.plot(mitbih_train.iloc[indice,:-1]);#
    ax.annotate("", xy = (0,1), xytext = (109, 1), arrowprops = dict(arrowstyle="<->", color = "red", linewidth = 4))
    ax.text(37.5, 0.95, "Distance RR", fontsize = fsa)
    ax.set_title("Figure : la distance RR",  y = -0.075, fontsize = fsa)
    fig.tight_layout()
    fig = plt.gcf()
    fig.set_dpi(600)
    st.pyplot(fig)
    #st.markdown("<h1 style='text-align: center;'>*Figure 2 : la Distance RR*</h1>", unsafe_allow_html=True)
    st.write(
    """
    \n
    """
    )
    
    # Exemples de signaux de différentes classes
    st.markdown("Observons maintenant quelques exemples de signaux liés à différentes classes du dataset MITBIH.")
    sns.set_theme()
    fig, axes = plt.subplots(3, 1, figsize = (16,27))
    fig.suptitle("Figure : exemples de signaux choisis aléatoirement de différentes classes du dataset MITBIH", fontsize = 25, y = -0.05)

    for i in range(0,3) : 
        axes[i].plot(mitbih_0.iloc[indices_mit[0][i],:-1], label = 'Normal' )
        axes[i].plot(mitbih_1.iloc[indices_mit[1][i],:-1], label = 'Tach. supraventr.', color = 'green')
        axes[i].plot(mitbih_2.iloc[indices_mit[2][i],:-1], label = 'Extrasystole ventr.', color = 'red')
        axes[i].plot(mitbih_3.iloc[indices_mit[3][i],:-1], label = 'Fusion', color = 'orange')
        axes[i].plot(mitbih_4.iloc[indices_mit[4][i],:-1], label = 'Non identifié', color = 'purple')
        axes[i].legend()

    fig.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(16, 9)
    fig.set_dpi(600.0)
    st.pyplot(fig)
    
    st.write(
    """
    \n
    """
    )

    # PTBDB               
    st.subheader("La base de données PTBDB :")
    st.markdown("Issue de l’institut national de métrologie allemand.")
    st.markdown("Contient les enregistrements de sujets catégorisés suivant 2 types :")
    st.markdown(" - Classe 'Normal' (0) : *sain*")
    st.markdown(" - Classe 'Abnormal' (1) : *infarctus du myocarde*")

    # informations sur le dataset ptbdb
    #ptb_inf = ptbdb.info()
    #st.write(ptb_inf)
    st.write(
    """
    \n
    """
    )    

    # Répartition des classes dans le data set PTBDB  
    st.markdown("Observons d’abord la répartition des classes du dataset PTB associé aux différentes valeurs de la cible")         
    liste_ptb = []
    for i in range(len(ptbdb.iloc[:,-1].value_counts())):
        x = "Classe {} : {}%".format(round(ptbdb.iloc[:,-1].value_counts(normalize = True).index[i]), round(100*ptbdb.iloc[:,-1].value_counts(normalize = True).iloc[i]))
        liste_ptb.append(x)

    plt.figure(figsize = (16,9), dpi =600)
    sns.set_theme()
    plt.title("Figure : Répartition des classes dans le data set PTB", fontsize = 15, y = 0.05)
    plt.pie(ptbdb.iloc[:,-1].value_counts(), labels = liste_ptb);
    fig.tight_layout()
    fig = plt.gcf()
    st.pyplot(fig)
    
    st.write(
    """
    \n
    """
    )       

    # Exemple de signaux du dataset PTBDB
    st.markdown("Quelques signaux du dataset PTBDB.")
    fig, axes = plt.subplots(2, 2, figsize = (16,6), dpi = 600)
    fig.suptitle(" Figure : Exemples d'ECGs, choisis aléatoirement, par classes - PTBDB", fontsize = 25, y = -0.01)
    
    for i in range(0,2):
        for j in range(0,2):
            axes[i,j].tick_params(axis = "both", labelbottom = False, labelleft = False, length = 0)
            axes[i,j].set_ylim(0,1)
            if i == 0:
                axes[i,j].plot(ptbdb_normal.iloc[indices_ptb[i][j],:-1])
                axes[i,0].set_ylabel("Classe 0")
                axes[i,j].set_title("{}".format(ptbdb_normal.iloc[indices_ptb[i][j]].name))

            if i == 1:
                axes[i,j].plot(ptbdb_abnormal.iloc[indices_ptb[i][j],:-1], color = "green")
                axes[i,0].set_ylabel("Classe 1")
                axes[i,j].set_title("{}".format(ptbdb_abnormal.iloc[indices_ptb[i][j]].name))
                
    fig.tight_layout()
    fig = plt.gcf()
    fig.set_dpi(600)
    st.pyplot(fig)

    st.write(
    """
    \n
    """
    )    

    st.markdown("De nos premières observations, il ressort que la distance RR ne donne pas d’information sur la classification des battements.")
    st.markdown("Problématique : Comment considérer la classification des battements cardiaques comme un problème d'apprentissage\
    où nous pouvons extraire des attributs à partir du jeu de données, puis entraîner des algorithmes de classification ?")