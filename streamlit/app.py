import streamlit as st
from contexte import contexte
from modelisation import modelisation
from exploration import exploration
from demonstration import demonstration

def main():
    
    menu_list = ["Le projet PyPitation", "Exploration des données", "Modelisation", "Démonstration"]

    menu = st.sidebar.radio("Sommaire", menu_list)
    if menu == menu_list[0]:
        contexte()
    elif menu == menu_list[1]:
        exploration()
    elif menu == menu_list[2]:
        modelisation()
    else:
        demonstration()

if __name__ == "__main__":
    main()