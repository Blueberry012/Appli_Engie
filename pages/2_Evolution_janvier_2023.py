import pandas as pd
import  matplotlib.pyplot as plt
import streamlit as st

df1 = pd.read_csv('data/pdl_1.csv')
df2 = pd.read_csv('data/pdl_2.csv')
df1['timestamp'] = pd.to_datetime(df1['timestamp'])
df2['timestamp'] = pd.to_datetime(df2['timestamp'])

# 3. Filtrer les données pour le mois de janvier 2023
df1_jan_2023 = df1[(df1['timestamp'].apply(lambda x: x.year) == 2023) & (df1['timestamp'].apply(lambda x: x.month) == 1)]
df2_jan_2023 = df2[(df2['timestamp'].apply(lambda x: x.year) == 2023) & (df2['timestamp'].apply(lambda x: x.month) == 1)]

# 4. Identifier les consommations de nuit
df1_night_consumption = df1_jan_2023[(df1_jan_2023['timestamp'].apply(lambda x: x.hour) >= 22) | (df1_jan_2023['timestamp'].apply(lambda x: x.hour) < 6)]
df2_night_consumption = df2_jan_2023[(df2_jan_2023['timestamp'].apply(lambda x: x.hour) >= 22) | (df2_jan_2023['timestamp'].apply(lambda x: x.hour) < 6)]

# 5. Agréger les données par jour et calculer la consommation totale de nuit
df1_night_consumption_per_day = df1_night_consumption.groupby(df1_jan_2023['timestamp'].apply(lambda x: x.day))['value'].sum()
df2_night_consumption_per_day = df2_night_consumption.groupby(df2_jan_2023['timestamp'].apply(lambda x: x.day))['value'].sum()


def main():
    menu_options = ["Point 1 & 2", "Point 1", "Point2"]
    choix_menu = st.sidebar.selectbox("Evolution janvier 2023 :", menu_options)
    st.title("Analyse de l'évolution des consommations de nuit sur le mois de janvier 2023")

    if choix_menu == "Point 1 & 2":
        plt.figure(figsize=(10, 6))
        plt.plot(df1_night_consumption_per_day.index, df1_night_consumption_per_day.values, label='Point 1', marker='o')
        plt.plot(df2_night_consumption_per_day.index, df2_night_consumption_per_day.values, label='Point 2', marker='o')
        plt.xlabel('Jour du mois')
        plt.ylabel('Consommation de nuit (en kWh)')
        plt.title('Évolution de la consommation de nuit en janvier 2023')
        plt.legend()
        plt.grid(True)
        st.pyplot()
        
        st.write("On peut remarquer que la consommation du Point 1 et celle du Point 2 suivent relativement la même tendance avec une diminution brutale de la consommation le 24 janvier.")
        st.write(" Cependant, on remarque que la consommation du Point 2 monte en flèche le 10 janvier, pour atteindre 150 kWh, et diminue tout aussi brutalement le lendemain.")

    elif choix_menu == "Point 1":
        plt.figure(figsize=(10, 6))
        plt.plot(df1_night_consumption_per_day.index, df1_night_consumption_per_day.values, label='Point 1', marker='o')
        plt.xlabel('Jour du mois')
        plt.ylabel('Consommation de nuit (en kWh)')
        plt.title('Évolution de la consommation de nuit en janvier 2023')
        plt.legend()
        plt.grid(True)
        st.pyplot()

    elif choix_menu == "Point 2":
        plt.figure(figsize=(10, 6))
        plt.plot(df2_night_consumption_per_day.index, df2_night_consumption_per_day.values, label='Point 2', marker='o')
        plt.xlabel('Jour du mois')
        plt.ylabel('Consommation de nuit (en kWh)')
        plt.title('Évolution de la consommation de nuit en janvier 2023')
        plt.legend()
        plt.grid(True)
        st.pyplot()


if __name__ == "__main__":
    main()
