import streamlit as st

def modelisation():
    st.header("Modélisation")

    st.subheader("La démarche globale")
    
    st.write(
        """
        Dans un premier temps nous avons testé deux algorithmes de Machine Learning \
        classiques avec le dataset MIT : la régression linéaire et le Support Vector \
        Machine. Au vu du déséquilibre des classes, nous avons tester ces algorithmes \
        après entrainement sur le dataset train tel quel, puis sur le data set train \
        ré-équilibré via undersampling
        
        Malgré des résultats encourageant avec des algorithmes de Machine Learning simples,\
        nous avons décidé de tester des algorithmes de Deep Learning:
        
        - nous avons d'abord testé un simple modèle de réseaux de neurones à 4 couches :
        """
    )
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write(' ')

    with col2:
        st.image("streamlit/images/image26.png", width = 300)

    st.write(
        """
        - dans un deuxième temps, nous avons testé un réseau de neurones convolutionel assez simple :  
        """
    )

    col5, col6, col7, col8, col9, col10= st.columns(6)
    with col5:
        st.write(' ')

    with col6:
        st.image("streamlit/images/image8.png", width = 500)

    st.write(
        """
        - nous avons enfin testé la technique du Transfer Learning avec un réseau DenseNet121. Pour cela, \
        nous avons procédé à un pre-processing du signal afin de le transformer en image qui pourra être \
        intégré dans le réseau DensNet121, lui même déjà entrainé sur des images en 2D. Le preprocessing est \
        une transformée en ondelettes continues, similaire à une transformée de Fourier mais qui \
        prend en compte le fait que la férquence du signal évolue dans le temps :
        """
    )

    st.image("streamlit/images/image_cwt.png", width = 1000)

    st.subheader("Le modèle choisi")

    st.write(
        """
        De tous les modèles testés, nous avons décidé de garder le CNN, qui propose les meilleurs résultats, aussi bien \
        sur le dataset MIT que sur le dataset PTB :
        """
    )

    col11, col12 = st.columns(2)

    with col11:
        st.image("streamlit/images/image10.png")

    with col12:
        st.image("streamlit/images/image4.png", width = 150)
    
    st.write(
        """
        C'est ce modèle qui sera utilisé dans la démonstration à suivre.
        """
    )