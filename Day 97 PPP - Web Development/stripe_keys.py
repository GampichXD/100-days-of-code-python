import os
import stripe
from dotenv import load_dotenv
load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

YOUR_DOMAIN = 'http://localhost:5000'
