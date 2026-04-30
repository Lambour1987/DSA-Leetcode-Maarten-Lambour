#30-4-2026: Hier halen we de data op

# Gebruik de Yahoo Library Finance
import yfinance as yf

# Test bestand data ophalen. Werkt.
#"AAPL" is Apple incorporated
# van de Yahoo library roep de download functie aan
# data = yf.download("AAPL", start="2020-01-01")
#Download alle data vanaf januari 2020
#df is DataFrame
# Meerdere requests naar de server: die slaan we op in data
def load_data(tickers):
    return yf.download(tickers, start="2020-01-01", group_by="ticker")


# print de eerste 5 rijen met head: testbestand
# print(data.head)