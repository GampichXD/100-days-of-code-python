from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    # Wait for the language selection popup to appear and select English
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN"))
    ).click()

    # Wait for the cookie button to be clickable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "bigCookie"))
    )

    # Set timers
    timeout = time.time() + 5
    five_min = time.time() + 60 * 5

    while True:
        # Re-fetch the cookie button to avoid staleness
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()

        # Every 5 seconds, check for upgrades
        if time.time() > timeout:
            # Re-fetch all prices and store items to avoid staleness
            all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
            item_prices = []
            items = driver.find_elements(By.CSS_SELECTOR, "#store div")
            item_ids = [item.get_attribute("id") for item in items]

            for price in all_prices:
                price_text = price.text
                if price_text != "" and "-" in price_text:  # Ensure valid price format
                    cost = int(price_text.split("-")[1].replace(",", "").strip())
                    item_prices.append(cost)

            # Map prices to item IDs
            upgrades = {}
            for i in range(len(item_prices)):
                upgrades[item_prices[i]] = item_ids[i]

            # Get current cookie count
            money_element = driver.find_element(By.ID, "money").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

            # Find affordable upgrades
            affordable_upgrades = {}
            for cost, item_id in upgrades.items():
                if cookie_count >= cost:
                    affordable_upgrades[cost] = item_id

            # Purchase the most expensive affordable upgrade
            if affordable_upgrades:
                highest_price = max(affordable_upgrades)
                to_purchase_id = affordable_upgrades[highest_price]
                driver.find_element(By.ID, to_purchase_id).click()
                print(f"Purchased upgrade: {to_purchase_id}")

            # Reset timeout
            timeout = time.time() + 5

        # After 5 minutes, print cookies per second and exit
        if time.time() > five_min:
            cps = driver.find_element(By.ID, "cps").text
            print(f"Cookies per second: {cps}")
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Optionally close the browser
    # driver.quit()
    pass