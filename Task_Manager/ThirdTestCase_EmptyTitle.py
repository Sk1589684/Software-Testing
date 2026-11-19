"""
=============================================================================
TC_017 - CREATE TASK WITHOUT TITLE (VALIDATION NEGATIVE TEST)
=============================================================================
Test Objective:
Verify that 'Task Title' is COMPULSORY (mandatory).
Without a title, task creation MUST be blocked and the form must not submit.
=============================================================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

EMAIL = "emp003@gmail.com"
PASSWORD = "Tempn0257d!"

LOGIN_URL = "https://taskmanagement.ai.studio/login"
TASKS_URL = "https://taskmanagement.ai.studio/tasks"

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

def safe_click(locator):
    element = wait.until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.5)
    try:
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)

try:
    print("=" * 75)
    print("RUNNING TC_017: COMPULSORY TASK TITLE VALIDATION TEST")
    print("=" * 75)

    # STEP 1: Open login page
    driver.get(LOGIN_URL)
    print("Step 1: Login page opened")

    # STEP 2: Clear prefilled credentials and login
    email_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    email_field.send_keys(Keys.CONTROL + "a")
    email_field.send_keys(Keys.BACKSPACE)
    email_field.send_keys(EMAIL)

    password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_field.send_keys(Keys.CONTROL + "a")
    password_field.send_keys(Keys.BACKSPACE)
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.ENTER)

    wait.until(lambda d: "/login" not in d.current_url)
    print(f"Step 2: Logged in successfully as {EMAIL}")

    # STEP 3: Navigate to Tasks page
    driver.get(TASKS_URL)
    time.sleep(1.5)
    print("Step 3: Tasks page loaded")

    # STEP 4: Click Create Task button
    create_button = (By.XPATH, "//button[contains(., 'Create Task')]")
    safe_click(create_button)
    print("Step 4: Create Task modal opened")
    time.sleep(1)

    # STEP 5: Verify Title input is marked as compulsory (HTML required attribute)
    title_field = wait.until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR,
            "input[placeholder*='e.g.,' i], input[placeholder*='Upgrade API' i]"
        ))
    )
    is_required = title_field.get_attribute("required") is not None
    print(f"Step 5: Verified Title field compulsory constraint: required={is_required}")

    # Explicitly clear Title field so it is EMPTY
    title_field.send_keys(Keys.CONTROL + "a")
    title_field.send_keys(Keys.BACKSPACE)
    print("        Task Title left EMPTY intentionally to test validation.")

    # Fill optional description
    description_fields = driver.find_elements(By.TAG_NAME, "textarea")
    if description_fields:
        description_fields[0].send_keys("Attempting to create task without mandatory title.")

    # STEP 6: Scroll down inside modal
    print("Step 6: Scrolling down to submit button...")
    modal_containers = driver.find_elements(By.XPATH, "//div[contains(@class, 'overflow-y-auto')]")
    if modal_containers:
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", modal_containers[0])
    time.sleep(1)

    # STEP 7: Attempt to click 'Assign & Launch Task' without Title
    submit_btn = wait.until(
        EC.presence_of_element_located((
            By.XPATH,
            "//button[contains(., 'Assign & Launch Task') or @type='submit']"
        ))
    )
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_btn)
    time.sleep(0.5)

    try:
        submit_btn.click()
    except Exception:
        driver.execute_script("arguments[0].click();", submit_btn)

    print("Step 7: Clicked 'Assign & Launch Task' with empty title.")
    time.sleep(2)

    # STEP 8: Verify that task creation was BLOCKED (Modal must remain open)
    modal_still_open = len(driver.find_elements(By.XPATH, "//button[contains(., 'Assign & Launch Task')]")) > 0

    if modal_still_open:
        print("\n" + "=" * 75)
        print("TEST CASE TC_017: PASS")
        print("CONFIRMED: Task Title is COMPULSORY. The application blocked task creation")
        print("and the modal remained open because the mandatory title was missing.")
        print("=" * 75)
    else:
        print("\n" + "=" * 75)
        print("TEST CASE TC_017: FAIL")
        print("Task was created without a mandatory title (validation bypassed).")
        print("=" * 75)

    # Close modal cleanly
    cancel_btn = driver.find_elements(By.XPATH, "//button[contains(., 'Cancel')]")
    if cancel_btn:
        cancel_btn[0].click()

except Exception as e:
    print("\nTEST CASE TC_017: ERROR:", e)
finally:
    time.sleep(3)
    driver.quit()
