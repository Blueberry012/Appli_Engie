import pandas as pd
import  matplotlib.pyplot as plt
import streamlit as st

df1 = pd.read_csv('data\pdl_1.csv')
df2 = pd.read_csv('data\pdl_2.csv')
df1['timestamp'] = pd.to_datetime(df1['timestamp'])
df2['timestamp'] = pd.to_datetime(df2['timestamp'])

# 3. Define a function to get the week number from a timestamp
def get_week_number(timestamp):
    return timestamp.isocalendar()[1]  # Get the ISO week number

# 4. Apply the function to create a new column for week number
df1['week_number'] = df1['timestamp'].apply(get_week_number)
df2['week_number'] = df2['timestamp'].apply(get_week_number)

# 5. Filter the data for February 2023
df1_feb_2023_data = df1[(df1['timestamp'].apply(lambda x: x.year) == 2023) & (df1['timestamp'].apply(lambda x: x.month) == 2)]
df2_feb_2023_data = df2[(df2['timestamp'].apply(lambda x: x.year) == 2023) & (df2['timestamp'].apply(lambda x: x.month) == 2)]

# 6. Analyze consumption patterns for each week
df1_weekly_profiles = df1_feb_2023_data.groupby('week_number')['value'].mean()
df2_weekly_profiles = df2_feb_2023_data.groupby('week_number')['value'].mean()


def main():
    menu_options = ["Point 1 & 2", "Point 1", "Point 2"]
    choix_menu = st.sidebar.selectbox("Profils février 2023 :", menu_options)
    st.title("Mise en évidence des différents profils de consommation hebdomadaire sur le mois de février 2023")

    if choix_menu == "Point 1 & 2":
        plt.figure(figsize=(10, 6))
        plt.plot(df1_weekly_profiles.index, df1_weekly_profiles.values, label='Point 1', marker='D', ls="--")
        plt.plot(df2_weekly_profiles.index, df2_weekly_profiles.values, label='Point 2', marker='.', ls="dotted")
        plt.xlabel('Numéro de Semaine')
        plt.ylabel('Consommation Moyenne (en kWh)')
        plt.title('Profils de Consommation Hebdomadaires en février 2023')
        plt.legend()
        plt.grid(True)
        st.pyplot()

        st.write("On remarque que la consommation du Point 1 et celle du Point 2 est strictement identique car les deux courbes se superposent parfaitement.")

    elif choix_menu == "Point 1":
        plt.figure(figsize=(10, 6))
        plt.plot(df1_weekly_profiles.index, df1_weekly_profiles.values, label='Point 1', marker='o')
        plt.xlabel('Numéro de Semaine')
        plt.ylabel('Consommation Moyenne (en kWh)')
        plt.title('Profils de Consommation Hebdomadaires en février 2023')
        plt.legend()
        plt.grid(True)
        st.pyplot()

    elif choix_menu == "Point 2":
        plt.figure(figsize=(10, 6))
        plt.plot(df2_weekly_profiles.index, df2_weekly_profiles.values, label='Point 2', marker='o')
        plt.xlabel('Numéro de Semaine')
        plt.ylabel('Consommation Moyenne (en kWh)')
        plt.title('Profils de Consommation Hebdomadaires en février 2023')
        plt.legend()
        plt.grid(True)
        st.pyplot()


if __name__ == "__main__":
    main()