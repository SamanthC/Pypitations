import streamlit as st
from contexte import contexte
from modelisation import modelisation
from exploration import exploration
from demonstration import demonstration
from conclusion import conclusion
from biblio import biblio

def main():
    
    menu_list = ["Le projet PyPitations", 
                 "Exploration des données", 
                 "Modelisation", 
                 "Démonstration", 
                 "Conclusions et perspectives", 
                 "Etat de l'art et bibliographie"]

    menu = st.sidebar.radio("Sommaire", menu_list)
    if menu == menu_list[0]:
        contexte()
    elif menu == menu_list[1]:
        exploration()
    elif menu == menu_list[2]:
        modelisation()
    elif menu == menu_list[3]:
        demonstration()
    elif menu == menu_list[4]:
        conclusion()
    else:
        biblio()

if __name__ == "__main__":
    main()