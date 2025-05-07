# Import Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os


# Set up chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4197024817&f_AL=true&geoId=90009496&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

action = webdriver.ActionChains(driver)

# Maximize window (optional)
driver.maximize_window()

load_dotenv()

# Close button
def close_button():
    dismiss_button = driver.find_element(By.CSS_SELECTOR, value='button[data-test-modal-close-btn]')
    dismiss_button.click()

time.sleep(4)
login_by_gmail = driver.find_element(By.CSS_SELECTOR, value='[data-modal=base-sign-in-modal]')
login_by_gmail.click()

email = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
email.click()
email.send_keys(os.environ['LINKEDIN_EMAIL'])

password = driver.find_element(By.ID, value="base-sign-in-modal_session_password")
password.click()
password.send_keys(os.environ['LINKEDIN_PASSWORD'], Keys.ENTER)

#If Captcha
input("Please complete the captcha and press Enter to continue...")

#For every div in job list
time.sleep(4)
listing = driver.find_elements(By.CSS_SELECTOR, value="li.scaffold-layout__list-item")
print(f"{len(listing)} job offers to apply for")

for job_offer in listing:
    try:
        job_offer.click()
        time.sleep(2)

        try:
            applied_status = driver.find_element(By.CSS_SELECTOR, value='.artdeco-inline-feedback--success')
            if 'Applied' in applied_status.text:
                print('You have already applied for this job')
                continue
        except NoSuchElementException:
            pass

        try:
            apply_button = driver.find_element(By.CSS_SELECTOR, value='.jobs-apply-button')
            apply_button.click()
            time.sleep(2)
            # Dismiss job offer with next steps needed
        except NoSuchElementException:
            continue

        try:
            next_step = driver.find_element(By.CSS_SELECTOR, value='button.artdeco-button--primary[aria-label]')
            # Fetch aria-label atribut
            button_label = next_step.get_attribute('aria-label')

            if button_label == "Submit application":
                print("Send application .... ")
                try:
                    phone_number = driver.find_element(By.CSS_SELECTOR, value='input[id*="phoneNumber-nationalNumber"]')
                    phone_number.clear()
                    phone_number.send_keys(os.environ['PHONE_NUMBER'])
                    next_step.click()
                    time.sleep(1)
                    try:
                        close_button()
                    except:
                        pass
                except NoSuchElementException:
                    continue
            # close if needed else steps
            elif button_label == 'Continue to next step':
                print('Offer need another steps i pass')
                try:
                    close_button()
                    discard_button = driver.find_element(By.CSS_SELECTOR, value='button[data-control-name="discard_application_confirm_btn"]')
                    discard_button.click()

                    close_left_button = driver.find_element(By.CSS_SELECTOR, value='div button.job-card-container__action')
                    close_left_button.click()
                    time.sleep(2)
                except:
                    pass

        except NoSuchElementException:
            continue
    except NoSuchElementException:
        print('Not found')
        continue

# driver.quit()





