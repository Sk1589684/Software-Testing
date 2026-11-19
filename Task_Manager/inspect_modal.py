from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://taskmanagement.ai.studio/login")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    driver.get("https://taskmanagement.ai.studio/tasks")
    time.sleep(2)
    
    # Click Create Task
    create_btn = driver.find_element(By.XPATH, "//button[contains(., 'Create Task')]")
    create_btn.click()
    time.sleep(1)
    
    print("--- CREATE TASK MODAL ---")
    modal_inputs = driver.find_elements(By.XPATH, "//div[contains(@class, 'fixed') or contains(@class, 'modal')]//input | //form//input")
    for inp in modal_inputs:
        print(f"Modal Input: type={inp.get_attribute('type')}, name={inp.get_attribute('name')}, placeholder={inp.get_attribute('placeholder')}")
        
    modal_buttons = driver.find_elements(By.XPATH, "//div[contains(@class, 'fixed') or contains(@class, 'modal')]//button | //form//button")
    for btn in modal_buttons:
        txt = btn.text.strip().replace('\n', ' ')
        if txt:
            print(f"Modal Button: '{txt}'")
            
    textareas = driver.find_elements(By.TAG_NAME, "textarea")
    for ta in textareas:
        print(f"Textarea: placeholder={ta.get_attribute('placeholder')}")
        
finally:
    driver.quit()
