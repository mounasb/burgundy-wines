import streamlit as st
import pandas as pd


vins_croix = pd.read_csv('data/vins_croix_predict.csv', index_col=[0])
vins_croix.rename(columns={'Notes': 'Note'}, inplace=True)

st.markdown("<h1 style='color: #c13639;'>Estimation des prix</h1>", unsafe_allow_html=True)
st.image('images/wine-g5b10738f3_1280.jpg', width=700)

st.text("")
st.text("")

st.markdown("Après une analyse approfondie des données et de leur contexte, ainsi qu'un travail rigoureux\
            sur les algorithmes de prédiction, nous sommes arrivés aux estimations suivantes :")

st.table(vins_croix)
