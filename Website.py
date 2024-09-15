import streamlit as st
import pandas as pd

#Erstellung Website
st.set_page_config(page_title="Statistiken Upper Lusatia F1 Fans", layout="centered")

# Hinzufügen von Inhalt
st.title("Willkommen auf der Website der F1 Fans in Upper Lusatia!")
st.write("Hier findest du Statistiken und Informationen zu F1-Fans in Upper Lusatia.")
st.header("Qualifying", divider=True)
st.header("Race", divider=True)

# Hier lesen wir die Daten ein
data_rennen = pd.read_csv("Data/Rennen.csv", encoding="utf-8", sep=",", index_col=0)
#alle Werte zu int
data_rennen = data_rennen.astype(int)

#Hier erstellen wir eine neues Dataframe um die Gesamtpunkte anzuzeigen
rennen_gesamt = pd.DataFrame()

# Schleife über die Spalten der Ausgangstabelle
for spalten_index, spalte in enumerate(data_rennen.columns):
    # Berechnen der kumulativen Summe für jede Spalte
    neue_spalte = data_rennen.iloc[:, :spalten_index + 1].sum(axis=1)
    # Hinzufügen der neuen Spalte zur neuen Tabelle
    rennen_gesamt[f'Summe bis Spalte {spalten_index + 1}'] = neue_spalte

# Umbenennen der Spalten in numerische Reihenfolge
rennen_gesamt.columns = range(1, len(rennen_gesamt.columns) + 1)
rennen_gesamt.sort_values(by=rennen_gesamt.columns[-1], inplace=True, ascending=False)
# Transponieren des DataFrames
rennen_gesamt_transponiert = rennen_gesamt.transpose()

chart_data = rennen_gesamt_transponiert

st.line_chart(chart_data)

st.header("Hall of Fame", divider=True)