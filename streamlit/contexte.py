import streamlit as st

def contexte():
    # Titre du projet
    st.title("Projet PyPitations")
    # Sous-Titre
    st.text("Présenté par Christophe Batty, David Farizon et Samanth Chinta")
    
    st.header("Le projet")
    st.markdown("Les signaux cardiaques décrits au sein des électrocardiogrammes (ECG) décrivent les battements de coeur.")
    st.markdown("Le but de ce projet est de classifier des signaux cardiaques de patients normaux et de patients atteints d’arythmie ou d’infarctus du\
    myocarde à l'aide de la Data Science, des techniques et méthodes apprises lors de notre formation de Data Scientist :")
    st.markdown("Le projet s'est donc articulé comme suit :")
    st.markdown("- *la compréhension du sujet, la découverte de la problématique*")
    st.markdown("- *l'exploration, la visualisation des données disponibles (données MIT-BIH et PTB)*")
    st.markdown("- *la définition d'une stratégie*")  
    st.markdown("- *l'utilisation de différents modèles d'apprentissage (machine learning, deep learning, transfer learning)*")  
    st.markdown("- *l'analyse des résultats des classifications*") 
    st.markdown("- *la synthèse des travaux (code, rapport, présentation) et les perspectives du projet*") 
        
    # Présentation du coeur
    st.header("Introduction du sujet")
    st.subheader("Qu'est ce que le coeur?")
    st.image("streamlit/images/image33.jpg", caption = "Fonctionnement du coeur")
    st.markdown("Le coeur, **organe vital**, assure la circulation du sang :")
    st.markdown("Chaque jour, il effectue quelques 100 000 battements.")
    st.markdown("Véritable moteur, il est constitué de 2 coeurs :")
    st.markdown("- *le coeur droit récupère le sang venant de l'organisme, appauvri en oxygène, pour l'envoyer vers les poumons*")
    st.markdown("- *le coeur gauche récupère le sang, oxygéné et nettoyé du gaz carbonique, pour l'envoyer dans tout l'organisme*")
    st.markdown("- *d'un système de chambres (oreillette --> ventricule), de valves organisant ces circulations*")  
    st.markdown("- *d'un **pilotage 'électrique'** orchestrant le fonctionnement des muscles cardiaques*")   
    
    # Explication ECG
    st.subheader("Qu'est ce qu'un électrocardiogramme (ECG)")
    st.image("streamlit/images/image34.png", caption = "Exemples d'ECGs")
    st.image("streamlit/images/image_ecg.png", caption = "Décomposition d'un ECG")
    st.markdown("L'ECG enregistre une succession de séquences de l'activité électrique du coeur, représentées par des ondes nommées P, QRS et T où :")
    st.markdown("- *l’onde P est celle des oreillettes au moment de leur contraction,*")
    st.markdown("- *l’ensemble QRS correspond à la contraction des ventricules,*")
    st.markdown("- *l’onde T reflète la repolarisation (retour à la phase de repos) des ventricules.*")  
    
    # Diagnostics actuel des ECG
    st.subheader("Diagnostics actuels")
    st.markdown("Aujourd'hui, l'analyse des ECG repose sur des interprétations visuelles faite par des spécialistes (cardiologues, médecins).")
    st.markdown("En effet, cette interprétation permet de comprendre et de protéger des maladies cardio-vasculaires.")
    st.markdown("Pour un cardiologue, si un faux positif (patient classifié comme étant atteint de maladie cardiaque alors qu’il est sain)\
    n’a généralement que peu de conséquences pour un patient, l’inverse, soit un vrai négatif peut être lourde en conséquence.")
    
     # Traitement actuel des données
    st.subheader("Des bases de données conséquentes et accessibles")
    st.markdown("Les hôpitaux ont constitué depuis de nombresues années des bases de données ECG importantes où chaque ECG a été annoté par plusieurs spécialistes.")
    st.markdown("Les bases de données du MIT-BIH Arrhythmia et du PTB sont **une source d'apprentissage rêvée pour des Datas Scientists**.")
    st.markdown("Ces bases de données ont déjà fait l'objet d'études de classification à l'aide de la Data Science.")
    
    st.markdown("### Le projet Pypitation (Py'thon'-'Pal'pitations) est une étude de classification.")
    
    # Pour découvrir
    st.subheader("Quelques vidéos intéressantes sur le sujet")
    st.markdown("Une présentation des différents types d'ECG (normaux/anormaux)")
    st.video(data="https://www.youtube.com/watch?v=cSugcAq61S0")
    st.markdown("Une vidéo vulgarisant le fonctionnement du coeur")
    st.video(data="https://www.youtube.com/watch?v=s7SuTXiGupQ")

