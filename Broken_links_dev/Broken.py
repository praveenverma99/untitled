import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = r"C:\Users\prave\Downloads\chromedriver_win32(3)"

driver = webdriver.Chrome(PATH)
#driver.maximize_window()

links = driver.find_elements(By.CSS_SELECTOR, "a")
# traverse list
links_list = ["https://masys.dev/", "https://masys.dev/th_landing/", "https://masys.dev/auth/sign_in.php","https://masys.dev/auth/sign_up.php"]

for link in links_list:
    driver.get("Links_list")

#words= ["Apple", "Banana", "Car", "Dolphin" ]
#for word in words:
 #   print (word)
    # get_attribute() to get all href

   # print(links.get_attribute('href'))

    url = link.get_attribute('href')

    result = requests.head(url)

    if result.status_code != 200:
        print(url, result.status_code)
driver.quit()
