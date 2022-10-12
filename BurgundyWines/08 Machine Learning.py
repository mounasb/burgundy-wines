import streamlit as st


st.markdown("<h1 style='color: #c13639;'>Modèles prédictifs</h1>", unsafe_allow_html=True)

st.image('images/code-g698c62cf6_1280.jpg', width=700)
st.text("")
st.markdown("Afin de calculer l'estimation des prix de vos vins sur le marché américain, \
            nous avons comparé plusieurs modèles d'apprentissage automatisé (intelligence artificielle), \
            qui croisent les différents paramètres entre eux.")
st.markdown("Nous les avons entraînés sur plusieurs jeux de données différents\
             pour tenter d'optimiser la pertinence de nos estimations.")

st.text("")
st.markdown("<h4 style='color: #c13639;'>1. Les données numériques</h4>", unsafe_allow_html=True)
st.markdown("Nous avons tout d'abord travaillé sur le jeu de données international, puis sur le cépage Pinot Noir uniquement,\
            en nous concentrant sur les données numériques, à savoir les notes et les millésimes.")

body = '''models = [LinearRegression(), DecisionTreeRegressor()]\n
    X = wines[['points', 'millesime']]\n
    y = wines['price'] \n
    scaler = StandardScaler().fit(X)\n
    X_scaled = scaler.transform(X)\n
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, random_state=42)\n
    for algo in models:\n
        model = algo.fit(X_scaled, y)'''
st.code(body, language = 'python')
st.text("")
st.markdown("Mais ces modèles n'ont pas été très convaincants :")
st.info('''LinearRegression(), training set score : 0.179043868295801\n
LinearRegression(), testing set score : 0.22504696779550581\n
\n
DecisionTreeRegressor(), training set score : 0.31382296327570103\n
DecisionTreeRegressor(), testing set score : 0.36018681475479364\n''')

st.text("")
st.text("")
st.markdown("Nous avons alors tenté d'optimiser le modèle, en jouant sur plusieurs paramètres :")
st.image("charts_img/DTR_max_depth.png")

st.text("")
st.text("")
st.markdown("<h4 style='color: #c13639;'>2. Les données catégorielles</h4>", unsafe_allow_html=True)
st.markdown("Toujours sur le jeu de données international,\
            nous avons observé certaines données catégorielles : le cépage et le pays d'origine des vins.\
            Les résultats se sont avérés plus satisfaisants.")

st.code('''DecisionTreeRegressor(max_depth=8), training set score : 0.45098727037234265\n
DecisionTreeRegressor(max_depth=8), testing set score : 0.4408557783219773''')

st.text("")
st.text("")
st.markdown("Nous avons aussi filtré notre jeu de données en le limitant uniquement au cépage Pinot Noir,\
            puis à la France uniquement, enfin à la Bourgogne.\
            Nous avons comparé les vins notés par un certain oenologue.\
            Finalement, c'est le modèle précédent que nous avons retenu pour effectuer nos estimations.")
