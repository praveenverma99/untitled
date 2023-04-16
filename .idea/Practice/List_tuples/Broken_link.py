from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

PATH = r"C:\Users\prave\Downloads\chromedriver_win32(3)"

driver = webdriver.Chrome(PATH)

# build a list of all url of masys.dev
# Create a Loop to iterate all the above url


driver.get("https://masys.dev/")

all_links = driver.find_elements(By.CSS_SELECTOR, "a")

for link in all_links:

    url = link.get_attribute('href')

    result = requests.head(url)

    if result.status_code != 200:
        print(url, result.status_code)