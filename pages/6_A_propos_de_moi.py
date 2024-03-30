import streamlit as st

st.title("Thom CHHUN")

st.write("📞 06 29 56 57 82")
st.write("✉️ thom.chhun@gmail.com")
st.write("📍 Courbevoie (92400)")
st.write("📅 20 ans")
st.link_button("Accéder à mon Porfolio", "https://thom-chhun-portfolio.netlify.app/")
st.link_button("Accéder à mon CV interactif", "https://thom-chhun-cv-interatif.streamlit.app/")
st.link_button("Accéder à mon Linkedin", "https://www.linkedin.com/in/thom-chhun-b7a587233/")

st.write("Actuellement alternant Data Analyst chez Gan Assurances depuis 2 ans, j'ai acquis des compétences solides dans le domaine de l'analyse de données. Cette expérience professionnelle m'a permis de mettre en pratique mes connaissances acquises au cours de mes études et a renforcé ma détermination à devenir Data Scientist en rejoignant le cycle ingénieur Data et IA de l’ESILV à partir de septembre 2024.")
st.write("Le choix d’Engie découle de ma volonté de me perfectionner dans ma vocation. L’opportunité de mettre à profit mes capacités en conception et prototypage de modèles de data science ont été des facteurs déterminants dans ma décision. J'ai foi en Engie pour assurer mon avenir en tant que futur expert en Data Science. Mon objectif en rejoignant votre équipe est d'investir pleinement ma maitrise des langages de programmation Python R afin de permetrtre la prévision de consommations énergétiques.")
st.write("Intégrer votre établissement serait pour moi l’opportunité d'apprendre le métier qui me passionne. Conscient de l'exigence de votre entreprise, je mettrai toute mon énergie dans la réussite de mon travail, tant personnellement que dans le cadre de projets en groupe. Ma rigueur associée à mes connaissances en Machine Learning et en Data Visualisation sont des atouts que j'engagerai au service de mes missions.")

st.divider()

with open("image/CV_Thom_CHHUN.pdf", "rb") as f:
    st.download_button("Télécharger mon CV", f, "CV_Thom_Chhun.pdf")

with open("image/Lettre_de_motivation_Thom_CHHUN.pdf", "rb") as f:
    st.download_button("Télécharger ma lettre de motivation", f, "Lettre_de_motivation_Thom_CHHUN.pdf")