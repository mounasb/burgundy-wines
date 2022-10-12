import streamlit as st
import pandas as pd
from figs import charts


# IMPORTS
wines = pd.read_csv('data/wines_clean.csv', index_col=[0])
wines_fr = pd.read_csv('data/wines_fr.csv', index_col=[0])
wines_pinot = pd.read_csv('data/wines_pinot.csv', index_col=[0])


# PRIX
st.markdown("<h5 style='color: #c13639;'>2. Les prix</h5>", unsafe_allow_html=True)
st.markdown("Ils sont très hétérogènes, allant de 4\$ à 3300\$ (2500\$ pour le Pinot Noir).\
            Cependant ces prix élevés sont très minoritaires.\
            En effet, 75% des vins référencés sont vendus à moins de 40\$,\
            et 75% des vins Pinot Noir sont vendus à moins de 55\$.")
st.pyplot(charts.fig_prices(wines, wines_fr, wines_pinot))
