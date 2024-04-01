import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
import xgboost as xgb
import seaborn as sns
from sklearn.metrics import mean_squared_error
import streamlit as st
from contextlib import contextmanager, redirect_stdout
from io import StringIO
#pip install scikit-learn

df1 = pd.read_csv('data/pdl_1.csv')
df2 = pd.read_csv('data/pdl_2.csv')

#Scikit-Learn

def main():
    menu_options = ["Point 1", "Point 2"]
    choix_menu = st.sidebar.selectbox("Machine Learning :", menu_options)
    st.title("Modélisation prédictive par régression de la consommation")

    if choix_menu == "Point 1":
        df = df1

    elif choix_menu == "Point 2":
        df = df2
    

    df = df.set_index('timestamp')
    df.index = pd.to_datetime(df.index)
    df.index = pd.to_datetime(df.index, utc=True).tz_convert(None)

    color_pal = sns.color_palette()
    plt.style.use('fivethirtyeight')


    #Prévision des séries temporelles
    st.subheader("Affichage de la série temporelle de consommation")

    df.plot(style='.',
            figsize=(15, 5),
            color=color_pal[0],
            title='Consommation (en kWh)')
    st.pyplot()
     

    #Echantillon de test et d'apprentissage
    st.subheader("Echantillon de test et d'apprentissage")

    train = df.loc[df.index < '2023-07-01']
    test = df.loc[df.index >= '2023-07-01']

    fig, ax = plt.subplots(figsize=(15, 5))
    train.plot(ax=ax, label="Echantillon d'apprentissage", title='Consommation (en kWh)')
    test.plot(ax=ax, label='Echantillon de test')
    ax.axvline('2023-07-01', color='black', ls='--')
    ax.legend(["Echantillon d'apprentissage", 'Echantillon de test'])
    st.pyplot()

    df.loc[(df.index > '09-01-2023') & (df.index < '09-08-2023')] \
    .plot(figsize=(15, 5), title='Consommation sur une semaine')
    st.pyplot()

    st.write("On peut remarquer tous les jours, il y a un voire deux pics de consommation. Neamoins, il n'y a eu presque aucune consommation le 3 septembre.")


    #Visualiser la relation entre la variable et la cible
    st.subheader("Visualiser la relation entre la variable et la cible")

    def create_features(df):
        df = df.copy()
        df['hour'] = df.index.hour
        df['dayofweek'] = df.index.dayofweek
        df['month'] = df.index.month
        df['year'] = df.index.year
        df['dayofyear'] = df.index.dayofyear
        df['dayofmonth'] = df.index.day
        df['weekofyear'] = df.index.isocalendar().week
        return df
    
    df = create_features(df)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.boxplot(data=df, x='hour', y='value')
    ax.set_title('Consommation par heure (en kWh)')
    st.pyplot()

    st.write("Il semble n'y avoir aucune consommation entre 19h et 4h. Cependant la consommation est constante entre 7h et 16h.")

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.boxplot(data=df, x='month', y='value', palette='Blues')
    ax.set_title('Consommation par mois (en kWh)')
    st.pyplot()

    st.write("On peut voir que la comsommation par mois a tendance à culminer deux fois dans l'année. Un premier pic de consommation en hiver, puis un deuxième en plein milieu de l'été.")


    #Créer mon modèle de régression
    st.subheader("Créer mon modèle de régression")

    train = create_features(train)
    test = create_features(test)
    FEATURES = ['dayofyear', 'hour', 'dayofweek', 'month', 'year']
    TARGET = 'value'
    X_train = train[FEATURES]
    y_train = train[TARGET]
    X_test = test[FEATURES]
    y_test = test[TARGET]

    code = '''reg = xgb.XGBRegressor(base_score=0.5, booster='gbtree',    
                       n_estimators=1000,#le nombre d'arbres
                       early_stopping_rounds=50,#50 arbres
                       objective='reg:linear',
                       max_depth=3,
                       learning_rate=0.01)# évite le surapprentissage
    
    reg.fit(X_train, y_train,
            eval_set=[(X_train, y_train), (X_test, y_test)],
            verbose=100)'''
    
    st.code(code, language='python')

    reg = xgb.XGBRegressor(base_score=0.5, booster='gbtree',    
                       n_estimators=1000,#le nombre d'arbres
                       early_stopping_rounds=50,#50 arbres
                       objective='reg:linear',
                       max_depth=3,
                       learning_rate=0.01)# évite le surapprentissage
    
    reg.fit(X_train, y_train,
            eval_set=[(X_train, y_train), (X_test, y_test)],
            verbose=100)
    
    st.write("On crée 1000 arbres de décision mais le modèle s'est arrêté à 639 arbres car l'écart quadratique moyen commencait à augmenter.")
    st.write("Pour éviter le surapprentissage, je place le taux d'apprentissage à 0.01")

    #Importance des variables
    st.subheader("Importance des variables dans le modèle")

    fi = pd.DataFrame(data=reg.feature_importances_,
             index=reg.feature_names_in_,
             columns=['importance'])
    fi.sort_values('importance').plot(kind='barh', title='Importance des variables')
    st.pyplot()

    st.write("Nous pouvons voir que pour notre modèle, les caractéristiques de l'heure et du jour de la semaine ont vraiment beaucoup d'importance, l'année et le jour de l'année ont moins d'importance et le mois n'en a pas beaucoup.")
    st.write("Il faut gardez à l'esprit que ce graphique ne nous dira pas exactement quelle est l'importance de chaque caractéristique individuellement, mais plutôt en tant qu'ensemble de variables dans ce modèle.")


    #Prévisions sur le test
    st.subheader("Prévisions sur le test")

    test['prediction'] = reg.predict(X_test)
    df = df.merge(test[['prediction']], how='left', left_index=True, right_index=True, suffixes=('', '_test'))
    ax = df[['value']].plot(figsize=(15, 5))
    df['prediction'].plot(ax=ax)
    plt.legend(['Données réelles', 'Prévisions'])
    ax.set_title('Données brutes et prévisions')
    st.pyplot()

    ax = df.loc[(df.index > '09-01-2023') & (df.index < '09-08-2023')]['value'] \
        .plot(figsize=(15, 5), title='Prédiction de la consommation sur une semaine')
    df.loc[(df.index > '09-01-2023') & (df.index < '09-08-2023')]['prediction'] \
        .plot(style='-')
    plt.legend(['Données réelles', 'Prévisions'])
    st.pyplot()

    st.write("On peut voir que le modèle n'est pas parfait, il y a quelques amélioration qui peuvent être fait.")
    st.write("L'une des idées serait d'ajouter les caractéristiques pour des jours spéciaux, comme les vacances, les jours fériés ou les fêtes par exemple. En effet, ces jours peuvent augmenter ou diminuer la consommation.")
    st.write("Neanmoins, on peut voir que notre prédictions sur l'échantillon de test dans la semaine suit globalement la tendance qu'on pourrait s'attendre à voir avec une consommation plus au moisn constante durant la journée et des creux pendant la nuit.")


    #L'écart quadratique moyen (RMSE)
    st.subheader("L'écart quadratique moyen (RMSE)")

    score = np.sqrt(mean_squared_error(test['value'], test['prediction']))
    st.write(f"L'écart quadratique moyen sur l'échantillon de test : {score:0.2f}")


    #Erreurs de prévision
    st.subheader("Erreurs de prévision")

    test['error'] = np.abs(test[TARGET] - test['prediction'])
    test['date'] = test.index.date
    st.write(test.groupby(['date'])['error'].mean().sort_values(ascending=False).head(10))
    
    st.write("On constate alors que les jours les moins biesn prédis se trouvent majoritairement en août 2023.")


    #Pistes d'amélioration
    st.subheader("Pistes d'amélioration")
    st.write("Pour améliorer la performance du modèle, on pourrait ajouter une validation croisée plus robuste (cross validation).")
    st.write("On pourrait également ajouter des caractéristiques externes comme la météo, le lieu du site observé ou les jours spéciaux.")

    
if __name__ == "__main__":
    main()
