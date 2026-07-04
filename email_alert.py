import resend
import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("API_KEY", "")
email = os.getenv("EMAIL", "")

def alert(wanted_price):
    
    resend.api_key = secret_key
    
    r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": email,
        "subject": "SSD PRICE ALERT",
        "html": f" I have found the desirable {wanted_price} price for your SDD"
    })