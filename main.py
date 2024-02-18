import requests
from bs4 import BeautifulSoup
from pprint import pprint
import lxml
import smtplib
import os
from email.mime.text import MIMEText

MY_EMAIL = os.environ.get("MY_EMAIL", "Key does not exist")
PASSWORD = os.environ.get("PASSWORD", "Key does not exist")
URL = "https://www.amazon.ca/Instant-Pot-6QT-Duo-Plus/dp/B07W55DDFB/ref=sr_1_2?asc_campaign=25bbdcd06c32d477f7fa1c3e4a91b032&asc_source=01GTER6R4MWCHKTX3Z44AQDYRW&crid=1ZT6WPHCBW6RN&keywords=instant%2Bpot%2Bduo%2Bplus&qid=1708206406&sprefix=Instant%2Bpot%2Bduo%2Caps%2C80&sr=8-2&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fr-CA;q=0.8,fr;q=0.7,en-CA;q=0.6"
}

response = requests.get(URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, 'lxml')
a_price_whole_element = soup.select_one(selector="span .a-price-whole")
a_price_whole = float(a_price_whole_element.text)
a_price_fraction_element = soup.select_one(selector="span .a-price-fraction")
a_price_fraction = float(f"0.{a_price_fraction_element.text}")
price = a_price_whole + a_price_fraction


if price < 100:
    subject = "Subject:Amazon Price Alert!"
    body = f"Price: ${price}, {URL}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"{subject}\n\n{body}")
