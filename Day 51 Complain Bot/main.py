from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os
from dotenv import load_dotenv
load_dotenv()

twitter_url = os.environ['TWITTER_URL']

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(60)
        self.down = float(self.driver.find_element(By.CSS_SELECTOR, '.download-speed').text)
        self.up = float(self.driver.find_element(By.CSS_SELECTOR,'.upload-speed').text)
        print(self.down, self.up)
        

    def tweet_at_provider(self):
        self.driver.get(twitter_url)

        #login_to_twitter
        time.sleep(3)
        email_box = self.driver.find_element(By.NAME, 'text')
        email_box.send_keys(os.environ['TWITTER_EMAIL'])
        email_box.send_keys(Keys.ENTER)

        time.sleep(5)

        try: # susbicious login triggered
            user_box = self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='ocfEnterTextTextInput']")
            user_box.send_keys(os.environ['TWITTER_USER'])
            user_box.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print("No suspicious login detected")

        time.sleep(5)
        password_box = self.driver.find_element(By.NAME, 'password')
        password_box.send_keys(os.environ['TWITTER_PASSWORD'])
        password_box.send_keys(Keys.ENTER)

        time.sleep(5)
        # send tweet
        tweet_box = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_box.send_keys(f"Hey @MetroPCS why is my internet speed {self.up} up and {self.down} down")
        send_tweet = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        send_tweet.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < float(os.environ['PROMISED_DOWN']) or bot.up < float(os.environ['PROMISED_UP']):
    time.sleep(3)
    bot.tweet_at_provider()
else:
    print(f'promised speed is {os.environ['PROMISED_UP']} up/ {os.environ['PROMISED_DOWN']} down and your speed is {bot.up} up/ {bot.down} down')
