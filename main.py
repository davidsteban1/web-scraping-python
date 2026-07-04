from scraper import scrape
from email_alert import alert

wanted_price = scrape()

if wanted_price is not None:
    print("Send email")
    alert(wanted_price)
else:
    print("Don't send any email")