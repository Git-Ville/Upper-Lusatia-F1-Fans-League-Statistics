import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

#Erstellung Website
st.set_page_config(page_title="Statistiken Upper Lusatia F1 Fans", layout="centered")



# Hinzufügen von Inhalt
st.title("Willkommen auf der Website der F1 Fans in Upper Lusatia!")
st.write("Hier findest du Statistiken und Informationen zu F1-Fans in Upper Lusatia.")

tab1, tab2, tab3 = st.tabs(["Qualifying", "Race", "Hall of Fame"])

with tab1:
    st.header("Qualifying", divider=True)
    from Statistics import pole_position_df
    st.bar_chart(pole_position_df)

with tab2:
    st.header("Race", divider=True)
    from Statistics import Rennsiege_df
    st.bar_chart(Rennsiege_df)
    from Statistics import rennen_gesamt_transponiert
    st.line_chart(rennen_gesamt_transponiert)
    from Statistics import rennen_gesamtrang_transponiert
    st.line_chart(rennen_gesamtrang_transponiert)
    from Statistics import Abstände_transponiert
    st.line_chart(Abstände_transponiert)

with tab3:
    st.header("Hall of Fame", divider=True)