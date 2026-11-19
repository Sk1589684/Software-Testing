import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

try:
    driver = webdriver.Chrome(options=options)
    driver.get("https://taskmanagement.ai.studio/login")
    print("Page title:", driver.title)
    driver.quit()
    print("SUCCESS")
except Exception as e:
    print("Error:", e)
