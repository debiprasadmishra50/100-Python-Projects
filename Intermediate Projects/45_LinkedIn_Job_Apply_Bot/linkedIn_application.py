from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

firefox_driver_path = "geckodriver-v0.29.0-win64/geckodriver.exe"
driver = webdriver.Firefox(executable_path=firefox_driver_path)

try:
    with open("data.txt", mode="r") as file:
        data = file.readlines()
        ID = data[0]
        PASSWORD = data[1]
        PHONE = data[2]
except FileNotFoundError:
    with open("data.txt", mode="w") as file:
        ID = input("Please enter your LinkedIn ID: ")
        PASSWORD = input("Please enter your LinkedIn Password: ")
        PHONE = input("Please enter your Phone No: ")
        file.write(f"{ID}\n{PASSWORD}\n{PHONE}")
    with open("data.txt", mode="r") as file:
        data = file.readlines()
        ID = data[0]
        PASSWORD = data[1]
        PHONE = data[2]


URL = input("Enter the job search URL:\nFor example:\n\thttps://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0\n\tURL: ")

driver.get(url=URL)

time.sleep(2)
sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys(ID)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
sign_in_button = driver.find_element_by_css_selector(".login__form_action_container button")
sign_in_button.click()

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()