import streamlit as st

def modelisation():
    st.header("Modélisation")

    st.subheader("La démarche globale")
    
    st.write(
        """
        - Dans un premier temps nous avons testé deux algorithmes de Machine Learning \
            classiques avec le dataset MIT : la régression linéaire et le Support Vector \
            Machine. Au vu du déséquilibre des classes, nous avons tester ces algorithmes \
            après entrainement sur le dataset train tel quel, puis sur le data set train \
            ré-équilibré via undersampling
        - Malgré des résultats encourageant avec des algorithmes de Machine Learning simples,\
            nous avons décidé de tester des algorithmes de Deep Learning:
            - nous avons d'abord testé un simple modèle de réseaux de neurones à 4 couches :
        """
    )
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write(' ')

    with col2:
        st.image("streamlit/images/image26.png", width = 300)

    st.subheader("Le modèle choisi")

    