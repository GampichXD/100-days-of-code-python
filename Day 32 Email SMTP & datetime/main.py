##################### Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib
# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. 
MY_EMAIL = "yesorry32@gmail.com"
MY_PASSWORD = "sraf ocot mvis yosg"
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
now = dt.datetime.now()
today_day = now.day
today_month = now.month
today_tuple = (today_month, today_day)
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

# birthdays_dict = target.to_dict(orient="records")
# print(birthdays_dict)

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
target = pd.read_csv('birthdays.csv')

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in target.iterrows()}
if (today_month, today_day) in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'], msg=f"Subject:Happy Birthday!\n\n{contents}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



