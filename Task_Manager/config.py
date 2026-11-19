"""
Configuration and Test Environment Settings for Task Management Application
Target URL: https://taskmanagement.ai.studio/login
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ---------------------------------------------------------------------------
# Target Application URLs
# ---------------------------------------------------------------------------
BASE_URL = "https://taskmanagement.ai.studio"
LOGIN_URL = f"{BASE_URL}/login"
DASHBOARD_URL = f"{BASE_URL}/"
TASKS_URL = f"{BASE_URL}/tasks"
TEAM_URL = f"{BASE_URL}/team"
TODOS_URL = f"{BASE_URL}/todos"

# ---------------------------------------------------------------------------
# Test Credentials & Payloads
# ---------------------------------------------------------------------------
VALID_ADMIN = {
    "email": "admin@company.com",
    "password": "Password123!",
    "role": "ADMIN",
    "name": "Admin"
}

VALID_EMPLOYEE = {
    "email": "emp@company.com",
    "password": "Password123!",
    "role": "EXECUTIVE",
    "name": "Employee"
}

INVALID_ACCOUNTS = {
    "wrong_password": {
        "email": "admin@company.com",
        "password": "WrongPassword!999"
    },
    "unregistered": {
        "email": "nonexistent_user_999@company.com",
        "password": "Password123!"
    },
    "malformed_email": {
        "email": "not-an-email-address",
        "password": "Password123!"
    }
}

SECURITY_PAYLOADS = {
    "sql_injection": "' OR '1'='1' --",
    "xss_script": "<script>alert('XSS_TEST')</script>",
    "long_string": "TaskAutomationTest_" + ("A" * 320)
}

# ---------------------------------------------------------------------------
# Path & Directory Setup
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

DEFAULT_TIMEOUT = 12

# ---------------------------------------------------------------------------
# WebDriver Factory
# ---------------------------------------------------------------------------
def get_driver(headless: bool = True):
    """
    Initializes and returns a configured Chrome WebDriver instance.
    :param headless: If True, runs Chrome in headless mode. Set False to see the browser.
    """
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Mask automation flags to prevent false-positive blocks
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(2)
    return driver
