import csv
from selenium import webdriver

def csv_url_reader(url_obj):
    reader = csv.DictReader(url_obj,delimitter = ',')
    for line in reader:
        url = line["URL"]
        title = line["Title"]

PATH = r"C:\Users\prave\Downloads\chromedriver_win32(3)"
driver = webdriver.Chrome(PATH)
driver.get(url)
assert title in driver.title
driver.quit()

if __name__ == "__main__"
    with open("URL.csv") url_obj:
        csv_url_reader(url_obj)