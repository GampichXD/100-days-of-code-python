from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")

site = "https://tinder.com/app/recs"
load_dotenv()
driver = webdriver.Chrome(options=chrome_options)
driver.get(site)

time.sleep(3)

accept_ck_button = '//*[@id="q1528582757"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]'

# Get Cookie to click on
cookie = driver.find_element(By.XPATH, accept_ck_button)
cookie.click()

time.sleep(3)
login_button = '//*[@id="q1528582757"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]'
login = driver.find_element(By.XPATH, login_button)
login.click()

time.sleep(3)
fb_login_button = '//*[@id="q-199798319"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]'
fb_login = driver.find_element(By.XPATH, fb_login_button)
fb_login.click()

time.sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

FB_EMAIL = os.environ['FB_EMAIL']
FB_PASSWORD = os.environ['FB_PASSWORD']
PHONE_NUMBER = os.environ['PHONE_NUMBER']

# Login and Hit Enter
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Manually close the FB Window since the continue Button is encrypted
input("Press Enter after closing the FB Window")
time.sleep(3)

# Switch back to the main window
driver.switch_to.window(base_window)
print(driver.title)

# Get phone number
need_number = input("Do you need to enter a phone number? (y/n): ")
if need_number.lower() == 'y':
    phone_path = '//*[@id="phone_number"]'
    phone_number = driver.find_element(By.XPATH, phone_path)
    phone_number.send_keys(PHONE_NUMBER)
    phone_number.send_keys(Keys.ENTER)
input("Press Enter after entering the phone number")



# Tinder Setup 
time.sleep(10)
like_button = driver.find_element(By.CSS_SELECTOR, 'button.Bgc\\(\\$c-ds-background-gamepad-sparks-like-default\\)')
like_button.click()

time.sleep(5)
nope_button = driver.find_element(By.CSS_SELECTOR, 'button.Bgc\\(\\$c-ds-background-gamepad-sparks-nope-default\\)')
nope_button.click()

# Tinder free tier only allows 100 swipes a day, so we need to keep track of the number of swipes
# for n in range(0, 100):
#     action = ActionChains(driver)
#     action.send_keys(Keys.ARROW_RIGHT)
#     action.perform()
#     time.sleep(2)

#     driver.quit()

#     print("Yes, you did it!")

# Start swiping: 50 "Like" and 50 "Nope"
like_count = 0
nope_count = 0
max_swipes = 50

while like_count < max_swipes or nope_count < max_swipes:
    try:
        # Swipe "Like"
        if like_count < max_swipes:
            like_button = driver.find_element(By.CSS_SELECTOR, 'button.Bgc\\(\\$c-ds-background-gamepad-sparks-like-default\\)')
            like_button.click()
            like_count += 1
            print(f"Swiped Like ({like_count}/50)")
            time.sleep(random.uniform(1, 3))  # Add random delay

        # Swipe "Nope"
        if nope_count < max_swipes:
            nope_button = driver.find_element(By.CSS_SELECTOR, 'button.Bgc\\(\\$c-ds-background-gamepad-sparks-nope-default\\)')
            nope_button.click()
            nope_count += 1
            print(f"Swiped Nope ({nope_count}/50)")
            time.sleep(random.uniform(1, 3))  # Add random delay

    except Exception as e:
        print(f"Error during swipe: {e}")
        break

# Quit the browser after completing 50-50 swipes
driver.quit()
print("Completed 50 Like and 50 Nope swipes!")






