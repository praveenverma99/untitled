import requests
from selenium import webdriver

# Define the list of URLs to open
urls = ["https://masys.dev/", "https://masys.dev/th_landing/", "https://masys.dev/auth/client_sign_in.php",
        "https://masys.dev/auth/client_sign_up.php", "https://masys.dev/", "https://masys.dev/client/policy/about_us.php",
        "https://masys.dev/client/policy/faq.php", "https://masys.dev/client/policy/help.php", "https://masys.dev/auth/sign_up.php",
        "https://masys.dev/client/policy/privacy_policy.php", "https://masys.dev/client/policy/terms_of_service.php"]


# Open the first URL in the list
driver = webdriver.Chrome()
driver.get(urls[0])

# Loop through the remaining URLs in the list
for url in urls[1:]:
    # Open the URL in the same tab
    driver.execute_script(f"window.location.href='{url}'")

    # Retrieve the URL and HTTP status code
    current_url = driver.current_url
    status_code = requests.get(current_url).status_code

    # Print the URL and HTTP status code
    print(f"URL: {current_url}\nStatus Code: {status_code}\n")
