# Automated Amazon Price Tracker

# Step 1: Updated Use BeautifulSoup to scrape the product price
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

# Step 3 : Add headers to your request
header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
        "Dnt": "1",
        "Priority": "u=1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Sec-Gpc": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url=live_url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

price = soup.find(name="span", class_="aok-offscreen").get_text()

# print(price)

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

# Step 2 : Email alert when the price below preset value

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100.00

if price_as_float < BUY_PRICE:
    message = f"Subject: Amazon Price Alert!\n\n{title} is now {price}.\n{live_url}.".encode("utf-8")

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ["EMAIL_ADDRESS"], password=os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=message,
        )


# Step 4 : Scrape the live Amazon site


