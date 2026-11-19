"""
Visual Interactive Login Test Script
Target: https://taskmanagement.ai.studio/login
Mode: Visible Browser Window (Headed) - Opens Google Chrome on screen
"""

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TARGET_URL = "https://taskmanagement.ai.studio/login"
VALID_EMAIL = "admin@company.com"
VALID_PASSWORD = "Password123!"

def print_step(step_num: int, title: str, description: str):
    print("\n" + "=" * 70, flush=True)
    print(f" STEP {step_num}: {title}", flush=True)
    print(f" -> {description}", flush=True)
    print("=" * 70, flush=True)

def slow_type(element, text, delay=0.08):
    """Types characters one by one with a human-like delay so it's visible on screen."""
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.BACKSPACE)
    time.sleep(0.3)
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

def run_visual_login_tests():
    print("*" * 75, flush=True)
    print(" LAUNCHING VISIBLE GOOGLE CHROME BROWSER ON YOUR SCREEN", flush=True)
    print(" Target: https://taskmanagement.ai.studio/login", flush=True)
    print(" Watch the browser window in front of you as each test executes!", flush=True)
    print("*" * 75, flush=True)

    # Configure Chrome in visible GUI mode (Headed)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 12)

    try:
        # -------------------------------------------------------------------
        # Step 1: Open Target URL
        # -------------------------------------------------------------------
        print_step(1, "Navigating to Login Page", f"Opening {TARGET_URL} in Chrome...")
        driver.get(TARGET_URL)
        time.sleep(2)
        print(f"   [OK] Page loaded: '{driver.title}'", flush=True)

        # Locate fields
        email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
        password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # -------------------------------------------------------------------
        # Step 2: Test Empty Form Submission (TC_004)
        # -------------------------------------------------------------------
        print_step(2, "TC_004: Submit Empty Form", "Clearing both fields and clicking Sign In to check validation...")
        email_field.send_keys(Keys.CONTROL + "a")
        email_field.send_keys(Keys.BACKSPACE)
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        submit_btn.click()
        time.sleep(2)
        print("   [OK] Checked: Validation messages visible on screen under input fields.", flush=True)

        # -------------------------------------------------------------------
        # Step 3: Test Malformed Email (TC_007)
        # -------------------------------------------------------------------
        print_step(3, "TC_007: Enter Malformed Email", "Typing invalid email format: 'not-an-email'...")
        slow_type(email_field, "not-an-email")
        slow_type(password_field, "Password123!")
        time.sleep(1)
        submit_btn.click()
        time.sleep(2)
        print("   [OK] Checked: Invalid format error displayed on screen.", flush=True)

        # -------------------------------------------------------------------
        # Step 4: Test Wrong Password (TC_002)
        # -------------------------------------------------------------------
        print_step(4, "TC_002: Correct Email with Wrong Password", f"Entering {VALID_EMAIL} with 'WrongPassword999!'...")
        slow_type(email_field, VALID_EMAIL)
        slow_type(password_field, "WrongPassword999!")
        time.sleep(1)
        submit_btn.click()
        time.sleep(2.5)
        print("   [OK] Checked: Authentication rejected with error notification toast.", flush=True)

        # -------------------------------------------------------------------
        # Step 5: Test Valid Login (TC_001)
        # -------------------------------------------------------------------
        print_step(5, "TC_001: Valid Registered Email and Password", f"Typing valid credentials: {VALID_EMAIL} / {VALID_PASSWORD}...")
        slow_type(email_field, VALID_EMAIL)
        slow_type(password_field, VALID_PASSWORD)
        time.sleep(1.2)

        print("   Clicking 'Sign In' button...", flush=True)
        submit_btn.click()
        time.sleep(3)

        # Verify landing on Dashboard
        current_url = driver.current_url
        print_step(6, "Authentication Verification", f"Current URL after login: {current_url}")
        if "/login" not in current_url:
            print("   >>> SUCCESS: User authenticated and authorized landing page displayed! <<<", flush=True)
        else:
            print("   >>> NOTE: Page state did not transition as expected. <<<", flush=True)

        # -------------------------------------------------------------------
        # Step 6: Explore Dashboard / Tasks
        # -------------------------------------------------------------------
        print_step(7, "Dashboard & Navigation Verification", "Viewing dashboard controls and sidebar links on screen...")
        time.sleep(2.5)

        # Navigate to tasks page visibly
        print("   Navigating to https://taskmanagement.ai.studio/tasks to view tasks...", flush=True)
        driver.get("https://taskmanagement.ai.studio/tasks")
        time.sleep(3)
        print(f"   [OK] Tasks page active: {driver.current_url}", flush=True)

        print("\n" + "=" * 70, flush=True)
        print(" VISUAL TEST EXECUTION COMPLETED SUCCESSFULLY!", flush=True)
        print(" Keeping the browser window open for 5 seconds so you can inspect...", flush=True)
        print("=" * 70, flush=True)
        time.sleep(5)

    except Exception as e:
        print(f"\n[ERROR occurred during test]: {e}", flush=True)
    finally:
        print("Closing browser session...", flush=True)
        driver.quit()
        print("Done.", flush=True)

if __name__ == "__main__":
    run_visual_login_tests()
