import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\prave\Downloads\chromedriver_win32(3)')

links_list = ["https://masys.dev/", "https://masys.dev/th_landing/", "https://masys.dev/auth/sign_in.php","https://masys.dev/auth/sign_up.php"]

for link in links_list:
 driver.get('links_list')
link = driver.find_elements_by_css_selector("a")
for link in links_list:
    r = requests.head(link.get_attribute('href'))
    print(link.get_attribute('href'), r.status_code)