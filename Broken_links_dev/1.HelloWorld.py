from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import webbrowser



# build a list of all url of masys.dev
# Create a Loop to iterate all the above url

urls = ["https://masys.dev/", "https://masys.dev/th_landing/", "https://masys.dev/auth/client_sign_in.php",
        "https://masys.dev/auth/client_sign_up.php", "https://masys.dev/", "https://masys.dev/client/policy/about_us.php",
        "https://masys.dev/client/policy/faq.php", "https://masys.dev/client/policy/help.php", "https://masys.dev/auth/sign_up.php",
        "https://masys.dev/client/policy/privacy_policy.php", "https://masys.dev/client/policy/terms_of_service.php"]

for url in urls:
   # webbrowser.open(url)

    PATH = r"C:\Users\prave\Downloads\chromedriver_win32(3)"

driver = webdriver.Chrome(PATH)

driver.get("urls")

#all_links = driver.find_elements(By.CSS_SELECTOR, "a")

#for link in all_links:

 #   website = link.get_attribute('href')

  #  result = requests.head(url)
response = requests.get(url)
print(f'{url} - Status code: {response.status_code}')
