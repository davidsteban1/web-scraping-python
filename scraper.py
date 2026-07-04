import requests
from bs4 import BeautifulSoup

def scrape():
    
    url = "https://www.euronics.lv/en/it/desktops/pc-components/mz-v9p1t0cw/samsung-990-pro-with-heatsink-1-tb-pcie-4-0-nvme-m-2-black-ssd"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    ssd = soup.find("div", class_="container product-desc m-t-16")
    price = ssd.get("data-product-price")
    wanted_price = float(price)
    if wanted_price < 300:
        return wanted_price


