from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import requests
from time import sleep

GOOGLE_FORM = "YOUR_GOOGLE_FORM_LINK"

# -------------------- BeautifulSoup ------------------ #
ZILLOW_URL = "YOUR_ZILLOW_URL"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Accept-Language": "en-US,en;q=0.5"
}
response = requests.get(url=ZILLOW_URL, headers=HEADERS)
zillow_page = response.text

soup = BeautifulSoup(zillow_page, "lxml")

all_link_elements = soup.select(selector=".list-card-top a")
all_links = []
for link in all_link_elements:
    href = link.get("href")
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)


all_address_elements = soup.select(selector=".list-card-info address")
all_addresses = [address.text.split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    # Get the prices. Single and multiple listings have different tag & class structures
    try:
        # Price with only one listing
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        # Price with multiple listings
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)


# --------------- Selenium ------------ #

FIREFOX_DRIVER_PATH = "geckodriver-v0.29.0-win64/geckodriver.exe"
driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)

for i in range(len(all_links)):
    driver.get(url=GOOGLE_FORM)
    sleep(3)

    address = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address.send_keys(all_addresses[i])
    price = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price.send_keys(all_prices[i])

    property_link = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    property_link.send_keys(all_links[i])

    submit = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span")
    submit.click()
