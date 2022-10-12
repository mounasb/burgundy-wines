import streamlit as st
import pandas as pd
from figs import charts


# IMPORTS
wines = pd.read_csv('data/wines_clean.csv', index_col=[0])
wines_fr = pd.read_csv('data/wines_fr.csv', index_col=[0])
wines_pinot = pd.read_csv('data/wines_pinot.csv', index_col=[0])


st.markdown("<h4 style='color: #c13639;'>C. Les cépages</h4>", unsafe_allow_html=True)
st.markdown("Le Pinot Noir est le cépage le plus représenté dans ce catalogue, avec plus de 12500 références.\
            Le Chardonnay et le Cabernet Sauvignon, eux, comptabilisent respectivement 11752 et 9472 références.\
            On note (sans surprise) que les 3 cépages les plus représentés sont d'origine française")
st.pyplot(charts.fig_varieties(wines))

st.text("")
st.text("")
st.text("")

st.markdown("La Bourgogne est la région qui produit le plus de Pinot Noir, de loin, \
            avec près de 1200 références. \
            La Vallée de la Loire et l'Alsace suivent avec une centaine de références chacune.")
st.pyplot(charts.fig_pinot_province(wines_pinot))
