import streamlit as st
import pandas as pd

# set Website
st.set_page_config(page_title="Statistiken Upper Lusatia F1 Fans", layout="centered")



# add title and explanation
st.title("Willkommen auf der Website der F1 Fans in Upper Lusatia!")
st.write("Hier findest du Statistiken und Informationen zu F1-Fans in Upper Lusatia.")

# add tabs
tab1, tab2, tab3 = st.tabs(["🔴 Qualifying", "🟢 Race", "🟠 Hall of Fame"])

#tab1
with tab1:
    st.header("Qualifying", divider="red")
    
    #bar chart pole positions
    from Statistics import pole_position_df
    st.bar_chart(pole_position_df)

#tab2
with tab2:
    st.header("Race", divider="green")
    
    st.subheader("Saisonverlauf", colors = [
    "#1f77b4",  # Blau
    "#ff7f0e",  # Orange
    "#2ca02c",  # Grün
    "#d62728",  # Rot
    "#9467bd",  # Lila
    "#8c564b",  # Braun
    "#e377c2",  # Pink
    "#7f7f7f",  # Grau
    "#bcbd22",  # Gelb
    "#17becf",  # Cyan
]
)
    # line chart placement history 
    from Statistics import rennen_gesamtrang_transponiert
    st.line_chart(rennen_gesamtrang_transponiert)

    st.subheader("Abstände")
    # line chart relative distances
    from Statistics import Abstände_transponiert
    st.line_chart(Abstände_transponiert)
  
    st.subheader("Gesamtpunkte")
    #line chart total points
    from Statistics import rennen_gesamt_transponiert
    st.line_chart(rennen_gesamt_transponiert)

    st.subheader("Rennsiege")
    #bar chart race wins
    from Statistics import Rennsiege_df
    st.bar_chart(Rennsiege_df)
    

#tab3
with tab3:
    st.header("Hall of Fame", divider="orange")