from selenium import webdriver
import time

firefox_driver_path = "geckodriver-v0.29.0-win64/geckodriver.exe"
driver = webdriver.Firefox(executable_path=firefox_driver_path)

URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)

# Cookie
cookie = driver.find_element_by_id("cookie")

# Right Panel Buy Items
right_panel = driver.find_elements_by_css_selector("#store div")
panel_ids = [panel.get_attribute("id") for panel in right_panel]

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    # Every 5 secs
    if time.time() > timeout:
        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert all <b> texts to Integer Price
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = panel_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 10 seconds till next check
        timeout = time.time() + 10

    # Stop the bot after 5 mins and check the cookies per second count
    if time.time() > five_min:
        cookie_per_sec = driver.find_element_by_id("cps").text
        print(cookie_per_sec)
        break







