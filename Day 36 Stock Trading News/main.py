import requests
from twilio.rest import Client
import os


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = 'S4HQI80Z94Z6HMI3'
NEWS_API_KEY = '5dc51a86bc0649eba2dec947c6698334'
MSG_API_KEY = "957c6fcebd6d8a592e4f665dccb662b5"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = "ACed8aadda05be248be2ac7804dfe18421"
auth_token = "3a23c3e78e5a3ed2bfdbf99bacfe0528"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    'function' : 'TIME_SERIES_DAILY',
    'symbol' : STOCK_NAME,
    'apikey' : STOCK_API_KEY,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
# print(response.json()['Time Series (Daily)'])
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
# print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data['4. close'])
# print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# positive_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
positive_difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if positive_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = round((positive_difference / yesterday_closing_price) * 100)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage_difference == 0):
    print("Get News")



    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        # 'qInTitle' : COMPANY_NAME,
        'q' : COMPANY_NAME,
        'apiKey' : NEWS_API_KEY,
    }
    news_request = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_request.raise_for_status()


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    # print(len(news_request.json()['articles'][0:3:1]))
    articles = news_request.json()['articles'][0:3:1]
    print(articles)
    # print(articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    articles_headline = [data["title"] for data in articles]
    articles_description = [data["description"] for data in articles]
    # print(articles_headline)
    # print(articles_description)

#TODO 9. - Send each article as a separate message via Twilio.
    for turn in range(len(articles)):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=f"{STOCK_NAME}: {up_down}{percentage_difference}%\n"
                 f"Headline: {articles_headline[turn]}. ({STOCK_NAME})?\n"
                 f"Brief: {articles_description[turn]}",
            to="whatsapp:+6282320835440",
        )
        print(message.body)

else:
    print("Meh")

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

