# 30-4-2026 hier gaan we de data bewerken: eigen data van maken

import pandas as pd

# inputparameter is data
def add_features(df):
    #maak een kopie van de data: veilig bewerkingen uitvoeren
    df = df.copy()


    #Maak nieuwe kolommen aan met berekeningen, gebaseerd op eerdere data
    #Maak koplom "return": % verandering t.o.v. voorgaande dag
    df["return"] = df["Close"].pct_change()

    #Gemiddelde van de laatste 20 dagen:
    #dag 20 → gemiddelde dag 1 t/m 20  
    #dag 21 → gemiddelde dag 2 t/m 21  
    #dag 22 → gemiddelde dag 3 t/m 22  
    df["ma20"] = df["Close"].rolling(20).mean()
    
    #spreiding van returns over laatste 20 dagen
    df["volatility"] = df["return"].rolling(20).std()

    return df