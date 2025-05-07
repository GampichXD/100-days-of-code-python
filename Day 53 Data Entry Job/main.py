from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")

property_list = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

link_list = []
for item in property_list:
    a_tag = item.find(name="a", class_ = "StyledPropertyCardDataArea-anchor")
    link_list.append(a_tag.get("href"))

price_list = []
for item in property_list:
    price = item.find(name="span", class_ = "PropertyCardWrapper__StyledPriceLine").text
    temp_price = price.replace("+","/")
    price_list.append(temp_price.split("/")[0])

addr_list = []
for item in property_list:
    addr = item.find('address').text
    addr = addr.strip('\n,')
    addr = addr.strip()
    addr = addr.replace("|","")
    addr_list.append(addr) 


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://docs.google.com/forms/d/e/1FAIpQLSeIA1YS-UIZHyBJSiRnNbxK7cQy_gxdgJbd3blXQu3XK7p9Kw/viewform')
sleep(5)
for i in range(len(price_list)):
    addr_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")))
    addr_input.send_keys(addr_list[i])
    price_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")))
    price_input.send_keys(price_list[i])
    link_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")))
    link_input.send_keys(link_list[i])
    submit_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")))
    submit_button.click()

#clicking submit another response
submit_another_response = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")))
submit_another_response.click()
