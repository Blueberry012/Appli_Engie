import streamlit as st

CURRENT_THEME = "blue"
IS_DARK_THEME = True

st.title('Application Engie')

st.image("image/engie.png", width=250, use_column_width=False, clamp=True)

st.header("Bienvenue")
st.write("Mon application Engie est une plateforme conçue pour restituer le test technique de candidature d'Engie ! ")


st.subheader("Contexte :")
st.write("On considère la consommation de deux points de consommation appartenant à un même site. Vous devrez effectuer une analyse de la consommation du site à travers 3 axes différents. Chaque analyse sera composée d'un graphique et d'un commentaire mettant en évidence une observation pertinente.")

st.subheader("Axes d'analyse :")
st.write("1) Comparaison de la consommation mensuelle de 2023 vs 2022")
st.write("2) Analyse de l'évolution des consommations de nuit sur le mois de janvier 2023. Une nuit est composée des consommations du jour J de 22h à 00h et des consommations du jour J+1 de 00h à 06h.")
st.write("3) Mise en évidence des différents profils de consommation hebdomadaire sur le mois de février 2023. Un profil de consommation reflète les habitudes de consommation d'un site.")

st.divider()

st.write("N'hésitez pas à explorer mon application pour consulter mon travail.")
