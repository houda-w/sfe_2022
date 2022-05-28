import streamlit as st
import mysql.connector
import impr
import os
import analytics
from PIL import Image


#@st.cache(suppress_st_warning=True)
def del_files():
    fold = 'OUTPUT'
    for f in os.listdir(fold):
       os.remove(os.path.join(fold,f))

def change_choice():
    menu = ['Acceuil','Analytiques','Procès verbaux']
    choice = st.sidebar.selectbox("Menu",menu,key='opt')
    if choice == "Acceuil":
        st.subheader("Bienvenue dans la page d'acceuil!")
        st.write("Veuillez toujours clicker sur le boutton TERMINER avant de générer des nouveaux PVs !")
        supr = st.button(label = 'Terminer',key="spr", on_click = del_files)
    elif choice == "Analytiques":
        st.subheader("Bienvenue dans la page de l'analyse des données")
        analytics.imprt_data()
    elif choice == "Procès verbaux":
        st.subheader("Ici vous pouvez télecharger les PV des eleveurs")
        impr.upl_data()
        #insertBLOB("Eric", fic)
        #st.button("revenir à la page d'acceuil")
        
