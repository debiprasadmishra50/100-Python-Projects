from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

try:
    with open("data.txt", mode="r") as file:
        data = file.readlines()
        FB_ID = data[0]
        FB_PASS = data[1]
except FileNotFoundError:
    with open("data.txt", mode="w") as file:
        FB_ID = input("Enter your Facebook User ID: ")
        FB_PASS = input("Enter your Facebook Password: ")
        file.write(f"{FB_ID}\n{FB_PASS}")
    with open("data.txt", mode="r") as file:
        data = file.readlines()
        FB_ID = data[0]
        FB_PASS = data[1]


profile = webdriver.FirefoxProfile()
profile.set_preference("geo.prompt.testing", True)
profile.set_preference("geo.prompt.testing.allow", True)
profile.set_preference("geo.provider.testing", True)
profile.set_preference('geo.wifi.uri',
        'data:application/json,{"location": {"lat": 40.7590, "lng": -73.9845}, "accuracy": 27000.0}')


firefox_driver_path = "geckodriver-v0.29.0-win64/geckodriver.exe"
driver = webdriver.Firefox(executable_path=firefox_driver_path, firefox_profile=profile)

URL = "https://tinder.com/"
driver.get(url=URL)

time.sleep(5)
log_in = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button")
log_in.click()

time.sleep(2)
try:
    fb_login = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
except NoSuchElementException:
    more_options = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/button")
    more_options.click()
    fb_login = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
    fb_login.click()
else:
    fb_login.click()


time.sleep(10)
tinder_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

email = driver.find_element_by_xpath("//*[@id='email']")
email.send_keys(FB_ID)
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(FB_PASS)
fb_page_login = driver.find_element_by_id("loginbutton")
fb_page_login.click()

time.sleep(5)
driver.switch_to.window(tinder_window)

time.sleep(2)
cookie_accept = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/button")
cookie_accept.click()

time.sleep(2)
allow_location = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]")
allow_location.click()

time.sleep(2)
not_interested = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[2]")
not_interested.click()


for click in range(100):
    time.sleep(2)
    try:
        right_swipe = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button")
        right_swipe.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

        try:
            upgrade_popup = driver.find_element_by_xpath("/html/body/div[2]/div/div/button[2]")
            upgrade_popup.click()
        except NoSuchElementException:
            time.sleep(2)










