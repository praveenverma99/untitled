import requests

urls = ["https://masys.dev/", "https://masys.dev/th_landing/", "https://masys.dev/auth/client_sign_in.php",
        "https://masys.dev/auth/client_sign_up.php", "https://masys.dev/", "https://masys.dev/client/policy/about_us.php",
        "https://masys.dev/client/policy/faq.php", "https://masys.dev/client/policy/help.php", "https://masys.dev/auth/sign_up.php",
        "https://masys.dev/client/policy/privacy_policy.php", "https://masys.dev/client/policy/terms_of_service.php"]

for url in urls:
    response = requests.get(url)
    print(f'{url} - Status code: {response.status_code}')

