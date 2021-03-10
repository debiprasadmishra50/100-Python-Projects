from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

SIMILAR_ACCOUNT = input("Enter the account name from which you want to follow it's followers"
                        "(for example: 'chefsteps'): \n")
try:
    with open("data.txt", mode="r") as file:
        data = file.readlines()
        INSTAGRAM_USERNAME = data[0]
        INSTAGRAM_PASSWORD = data[1]
except FileNotFoundError:
    with open("data.txt", mode="w") as file:
        INSTAGRAM_USERNAME = input("\nEnter your Instagram ID: ")
        INSTAGRAM_PASSWORD = input("Enter your Instagram Password: ")
        file.write(f"{INSTAGRAM_USERNAME}\n{INSTAGRAM_PASSWORD}")
    with open("data.txt", mode="r") as file:
        data = file.readlines()
        INSTAGRAM_USERNAME = data[0]
        INSTAGRAM_PASSWORD = data[1]


FIREFOX_DRIVER_PATH = "geckodriver-v0.29.0-win64/geckodriver.exe"
URL = "https://www.instagram.com"

class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Firefox(executable_path=driver_path)

    def login(self):
        self.driver.get(f"{URL}/accounts/login/")
        sleep(5)
        username = self.driver.find_element_by_name("username")
        username.send_keys(INSTAGRAM_USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(INSTAGRAM_PASSWORD)
        sleep(1)
        try:
            login = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button")
        except NoSuchElementException:
            login = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
            login.click()
        else:
            login.click()

    def find_followers(self):
        self.driver.get(f"{URL}/{SIMILAR_ACCOUNT}")
        sleep(3)
        followers = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        sleep(2)

        follwer_list = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        for i in range(10):
            # Scroll inside a div popup
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follwer_list)
            sleep(2)

    def follow(self):
        follow_button = self.driver.find_elements_by_css_selector("li button")
        for button in follow_button:
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
                cancel_button.click()
                sleep(1)
            else:
                sleep(1)


insta_follower = InstaFollower(driver_path=FIREFOX_DRIVER_PATH)
insta_follower.login()
sleep(2)
insta_follower.find_followers()
sleep(2)
insta_follower.follow()
