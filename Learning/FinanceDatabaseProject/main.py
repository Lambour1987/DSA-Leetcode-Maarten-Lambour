#30-4-2026 hier run je alles samen

# from backtest import run_backtest
# data ophalen uit dataloader.py
from data_loader import load_data
# import eigen tabblad features
from features import add_features
# import eigen tabblad scoring
from scoring import simple_score

# Bedrijven ophalen: Lijst met bedrijven
# Hoe meer bedrijven, hoe meer missing data. Meer noise.
tickers = [
    "AAPL", "MSFT", "TSLA", "AMZN", "NVDA",
    "META", "GOOGL", "NFLX", "AMD", "INTC",
    "JPM", "BAC", "GS", "V", "MA",
    "DIS", "KO", "PEP", "WMT", "NKE",
    "XOM", "CVX", "HD", "UNH", "PFE",
    "ABT", "CRM", "ORCL", "ADBE", "CSCO",
    "IBM", "T", "VZ", "SPGI", "BLK",
    "COST", "MCD", "SBUX", "BA", "CAT",
    "GE", "F", "GM", "UBER", "LYFT",
    "SQ", "PYPL", "SHOP", "PLTR", "RIVN"
]

# Gebruik load_data functie
data = load_data(tickers)

#Resultaten in een list
results = []

#Voor ieder bedrijf gaan we gegevens ophalen
for ticker in tickers:   

    #bij onvoldoende gegevens?
    # We willen alles gewoon in 1 batch bestand hebben dus dat is 1 call naar de server.
    try:
        df = data[ticker].copy()
    except Exception:
        print(f"{ticker} skipped (data issue)")
        continue

    #Bij missing data controleren
    if df.empty or len(df)<50:
        print(f"{ticker} skipped (no data)")
        continue

    #features
    df = add_features(df)

    #NaN: Not A Number: een pandas functie die verwijdert missende data
    df=df.dropna()

    #Dus: print volgens mij de bedrijven die lege waarden hebben
    if df.empty:
        print(f"{ticker} skipped (after features)")
        continue

    #data die we krijgen flattenen
    #df.columns = df.columns.get_level_values(0)
    #score
    score = simple_score(df)

    #toevoegen ticker en score aan lijst resultaat
    results.append((ticker, score))

    #opslaan
    print(ticker, "Score:", score)

#sorteren: Sorteer op 2e waarde
results.sort(key=lambda x: x[1], reverse=True)

# printen
print("\nTOP PICKS:")
for ticker, score in results:
    print(ticker, "→", score)

#Dit kan weg
#alleen backtest runnen: alle logica staat daar
## run_backtest(data, tickers, add_features, simple_score)
