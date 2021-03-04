import requests
from twilio.rest import Client

STOCK_NAME = "your_company_stock_name"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "your_alphavantage_API_KEY"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

COMPANY_NAME = "your_company_name"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "your_news_API_KEY"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

# Twilio Credentials
ACCOUNT_SID = "your_twilio_account_sid"
AUTH_TOKEN = "your_twilio_auth_token"

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_closing_price = data_list[1]["4. close"]

price_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if price_difference > 0:
    up_down = "👆"
else:
    up_down = "👇"

price_difference = abs(price_difference)
percent_price_difference = round((price_difference / float(yesterday_closing_price)) * 100)

if percent_price_difference > 1:
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    articles = response.json()["articles"]
    first_three_articles = articles[:3]
    article_list = [f"{STOCK_NAME}: {up_down}{percent_price_difference}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in
                    first_three_articles]
    
    client = Client(ACCOUNT_SID, AUTH_TOKEN)  # twilio API, sending sms

    for article in article_list:
        message = client.messages \
            .create(
            body=article,
            from_='your_twilio_phone_number',
            to='your_phone_number_with_country_code'
        )
