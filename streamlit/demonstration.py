import streamlit as st
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt

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
    st.header("Démonstration")
    st.write("Nous allons tester notre réseau de neurones convolutionnel avec des exemples du dataset MIT test : ")
    st.subheader("Sélection de l'ECG")

    # Saisie de l'ECG qui sera tracé et classifié
    index = st.text_input("Veuillez rentrer un nombre entre 0 et 21892 :")
    
    if index:

        # Illustration de l'ECG saisi
        fig = plt.figure(figsize = (10,5))
        plt.plot(X_test.iloc[int(index),:])
        st.pyplot(fig)
        
        st.subheader("Prédiction du modèle")
        
        # Boutton pour déclancher la classification
        button = st.button("Prédire la classe de l'éléctrocardiogramme")

        # Variables de la classe prédite et la classe réelle
        pred = int(model.predict(X_test.iloc[int(index):int(index)+1,:]).argmax(1))
        reel = int(y_test.iloc[int(index)])

        # Affichage du résultat une fois le boutton appuyé
        if button:
            st.markdown("La classe prédite par le modèle est **{} : {}**".format(pred, dictionnaire[pred]))
            st.markdown("La classe réelle de l'ECG est **{} : {}**".format(reel, dictionnaire[reel]))

            if pred == reel :
                st.success("Le modèle a prédit la bonne classe!")
            else:
                st.error("Le modèle n'a pas prédit la bonne classe!")



