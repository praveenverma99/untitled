import urllib.request
from urllib.error import HTTPError, URLError
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\prave\Downloads\chromedriver_win32(3)"
driver = webdriver.Chrome(chrome_driver_path)
homepage = "https://masys.dev/auth/client_sign_in.php"
url = ""
resp_code = 200

driver.maximize_window()
driver.get(homepage)
links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    url = link.get_attribute("href")
    print(url)

    if url is None or url == "":
        print("URL is either not configured for anchor tag or it is empty")
        continue

    if not url.startswith(homepage):
        print("URL belongs to another domain, skipping it.")
        continue

    try:
        conn = urllib.request.urlopen(url)
        resp_code = conn.getcode()
        if resp_code >= 400:
            print(url + " is a broken link")
        else:
            print(url + " is a valid link")
    except HTTPError as e:
        print(url + " is a broken link. Error code: " + str(e.code))
    except URLError as e:
        print(url + " is a broken link. Reason: " + str(e.reason))

driver.quit()
