A simple and automated Selenium-based tool designed to **test multiple username/password combinations** on a web login page and identify **working vs non-working credentials**.

This tool was built for **ethical security evaluation**, **internal audits**, and **testing account validity** for approved systems.

---

## 🚀 Features

- 🔄 Bulk login attempts using CSV / Excel credentials  
- 🧪 Detects valid vs invalid login attempts  
- ❌ Captures login errors using error message ID  
- 👤 Randomized user-agents (anti-bot detection)  
- 🕵️ Anti-automation techniques to avoid detection  
- 📝 Exports working accounts to `working_credentials.txt`  
- 🧘 Human-like delays + rate limiting to avoid blocking  
- 🌐 Works on Windows, Linux, and macOS  

Chrome must be installed on your system.
The script automatically installs the correct ChromeDriver.

---- Inside Creds_check.py 

PUT the URL of you login page you want to test.
Replace "your_login_page" in LOGIN_URL = "https://your_login_page/" with your actual URL.
Install dependencies:
---

Install dependencies:

```bash
pip install pandas selenium undetected-chromedriver openpyxl
pip install webdriver-manager






