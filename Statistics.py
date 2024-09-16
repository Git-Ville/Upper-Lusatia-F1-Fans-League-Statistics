# Hier importieren wir alle notwendigen Module

import pandas as pd

# Hier lesen wir die Daten ein
data_quali = pd.read_csv("Data/Quali.csv", encoding="utf-8", sep=";", index_col=0)



#alle Werte zu int
data_quali = data_quali.astype(int)


pole_position_counts = {}

# Loop durch jede Spalte
for column in data_quali.columns:
    # Finden Sie den Teilnehmer mit der höchsten Punktzahl in der aktuellen Spalte
    max_score = data_quali[column].max()

    # Überprüfen, ob es mehrere Teilnehmer mit der höchsten Punktzahl gibt
    max_participants = data_quali[data_quali[column] == max_score].index.tolist()
    
    # Loop durch jeden Teilnehmer in der Liste der Teilnehmer mit den höchsten Punktzahlen
    for participant in max_participants:
        # Wenn der Teilnehmer nicht im Dictionary ist, füge ihn hinzu und setze den Zähler auf 1
        if participant not in pole_position_counts:
            pole_position_counts[participant] = 1
        else:
            # Andernfalls erhöhe den Zähler um 1
            pole_position_counts[participant] += 1
    
    # Füge Teilnehmer mit 0 Pole-Positionen hinzu
    for participant in data_quali.index:
        if participant not in pole_position_counts:
            pole_position_counts[participant] = 0
    

# Erstelle ein DataFrame aus dem Dictionary
pole_position_df = pd.DataFrame.from_dict(pole_position_counts, orient='index', columns=['Pole Positions'])
pole_position_df.index.name = 'Team'
pole_position_df.sort_values(by="Pole Positions", inplace=True, ascending=False)


# Hier lesen wir die Daten ein
data_rennen = pd.read_csv("Data/Rennen.csv", encoding="utf-8", sep=",", index_col=0)

#alle Werte zu int
data_rennen = data_rennen.astype(int)


Rennsiege_counts = {}

# Loop durch jede Spalte
for column in data_rennen.columns:
    # Finden Sie den Teilnehmer mit der höchsten Punktzahl in der aktuellen Spalte
    max_score = data_rennen[column].max()

    # Überprüfen, ob es mehrere Teilnehmer mit der höchsten Punktzahl gibt
    max_participants = data_rennen[data_rennen[column] == max_score].index.tolist()
    
    # Loop durch jeden Teilnehmer in der Liste der Teilnehmer mit den höchsten Punktzahlen
    for participant in max_participants:
        # Wenn der Teilnehmer nicht im Dictionary ist, füge ihn hinzu und setze den Zähler auf 1
        if participant not in Rennsiege_counts:
            Rennsiege_counts[participant] = 1
        else:
            # Andernfalls erhöhe den Zähler um 1
            Rennsiege_counts[participant] += 1
    
    # Füge Teilnehmer mit 0 Pole-Positionen hinzu
    for participant in data_rennen.index:
        if participant not in Rennsiege_counts:
            Rennsiege_counts[participant] = 0

# Erstelle ein DataFrame aus dem Dictionary
Rennsiege_df = pd.DataFrame.from_dict(Rennsiege_counts, orient='index', columns=['Rennsiege'])
Rennsiege_df.index.name = 'Team'
Rennsiege_df.sort_values(by="Rennsiege", inplace=True, ascending=False)


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


# Saisonverlauf (Punkte der Rennwochenenden addiert)

# Transponieren des DataFrames
rennen_gesamt_transponiert = rennen_gesamt.transpose()

rennen_gesamtrang = rennen_gesamt.rank(ascending=False)
rennen_gesamtrang = rennen_gesamtrang.astype("int")
rennen_gesamtrang.sort_values(by=rennen_gesamtrang.columns[-1], inplace=True)


# Transponieren des DataFrames
rennen_gesamtrang_transponiert = rennen_gesamtrang.transpose()
rennen_gesamtrang_transponiert = rennen_gesamtrang_transponiert * -1


#Hier erstellen wir eine neue Zeile, welche den Durchschnitt der Liga abbildet
data_rennen_average = rennen_gesamt
average = rennen_gesamt.mean()

data_rennen_average.loc[11] = average
data_rennen_average = data_rennen_average.rename(index={11: 'Average'})

# Hier erstellen wir ein neues DataFrame, welches den Abstand zum Durchschnitt abbildet
Abstände = pd.DataFrame()

# Holen des Durchschnitts für jede Spalte aus der elften Zeile
durchschnittszeile = data_rennen_average.iloc[-1]

# Schleife über die Spalten der Ausgangstabelle
for spalte in data_rennen_average.columns:
    # Berechnen der Differenz jedes Elements in der aktuellen Spalte zum Durchschnitt in der elften Zeile
    neue_spalte = data_rennen_average[spalte] - durchschnittszeile[spalte]
    
    # Hinzufügen der neuen Spalte zur neuen Tabelle
    Abstände[f'Abstand_{spalte}'] = neue_spalte

# Umbenennen der Spalten in numerische Reihenfolge
Abstände.columns = range(1, len(Abstände.columns) + 1)

Abstände.sort_values(Abstände.columns[-1], inplace=True, ascending=False)

# Transponieren des DataFrames
Abstände_transponiert = Abstände.transpose()

# ewige Tabelle
ewige_tabelle = pd.read_csv("Data/ewige_tabelle.csv", encoding="utf-8", sep=";")
print(ewige_tabelle)