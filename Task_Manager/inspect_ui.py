from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://taskmanagement.ai.studio/login")
    time.sleep(2)
    
    print("--- LOGIN PAGE ELEMENTS ---")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for inp in inputs:
        print(f"Input: type={inp.get_attribute('type')}, name={inp.get_attribute('name')}, placeholder={inp.get_attribute('placeholder')}, value={inp.get_attribute('value')}")
        
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in buttons:
        print(f"Button: text='{btn.text}', type={btn.get_attribute('type')}, class={btn.get_attribute('class')[:40]}")

    # Now let's try logging in
    email_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    
    email_input.clear()
    email_input.send_keys("admin@company.com")
    password_input.clear()
    password_input.send_keys("Password123!")
    submit_btn.click()
    
    time.sleep(3)
    print("\n--- AFTER LOGIN ---")
    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)
    
    # Check elements on dashboard
    print("\nLinks:")
    for a in driver.find_elements(By.TAG_NAME, "a")[:10]:
        print("Link:", a.text, "href:", a.get_attribute("href"))
        
    # Check if there are tasks or buttons
    print("\nButtons after login:")
    for btn in driver.find_elements(By.TAG_NAME, "button")[:15]:
        print("Button:", btn.text.strip())

finally:
    driver.quit()
