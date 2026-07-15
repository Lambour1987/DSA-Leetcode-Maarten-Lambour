# is bedoelt om te kijken of we met de huidige strategie ook resultaat hadden behaald in het verleden


#dit weer weggehaald omdat het tot problemen leidde
# import numpy as np

# def run_backtest(data, tickers, add_features, simple_score):

#     portfolio_returns = []
#     dates = data["AAPL"].index

#     for i in range(50, len(dates)-1):

#         scores = []

#         for ticker in tickers:

#             try:
#                 df = data[ticker].iloc[:i].copy()
#             except:
#                 continue

#             if len(df) < 50:
#                 continue

#             df = add_features(df)
#             df = df.dropna()

#             if df.empty:
#                 continue

#             score = simple_score(df)
#             scores.append((ticker, score))

#         scores.sort(key=lambda x: x[1], reverse=True)
#         top = scores[:5]

#         daily_return = 0
#         count = 0

#         for ticker, score in top:
#             try:
#                 price_now = data[ticker].iloc[i]["Close"]
#                 price_next = data[ticker].iloc[i+1]["Close"]

#                 ret = (price_next - price_now) / price_now

#                 daily_return += ret
#                 count += 1
#             except:
#                 continue

#         if count > 0:
#             portfolio_returns.append(daily_return / count)

#     cumulative = np.cumprod([1 + r for r in portfolio_returns])[-1]

#     print("\nBACKTEST RESULT:", cumulative)


