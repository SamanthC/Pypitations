import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg

tab_doc = pd.read_csv('data/tab_article.csv', sep = ';')


def biblio():
    st.header("Etat de l'art et bibliographie")
    st.write(
    """
    \n
    """
    )
    st.markdown("Ces sujets font et feront encore l’objet de progrès.")
    st.write(
    """
    \n
    """
    )
    st.markdown("Les différentes approches peuvent être comparées sous l’angle des métriques rapportées dans la littérature scientifique.")
    fig = plt.figure(figsize=(15,12), dpi=600)
    ax = fig.add_subplot(111)
    x = tab_doc.Year
    y1 = tab_doc.Accuracy
    y2 = tab_doc.Sensitivity
    y3 = tab_doc.Specificity
    ax.scatter(x, y1,color='r', s = 200, marker='^', label='Accuracy', facecolor = 'none')
    ax.scatter(x, y2,color='g', s = 200, marker='*', label='Sensitivity', facecolor = 'none')
    ax.scatter(x, y3,color='b',s = 200, marker='p', label='Specificity', facecolor = 'none')
    ax.set_xlim([2005,2023])
    ax.set_ylim([65,101])
    ax.set_xlabel('Années')
    ax.legend(loc='best')
    fig.tight_layout()
    fig = plt.gcf()
    st.pyplot(fig)
    st.markdown("<h4 style='text-align: center;'>Figure : Performances des algorithmes de classification d'ECGs.</h4>", unsafe_allow_html=True)
    st.write(
    """
    \n
    """
    )

    st.markdown("Le challenge du temps réel est un compromis entre précision du résultat et la rapidité de son obtention.")
    st.dataframe(tab_doc)
    st.markdown("<h4 style='text-align: center;'>Table : Tableau récapitulatif des avancées sur le sujet.</h4>", unsafe_allow_html=True)
    st.write(
    """
    \n
    """
    )
    st.markdown("Merci pour votre attention !")