import streamlit as st

def contexte():
    # Titre du projet
    st.title("Projet PyPitation")

    # Sous-Titre
    st.text("Présenté par Christophe Batty, David Farizon et Samanth Chinta")

    # Introduction
    st.header("Qu'est ce que le coeur?")
    st.image("streamlit/images/image33.jpg", caption = "Fonctionnement du coeur")
    st.text("blablabla")

    # Explication ECG
    st.header("Qu'est ce qu'un électrocardiogramme (ECG)")
    st.image("streamlit/images/image34.png", caption = "Exemples d'ECGs")

    st.image("streamlit/images/image_ecg.png", caption = "Décomposition d'un ECG")


