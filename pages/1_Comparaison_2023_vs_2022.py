import pandas as pd
import  matplotlib.pyplot as plt
import streamlit as st

df1 = pd.read_csv('data\pdl_1.csv')
df2 = pd.read_csv('data\pdl_2.csv')
df1['timestamp'] = pd.to_datetime(df1['timestamp'])
df2['timestamp'] = pd.to_datetime(df2['timestamp'])

df1['month'] = df1['timestamp'].apply(lambda x: x.month)
df1_2022 = df1[df1['timestamp'].apply(lambda x: x.year) == 2022]
df1_2023 = df1[df1['timestamp'].apply(lambda x: x.year) == 2023]

df1_monthly_consumption_2022 = df1_2022.groupby('month')['value'].sum()
df1_monthly_consumption_2023 = df1_2023.groupby('month')['value'].sum()

df2['month'] = df2['timestamp'].apply(lambda x: x.month)
df2_2022 = df2[df2['timestamp'].apply(lambda x: x.year) == 2022]
df2_2023 = df2[df2['timestamp'].apply(lambda x: x.year) == 2023]

df2_monthly_consumption_2022 = df2_2022.groupby('month')['value'].sum()
df2_monthly_consumption_2023 = df2_2023.groupby('month')['value'].sum()


def main():
    menu_options = ["Point 1 & 2", "Point 1", "Point 2"]
    choix_menu = st.sidebar.selectbox("Comparaison 2022 vs 2023 :", menu_options)
    st.title("Comparaison de la consommation mensuelle de 2023 vs 2022")

    if choix_menu == "Point 1 & 2":
        plt.figure(figsize=(10, 6))
        plt.plot(df1_monthly_consumption_2022.index, df1_monthly_consumption_2022.values, label='2022')
        plt.plot(df1_monthly_consumption_2023.index, df1_monthly_consumption_2023.values, label='2023')
        plt.xlabel('Mois')
        plt.ylabel('Consommation Totale (en kWh)')
        plt.title('Comparaison de la consommation mensuelle du Point 1 (2022 vs 2023)')
        plt.legend()
        st.pyplot()

        st.write("On peut remarque qu'on consomme globalement plus en 2022 qu'en 2023, mis a part pendant le mois de septembre et en fin d'année à partir de mi octobre")

        st.divider()

        plt.figure(figsize=(10, 6))
        plt.plot(df2_monthly_consumption_2022.index, df2_monthly_consumption_2022.values, label='2022')
        plt.plot(df2_monthly_consumption_2023.index, df2_monthly_consumption_2023.values, label='2023')
        plt.xlabel('Mois')
        plt.ylabel('Consommation Totale (en kWh)')
        plt.title('Comparaison de la consommation mensuelle du Point 2 (2022 vs 2023)')
        plt.legend()
        st.pyplot()

        st.write("On peut remarque que la consommation de Point 1 et celle du Point 2 suivent tous les deux la même tendance, c'est l'échelle de la consommation qui change.")

    elif choix_menu == "Point 1":
        plt.figure(figsize=(10, 6))
        plt.plot(df1_monthly_consumption_2022.index, df1_monthly_consumption_2022.values, label='2022')
        plt.plot(df1_monthly_consumption_2023.index, df1_monthly_consumption_2023.values, label='2023')
        plt.xlabel('Mois')
        plt.ylabel('Consommation Totale (en kWh)')
        plt.title('Comparaison de la consommation mensuelle du Point 1 (2022 vs 2023)')
        plt.legend()
        st.pyplot()

    elif choix_menu == "Point 2":
        plt.figure(figsize=(10, 6))
        plt.plot(df2_monthly_consumption_2022.index, df2_monthly_consumption_2022.values, label='2022')
        plt.plot(df2_monthly_consumption_2023.index, df2_monthly_consumption_2023.values, label='2023')
        plt.xlabel('Mois')
        plt.ylabel('Consommation Totale (en kWh)')
        plt.title('Comparaison de la consommation mensuelle du Point 2 (2022 vs 2023)')
        plt.legend()
        st.pyplot()


if __name__ == "__main__":
    main()
