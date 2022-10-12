import streamlit as st
import pandas as pd
from figs import charts


# IMPORTS
wines = pd.read_csv('data/wines_clean.csv', index_col=[0])
wines_fr = pd.read_csv('data/wines_fr.csv', index_col=[0])
wines_pinot = pd.read_csv('data/wines_pinot.csv', index_col=[0])


# MILLÉSIMES
st.markdown("<h5 style='color: #c13639;'>3. Les millésimes</h5>", unsafe_allow_html=True)
st.markdown("Ils s'étendent de 1904 à 2021 \
            sauf pour le Pinot Noir, pour lequel le millésime le plus ancien date de 2000. \
            À l'international, 2017 est l'année où le plus de vins ont été produits. \
            En France, et pour le Pinot Noir, c'est 2020 et 2018 qui ont respectivement été les plus généreuses.")
st.pyplot(charts.fig_millesimes(wines, wines_fr, wines_pinot))
