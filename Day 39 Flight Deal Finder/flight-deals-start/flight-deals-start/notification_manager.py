import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, origin_city_code, destination_city_code, from_time, to_time, cheapest_price):
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"Low price alert! Only £{cheapest_price} to fly from {origin_city_code} to {destination_city_code}, on {from_time} until {to_time}",
            from_="whatsapp:+14155238886",
            to="whatsapp:+6282320835440",
        )
        print("SUCCESS! Message has been sent")
        # pass

    # pass

