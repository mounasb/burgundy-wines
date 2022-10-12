import streamlit as st
import pandas as pd
from figs import charts
 

# IMPORTS
wines = pd.read_csv('data/wines_clean.csv', index_col=[0])
wines_fr = pd.read_csv('data/wines_fr.csv', index_col=[0])
wines_pinot = pd.read_csv('data/wines_pinot.csv', index_col=[0])


st.markdown("<h1 style='color: #c13639;'>Analyse des données</h1>", unsafe_allow_html=True)

st.markdown("Nous nous sommes tout d'abord intéressés à l'intégralité du jeu de données, qui comprend près de \
            130.000 références de vins du monde entier, réparties entre 43 pays, 707 cépages, et plus de 16.700 vignobles différents.")
st.markdown("Puis nous nous sommes penchés plus spécifiquement sur les vins français, puis sur le principal cépage que vous produisez : le Pinot Noir.")


# 9 PLOTS (NOTES, PRIX, MILLESIMES)
st.markdown("<h4 style='color: #c13639;'>A. Comparatif des notes, prix et millésimes</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='color: #c13639;'>1. Les notes</h5>", unsafe_allow_html=True)
st.markdown("Elles sont réparties de façon homogène entre 80 et 100, et suivent presque une loi normale. \
            La moyenne des notes attribuées aux vins du cépage Pinot Noir est de 89.4. \
            Elle est supérieure à la moyenne nationale (88.7) et internationale (88.5)")
st.pyplot(charts.fig_points(wines, wines_fr, wines_pinot))
