#30-4-2026

#OUDE CODE

# def simple_score(df):
#     #Pak de laatste rij van je data
#     latest = df.iloc[-1]

#     score = 0

#     # trend check: Is de huidige prijs boven het 20 daags gemiddelde
#     if latest["Close"] > latest["ma20"]:
#         score += 4

#     # low volatility bonus: Beoordeel of de stock stabiel is: lager dan 0.02 is stabiel.
#     if latest["volatility"] < 0.02:
#         score += 3

#     # positive return trend: Gemiddelde omzet boven 0.
#     if df["return"].mean() > 0:
#         score += 3

#     # Het eindresultaat returnen
#     return score

# OUDE CODE, VERBETERD

# def simple_score(df):
#     latest = df.iloc[-1]

#     # 1. TREND (0–40 punten): Is de huidige prijs boven het 20 daags gemiddelde
#     trend = 40 if latest["Close"] > latest["ma20"] else 0

#     # 2. MOMENTUM (0–30 punten): # low volatility bonus: Beoordeel of de stock stabiel is: lager dan 0.02 is stabiel.
#     momentum = 30 if df["return"].mean() > 0 else 0

#     # 3. RISK (0–30 punten): # positive return trend: Gemiddelde omzet boven 0.
#     risk = 30 if latest["volatility"] < 0.02 else 0

#     score = trend + momentum + risk

#     return score

#NIEUWE CODE: Nu echt ranking systeem: Betere uitkomsten: gewoon tussen 0 en 100.

import numpy as np

def simple_score(df):
    latest = df.iloc[-1]

    # -------------------------
    # 1. TREND SCORE
    # -------------------------
    ma = df["ma20"]

    trend_z = (latest["Close"] - ma.mean()) / ma.std()
    trend_score = np.tanh(trend_z) * 40   # -40 tot +40

    # -------------------------
    # 2. MOMENTUM SCORE
    # -------------------------
    returns = df["return"].dropna()

    momentum_z = returns.mean() / (returns.std() + 1e-9)
    momentum_score = np.tanh(momentum_z) * 30  # -30 tot +30

    # -------------------------
    # 3. RISK SCORE (lager = beter)
    # -------------------------
    vol = df["volatility"].dropna()

    vol_z = (vol.mean() - vol.mean()) / (vol.std() + 1e-9)
    
    # Tanh zorgt ervoor dat extreme waarden niet exploderen
    risk_score = (1 - np.tanh(vol_z)) * 30  # 0–30 (lager risico = hoger)

    # -------------------------
    # TOTAL SCORE (0–100)
    # -------------------------
    score = 50 + trend_score + momentum_score + risk_score

    return round(max(0, min(score, 100)), 2)