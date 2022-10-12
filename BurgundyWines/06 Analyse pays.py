import streamlit as st
import pandas as pd
from figs import charts


# IMPORTS
wines = pd.read_csv('data/wines_clean.csv', index_col=[0])
wines_fr = pd.read_csv('data/wines_fr.csv', index_col=[0])
wines_pinot = pd.read_csv('data/wines_pinot.csv', index_col=[0])


st.markdown("<h4 style='color: #c13639;'>B. Les pays producteurs</h4>", unsafe_allow_html=True)
st.markdown("Les États-Unis restent le pays producteur majoritaire, de loin, \
            avec plus de 50000 références de vins, dont presque 10000 de Pinot Noir. \
            La France est le deuxième pays le plus producteur, comptabilisant \
            plus de 16300 références, dont plus de 1400 de Pinot Noir.\
            Tous cépages confondus, l'Italie produit presque autant de vins que la France")

st.pyplot(charts.fig_countries(wines, wines_pinot))
