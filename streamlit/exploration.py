# import des librairies et des datasets

import streamlit as st



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
    
    st.image("streamlit/images/image38.png", width = 1000, caption = "Répartition des classes dans le data set MITBIH")

    st.markdown("Nous observons un déséquilibre de classes que nous devrons traiter par rééchantillonage au moment de l'entraînement des modèles.")
    
    # Exemple de signal anoté
    st.markdown("Observons maintenant un ECG de classe normale et décomposons sa forme.")
    st.image("streamlit/images/image37.png", width = 1000,  caption = "Exemple d'ECG de classe 'Normal")


    # Distance RR
    st.markdown("Une caractéristique importante des ECGs : la distance RR (distance entre deux pics).")
    st.image("streamlit/images/dist_RR.png", width = 1000, caption = "Distance RR")
    
    
    # Exemples de signaux de différentes classes
    st.markdown("Observons maintenant quelques exemples de signaux liés à différentes classes du dataset MITBIH.")
    st.image("streamlit/images/image41.png", width = 1000, caption = "Figure : exemples de signaux choisis aléatoirement de différentes classes du dataset MITBIH")

    
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
    st.markdown("Observons d’abord la répartition des classes du dataset PTB associé aux différentes valeurs de la cible:") 
    st.image("streamlit/images/image45.png", width = 1000, caption = "Figure : Répartition des classes dans le data set PTB")
        
     

    # Exemple de signaux du dataset PTBDB
    st.markdown("Quelques signaux du dataset PTBDB:")
    st.image("streamlit/images/image100.png", width = 1000, caption = "Quelques signaux du dataset PTBDB")

    

    st.markdown("De nos premières observations, il ressort que la distance RR ne donne pas d’information sur la classification des battements.")
    st.markdown("Problématique : Comment considérer la classification des battements cardiaques comme un problème d'apprentissage\
    où nous pouvons extraire des attributs à partir du jeu de données, puis entraîner des algorithmes de classification ?")
