import streamlit as st
import pandas as pd
import altair as alt

# set Website
st.set_page_config(page_title="Statistics F1 Fantasy",page_icon="🏎️", layout="centered", menu_items={'about': "Made by Julius with Streamlit"})



# add title and explanation
st.title("Willkommen auf der Website der F1 Fans aus Upper Lusatia (und Umgebung)!")
st.write("Lights out and away we go - Hier findest du Statistiken und Informationen zu der schon heute legendären F1-Fantasy-Liga »Upper Lusatia F1 Fans«.")

# add tabs
tab1, tab2, tab3 = st.tabs(["🏎️ Qualifying", "🏁 Weekend", "🏆 Hall of Fame"])

#tab1
with tab1:
    st.header("Qualifying", divider="red")
    
    #bar chart pole positions
    from Statistics import pole_position_df
    st.bar_chart(pole_position_df)

#tab2
with tab2:
    st.header("Weekend", divider="green")
    
    st.subheader("Saisonverlauf")
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
    st.subheader("Ewige Tabelle")
    from Statistics import ewige_tabelle
    st.dataframe(ewige_tabelle)
