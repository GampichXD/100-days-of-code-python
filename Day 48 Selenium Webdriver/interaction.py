from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")

total_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')


print(total_articles.text)

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")

# all_portals.click()

search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
search.send_keys("Python", Keys.ENTER)

# driver.quit()