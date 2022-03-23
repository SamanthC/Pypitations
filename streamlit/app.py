import streamlit as st
from contexte import contexte
from modelisation import modelisation
from exploration import exploration
from demonstration import demonstration
from conclusion import conclusion

def main():
    
    menu_list = ["Le projet PyPitations", "Exploration des données", "Modelisation", "Démonstration", "Conclusion et Ouverture"]

    menu = st.sidebar.radio("Sommaire", menu_list)
    if menu == menu_list[0]:
        contexte()
    elif menu == menu_list[1]:
        exploration()
    elif menu == menu_list[2]:
        modelisation()
    elif menu == menu_list[3]:
        demonstration()
    else:
        conclusion()

if __name__ == "__main__":
    main()