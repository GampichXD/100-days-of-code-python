from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()

class InstaFollower:
    def __init__(self):
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_experimental_option('detach', True)
                self.driver = webdriver.Chrome(options=chrome_options)
                self.driver.get(f'https://www.instagram.com/{os.environ['SIMILIAR_ACCOUNT']}/')
                self.count = 0

    def login(self):
            url = "https://www.instagram.com/accounts/login/"
            self.driver.get(url)
            time.sleep(4.2)

            # Check if the cookie warning is present on the page
            decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
            cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
            if cookie_warning:
                    # Dismiss the cookie warning by clicking the button
                    cookie_warning[0].click()

            username = self.driver.find_element(By.NAME, value='username')
            password = self.driver.find_element(By.NAME, value='password')

            username.send_keys(os.environ['USERNAME_INST'])
            password.send_keys(os.environ['PASSWORD'])

            time.sleep(2.1)
            password.send_keys(Keys.ENTER)

            input("Press Enter if authentication code is clear : ")

            time.sleep(4.3)
            #Click "Not now" and ignore Save-login info prompt
            save_login_prompt = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Not now')]")
            if save_login_prompt:
                    save_login_prompt.click()

            time.sleep(3.7)
            #Click "not now" on notification prompt
            notification_prompt = self.driver.find_element(By.XPATH, value="// button[contains(text(), 'Not Now')]")
            if notification_prompt:
                    notification_prompt.click()
    
    def find_followers(self):
            
            try:
                    self.driver.get(f'https://www.instagram.com/{os.environ["SIMILIAR_ACCOUNT"]}/')
                    time.sleep(3)

                    followers_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]"))
                )
                    followers_button.click()
                    main_window = self.driver.current_window_handle
                    for window in self.driver.window_handles:
                            if window != main_window:
                                    self.driver.switch_to.window(window)
                                    break
                    time.sleep(9)

                    modal_xpath = "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
                    modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
                    for i in range(5):
                            
                            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                            time.sleep(2)
            except Exception as e:
                    print(f"An error occurred: {e}")
    
    def follow(self):
            follower_list = self.driver.find_elements(By.XPATH, value='//div[text()="Follow"]')
            for button in follower_list:
                    try:
                            button.click()
                            time.sleep(4)
                    except ElementClickInterceptedException:
                            pass
    
bot = InstaFollower()
bot.login()
time.sleep(6)
bot.find_followers()
time.sleep(2)
bot.follow()