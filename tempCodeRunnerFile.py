from scraper import scrape
from email import send_alert

wanted_price = scrape()
send_alert(wanted_price)