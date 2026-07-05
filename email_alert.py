import resend
import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("API_KEY", "")
email = os.getenv("EMAIL", "")

def alert(wanted_price):
    resend.api_key = secret_key
    
    with open("template.html", "r", encoding="utf-8") as file:
        html_template = file.read()
    
    html_content = html_template.format(wanted_price=wanted_price)

    r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": email,
        "subject": f"🚨 Price Alert: Target Hardware dropped to {wanted_price}€!",
        "html": html_content
    })