import streamlit as st
import pandas as pd
import numpy as np

# Définition des matrices de confusion et les rapports de classifications pour les 2 datasets

conf_matrix_mit = pd.DataFrame(
    np.array(
        [
            [17677, 218, 127, 78, 18],
            [69, 444, 10, 5, 1],
            [47, 5, 1362, 25, 9],
            [9, 3, 13, 137, 0],
            [43, 4, 17, 0, 1544]
        ]
    )
)

conf_matrix_mit.columns = ["predict_0", "predict_1", "predict_2", "predict_3", "predict_4"]

conf_matrix_ptb = pd.DataFrame(
    np.array(
        [
            [790, 51],
            [107, 1963]
        ]
    )
)

conf_matrix_ptb.columns = ["predict_0", "predict_1"]

report_mit = pd.DataFrame(
    [
        ["0.99", "0.98", "0.98"],
        ["0.66", "0.80", "0.72"],
        ["0.89", "0.94", "0.92"],
        ["0.56", "0.85", "0.67"],
        ["0.98", "0.96", "0.97"]
    ]
)

report_mit.columns = ["précision", "rappel", "f1-score"]

report_ptb = pd.DataFrame(
    [
        ["0.88", "0.94", "0.91"],
        ["0.97", "0.95", "0.96"],
    ]
)

report_ptb.columns = ["précision", "rappel", "f1-score"]


def modelisation():
    # Titre de la page
    st.header("Modélisation")

    # Sous-Titre 1
    st.subheader("La démarche globale")
    
    st.write(
        """
        Dans un premier temps nous avons testé deux algorithmes de Machine Learning \
        classiques avec le dataset MIT : la régression logistique et le Support Vector \
        Machine. Au vu du déséquilibre des classes, nous avons tester ces algorithmes \
        après entrainement sur le dataset train tel quel, puis sur le data set train \
        ré-équilibré via undersampling
        
        Malgré des résultats encourageant avec des algorithmes de Machine Learning simples,\
        nous avons décidé de tester des algorithmes de Deep Learning:
        
        - nous avons d'abord testé un simple modèle de réseaux de neurones à 4 couches :
        """
    )

    # Centrage de l'image
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write(' ')

    with col2:
        st.image("streamlit/images/image26.png", width = 300, caption = "Réseau de neurones artificiel")

    st.write(
        """
        - dans un deuxième temps, nous avons testé un réseau de neurones de convolution assez simple :  
        """
    )

    # Centrage de l'image
    col5, col6, col7, col8, col9, col10= st.columns(6)
    with col5:
        st.write(' ')

    with col6:
        st.image("streamlit/images/image8.png", width = 500, caption = "Réseau de neurones de convolution")

    st.write(
        """
        - nous avons enfin testé la technique du Transfer Learning avec un réseau DenseNet121. Pour cela, \
        nous avons procédé à un pre-processing du signal afin de le transformer en image qui pourra être \
        intégré dans le réseau DensNet121, lui même déjà entrainé sur des images en 2D. Le preprocessing est \
        une transformée en ondelettes continues, similaire à une transformée de Fourier mais qui \
        prend en compte le fait que la férquence du signal évolue dans le temps :
        """
    )

    st.image("streamlit/images/image_cwt.png", width = 1000, caption = "Transformation d'un signal en image via CWT")

    # Sous-Titre 2
    st.subheader("Le modèle choisi")

    st.write(
        """
        De tous les modèles testés, nous avons décidé de garder le CNN, qui propose les meilleurs résultats, aussi bien \
        sur le dataset MIT que sur le dataset PTB :
        """
    )

    # KPI du dataset MIT
    st.write("- Matrice de confusion et rapport des métriques du dataset MIT test")
    st.table(conf_matrix_mit)
    st.table(report_mit)

    # KPI du dataset PTB
    st.write("- Matrice de confusion et rapport des métriques du dataset PTB")
    st.table(conf_matrix_ptb)
    st.table(report_ptb)
    
    st.write(
        """
        **C'est ce modèle qui sera utilisé dans la démonstration à suivre.**
        """
    )