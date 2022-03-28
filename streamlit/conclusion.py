import streamlit as st

def conclusion():
    st.header("Conclusions et perspectives")

    st.subheader("Le projet nous a permis d’aborder différentes aspects liés à la classification de signaux temporels :")
    st.markdown("- Analyse")
    st.markdown("- Traitement de signaux")
    st.markdown("- Modélisation")
    st.markdown("- Elaboration d’algorithmes d’apprentissage")
    st.write(
    """
    \n
    """
    )
    st.markdown("Nous avons réussi à obtenir des résultats préliminaires encourageants, notamment avec le réseau de neurones convolutionnel.") 
    st.write(
    """
    \n
    """
    )   
    st.subheader("Pistes d’optimisations des modèles testés :")
    st.markdown("- Modification des hyperparamètres des modèles déjà testés")
    st.markdown("- Ajout des couches intermédiaires de convolution et de pooling dans les modèles CNN")
    st.markdown("- Changement de filtres pour le preprocessing CWT")
    st.markdown("Test d’autres modèles pré-entraînés pour le transfer learning")
    st.markdown("Test d’approche hybride de feature extraction")
    st.write(
    """
    \n
    """
    )
    st.subheader("Ce projet a permis de mettre en œuvre :")
    st.markdown("- La découverte du fonctionnement du cœur et une problématique d’identification de pathologie cardiaque à partir d’ECGs")
    st.markdown("- Les outils et méthodes étudiées lors de la formation, notamment les réseaux de neurones convolutionnels pour image\
         et le transfer learning")
    st.write(
    """
    \n
    """
    )

    st.write(
    """
    \n
    """
    )
    st.subheader("Il est possible d'imaginer des mesures et une aide au diagnostic en temps réel via des capteurs connectés.")
    st.markdown("- Récupération des ECG (signaux électriques)")
    st.markdown("- Identification d’éventuelle présence d’anomalie cardiaque")
    st.write(
    """
    \n
    """
    )
    
    st.write(
    """
    \n
    """
    )

    st.subheader("En conclusion :")
    st.markdown("Le sujet est en plein essor.")
    st.markdown("Il peut être associé à d’autres données associées à des mesures de paramètres de santé ou d’autres caractéristiques temporelles des organismes vivants :")
    st.markdown("- Analyses sanguines")
    st.markdown("- Prises alimentaires")
    st.markdown("- Activités physiques et sportives")
    st.markdown("Plus généralement, toute donnée mesurable associée à différents types de mouvements conscients ou inconscients (réflexes) du corps humain.")
    st.markdown("Cependant, attention, un algorithme de classification d'ECGs n'a pas vocation à remplacer un expert médical mais peut être d'une grande aide.")
    st.write(
    """
    \n
    """
    )
    st.markdown("Merci pour votre attention !")