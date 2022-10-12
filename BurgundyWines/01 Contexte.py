import streamlit as st

# Titre Général
st.markdown("<h1 style='color: #c13639;'>Domaine des Croix</h1>", unsafe_allow_html=True)
st.markdown("# Etude de marché sur le vin")
st.markdown("*Projet fictif réalisé dans le cadre de la formation Data Analyst à la Wild Code School de Lyon*")
st.image('images/grapes-g547e23a3b_1920.jpg')

st.markdown("**Le Domaine des Croix**")
st.markdown("Vous possédez un vignoble en Bourgogne, et produisez du Pinot Noir ainsi que du Chardonnay depuis 2000. \
            Vous cherchez à définir le prix de 14 de vos bouteilles de vin pour le marché américain. \
            Vous nous avez fourni un jeu de données de 130k bouteilles de vin, contenant les cépages,\
            les pays et région de production, les millésimes, les notes et descriptifs d'oenologues, \
            et le prix de toutes ces bouteilles sur le marché américain.")
st.markdown("Notre objectif est de vous présenter une analyse du marché, puis d'estimer, à partir de ces données, les prix de vente les plus adaptés.")
