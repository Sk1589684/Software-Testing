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
    
    # Login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    
    # Go to /tasks
    driver.get("https://taskmanagement.ai.studio/tasks")
    time.sleep(2)
    
    print("--- /tasks PAGE ---")
    print("URL:", driver.current_url)
    
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for inp in inputs:
        print(f"Task Input: type={inp.get_attribute('type')}, placeholder={inp.get_attribute('placeholder')}")
        
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in buttons:
        txt = btn.text.strip().replace('\n', ' ')
        if txt:
            print(f"Task Button: '{txt}'")
            
    # Check selects / dropdowns
    selects = driver.find_elements(By.TAG_NAME, "select")
    for s in selects:
        print(f"Select: name={s.get_attribute('name')}, id={s.get_attribute('id')}")

finally:
    driver.quit()
