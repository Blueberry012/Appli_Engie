import pandas as pd
import  matplotlib.pyplot as plt
import streamlit as st

df1 = pd.read_csv('data/pdl_1.csv')
df2 = pd.read_csv('data/pdl_2.csv')

st.title("Bases de données")

# Ajouter une image avec redimensionnement et placement spécifique
image = 'image/engie.png'

# Affichage de l'image avec une taille personnalisée et placement dans le coin supérieur droit
st.image(image, width=250, use_column_width=False, clamp=True)

def afficher_site1():
    st.header("Données du Site 1")
    st.write(df1)

def afficher_site2():
    st.header("Données du Site 2")
    st.write(df2)

afficher_site1()
afficher_site2()
