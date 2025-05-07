import smtplib
import datetime as dt
import pandas as pd
import random


MY_EMAIL = "yesorry32@gmail.com"
MY_PASSWORD = "sraf ocot mvis yosg"
# data = pd.read_csv('quotes.txt')
# list_quotes = data.values.tolist()

# print((random.choice(list_quotes)[0]))



now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if day_of_week == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation"
                                f"\n\n{quote}")

# print(day_of_week)
#
# data_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(data_of_birth)



# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user = my_email,password = my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="rorojakung@gmail.com",
#         msg=f"Subject:Hello\n\n{random.choice(list_quotes)[0]}")
# connection.close()
