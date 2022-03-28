import streamlit as st
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
import time


# Import du modèle
model = keras.models.load_model("models/CNN_1.h5")

# Import des données du dataset MIT test

mit_test = pd.read_csv("data/mitbih_test.csv", header=None)

X_test = mit_test.iloc[:,:-1]
y_test = mit_test.iloc[:,-1]

# Mapping entre les numéros de classes et les libellés
dictionnaire = {
    0 : "Normal",
    1 : "Tachycardie supraventriculaire",
    2 : "Extrasystole ventriculaire",
    3 : "Fusion",
    4 : "Non identifié"
}

def demonstration():

    # Titre et sous-titre
    st.header("Démonstration")
    st.write("Nous allons tester notre réseau de neurones de convolution avec des exemples du dataset MIT test : ")
    st.subheader("Sélection de l'ECG")

    # Saisie de l'ECG qui sera tracé et classifié
    index = st.text_input("Veuillez rentrer un nombre entre 0 et 21892 :")
    
    if index:

        # Illustration de l'ECG saisi
        fig = plt.figure(figsize = (10,5))
        plt.plot(X_test.iloc[int(index),:])
        st.pyplot(fig)

        # Variables de la classe prédite et la classe réelle
        pred = int(model.predict(X_test.iloc[int(index):int(index)+1,:]).argmax(1))
        pred_proba = int(model.predict(X_test.iloc[int(index):int(index)+1,:]).max()*100)
        reel = int(y_test.iloc[int(index)])        
        
        st.subheader("Prédiction du modèle")

        # Bouton pour lancer la prédiction (session state pour ne pas enlever l'output du 1er bouton quand le 2e est cliqué)
        button1 = st.button("Prédire la classe de l'éléctrocardiogramme")

        if st.session_state.get('button') != True:
            st.session_state['button'] = button1
        if st.session_state['button'] == True:
            # Output du premier bouton
            st.markdown("La classe prédite par le modèle est **{} : {}**.".format(pred, dictionnaire[pred]))
            st.markdown("Probabilité de la classe prédite :")

            # Message conditionnel en fonction de la proba de la classe prédite
            if pred_proba > 90 :
                st.success("La probabilité de la classe prédite est de **{}%**!".format(pred_proba))
            else:
                st.warning("Attention! La probabilité de la classe prédite est de **{}%**. Le diagnostic \
                    doit être validé par un expert".format(pred_proba))

            if st.button('Découvrir la classe réelle'):
                # Output du 2e bouton
                st.markdown("La classe réelle de l'ECG est **{} : {}**".format(reel, dictionnaire[reel]))
                # Message conditionnel en fonction de si la classe prédite est la bonne ou pas
                if pred == reel :
                    st.success("Le modèle a prédit la bonne classe!")
                else:
                    st.error("Le modèle n'a pas prédit la bonne classe!")

                st.session_state['button'] = False