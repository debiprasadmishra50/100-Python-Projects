from selenium import webdriver
import time

FIREFOX_DRIVER_PATH = "geckodriver-v0.29.0-win64/geckodriver.exe"

try:
    with open("data.txt", mode="r") as file:
        data = file.readlines()
        TWITTER_EMAIL = data[0]
        TWITTER_PASSWORD = data[1]
        PROMISED_DOWN = data[2]
        PROMISED_UP = data[3]
except FileNotFoundError:
    with open("data.txt", mode="w") as file:
        TWITTER_EMAIL = input("Enter your Twitter ID: ")
        TWITTER_PASSWORD = input("Enter your Twitter Password: ")
        PROMISED_DOWN = input("Enter your ISP's promised Download speed: ")
        PROMISED_UP = input("Enter your ISP's promised Upload Speed: ")
        file.write(f"{TWITTER_EMAIL}\n{TWITTER_PASSWORD}\n{PROMISED_DOWN}\n{PROMISED_UP}")
    with open("data.txt", mode="r") as file:
        data = file.readlines()
        TWITTER_EMAIL = data[0]
        TWITTER_PASSWORD = data[1]
        PROMISED_DOWN = data[2]
        PROMISED_UP = data[3]


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Firefox(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # Start test
        self.driver.get("https://www.speedtest.net")
        time.sleep(5)
        start_test = self.driver.find_element_by_css_selector(".start-button a .start-text")
        start_test.click()

        print("Logging Test Status...")
        in_progress = True
        while in_progress:
            # Get the up and down speed
            progress = self.driver.find_element_by_class_name("overall-progress").text
            if progress.startswith("Your speed test has completed"):
                self.down = float(self.driver.find_element_by_class_name("download-speed").text)
                self.up = float(self.driver.find_element_by_class_name("upload-speed").text)
                print(f"Download Speed: {self.down}")
                print(f"Upload Speed: {self.up}")
                in_progress = False
            else:
                print(f"\r{progress}...")
                time.sleep(5)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(5)
        twitter_log_in = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]")
        twitter_log_in.click()

        input_field = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        input_field.send_keys(TWITTER_EMAIL)

        password = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
        password.send_keys(TWITTER_PASSWORD)

        time.sleep(1)
        login = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")
        login.click()

        time.sleep(5)

        tweet_compose = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div")
        tweet = f"Hey Internet Provider, why is my Internet speed {self.down}down/{self.up}up " \
                f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)

        time.sleep(2)

        tweet_upload = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]")
        tweet_upload.click()

        time.sleep(3)
        print("Tweet Sent...")


bot = InternetSpeedTwitterBot(driver_path=FIREFOX_DRIVER_PATH)
bot.get_internet_speed()
if int(bot.down) < int(PROMISED_DOWN) or int(bot.up) < int(PROMISED_UP):
    print("Sending Tweet...\n")
    bot.tweet_at_provider()
else:
    print("\nYou've perfect Internet Connection...")
