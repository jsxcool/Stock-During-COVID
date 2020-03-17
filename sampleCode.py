import yfinance as yf

# this is an example to get stock information for Microsoft Corp

# type: dictionary (hashmap or say json format)
msft = yf.Ticker("MSFT")

# get stock info
# print(type(msft.info))

"""
{'zip': '98052', 'sector': 'Technology', 'fullTimeEmployees': 144000, 'city': 'Redmond', 'phone': '425-882-8080', 'state': 'WA', 'country': 'United States', 
'companyOfficers': [], 'website': 'http://www.microsoft.com', 'maxAge': 1, 'address1': 'One Microsoft Way', 'fax': '425-706-7329', 'industry': 'Software—Infrastructure', 
'previousClose': 135.42, 'regularMarketOpen': 140, 'twoHundredDayAverage': 153.49956, 'trailingAnnualDividendYield': 0.014325802, 'payoutRatio': 0.32930002, 
'volume24Hr': None, 'regularMarketDayHigh': 147.4998, 'navPrice': None, 'averageDailyVolume10Day': 77632800, 'totalAssets': None, 'regularMarketPreviousClose': 135.42, 
'fiftyDayAverage': 170.53229, 'trailingAnnualDividendRate': 1.94, 'open': 140, 'toCurrency': None, 'averageVolume10days': 77632800, 'expireDate': None, 'yield': None, 
'algorithm': None, 'dividendRate': 2.04, 'exDividendDate': 1589932800, 'beta': 1.091844, 'circulatingSupply': None, 'startDate': None, 'regularMarketDayLow': 135, 
'priceHint': 2, 'currency': 'USD', 'trailingPE': 25.208344, 'regularMarketVolume': 59811479, 'lastMarket': None, 'maxSupply': None, 'openInterest': None, 
'marketCap': 1100755894272, 'volumeAllCurrencies': None, 'strikePrice': None, 'averageVolume': 40122336, 'priceToSalesTrailing12Months': 8.19936, 'dayLow': 135, 
'ask': 144.61, 'ytdReturn': None, 'askSize': 1400, 'volume': 59811479, 'fiftyTwoWeekHigh': 190.7, 'forwardPE': 23.081514, 'fromCurrency': None, 
'fiveYearAvgDividendYield': 2, 'fiftyTwoWeekLow': 115.52, 'bid': 144.84, 'tradeable': True, 'dividendYield': 0.0128, 'bidSize': 800, 'dayHigh': 147.4998, 
'exchange': 'NMS', 'shortName': 'Microsoft Corporation', 'longName': 'Microsoft Corporation', 'exchangeTimezoneName': 'America/New_York', 'exchangeTimezoneShortName': 'EDT', 
'isEsgPopulated': False, 'gmtOffSetMilliseconds': '-14400000', 'quoteType': 'EQUITY', 'symbol': 'MSFT', 'messageBoardId': 'finmb_21835', 'market': 'us_market', 
'annualHoldingsTurnover': None, 'enterpriseToRevenue': 8.648, 'beta3Year': None, 'profitMargins': 0.33016, 'enterpriseToEbitda': 18.95, '52WeekChange': 0.15104115, 
'morningStarRiskRating': None, 'forwardEps': 6.27, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 7606049792, 'fundInceptionDate': None, 
'annualReportExpenseRatio': None, 'bookValue': 14.467, 'sharesShort': 37031775, 'sharesPercentSharesOut': 0.0049, 'fundFamily': None, 'lastFiscalYearEnd': 1561852800,
'heldPercentInstitutions': 0.74410003, 'netIncomeToCommon': 44323000320, 'trailingEps': 5.741, 'lastDividendValue': None, 'SandP52WeekChange': -0.15760958, 
'priceToBook': 10.003532, 'heldPercentInsiders': 0.01421, 'nextFiscalYearEnd': 1625011200, 'mostRecentQuarter': 1577750400, 'shortRatio': 0.82, 
'sharesShortPreviousMonthDate': 1580428800, 'floatShares': 7495150845, 'enterpriseValue': 1160984395776, 'threeYearAverageReturn': None, 'lastSplitDate': 1045526400, 
'lastSplitFactor': '2:1', 'legalType': None, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': 0.383, 'dateShortInterest': 1582848000, 'pegRatio': 1.85, 
'lastCapGain': None, 'shortPercentOfFloat': 0.0049, 'sharesShortPriorMonth': 56674560, 'category': None, 'fiveYearAverageReturn': None, 'regularMarketPrice': 140, 
'logo_url': 'https://logo.clearbit.com/microsoft.com'}

data that may be useful:
'currency': 'USD', 
'regularMarketOpen': 140, 'regularMarketPreviousClose': 135.42,  'dayHigh': 147.4998, 'dayLow': 135, 
'open': 140, 'previousClose': 135.42, 'regularMarketDayHigh': 147.4998, 'regularMarketDayLow': 135,
"""

# get historical market data
# hist = msft.history(period="5d")
# print(hist)

"""
Open    High     Low   Close    Volume  Dividends  Stock Splits
Date
2020-03-11  157.13  157.70  151.15  153.63  56371600          0             0
2020-03-12  145.30  153.47  138.58  139.06  93226400          0             0
2020-03-13  147.50  161.91  140.73  158.83  92727400          0             0
2020-03-16  140.00  149.35  135.00  135.42  87697700          0             0
2020-03-17  140.00  147.50  135.00  145.51  63394881          0             0
"""

# show financials
# print(msft.financials)

# show analysts recommendations
# print(msft.recommendations)

# show next event (earnings, etc)
# print(msft.calendar)

# show options expirations
print(msft.options)