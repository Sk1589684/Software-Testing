
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException
)
from datetime import datetime
import time

# ==========================================
# TC_016 - CREATE TASK WITH VALID INFORMATION
# ==========================================
# IMPORTANT BUSINESS RULE:
# Task Title is a COMPULSORY (mandatory) field.
# Without a Task Title, a task CANNOT be created. The UI enforces
# HTML5 required validation, and submission is blocked if omitted.
# ==========================================

# ===== CHANGE HERE: LOGIN CREDENTIALS =====
EMAIL = "emp003@gmail.com"   # CHANGE HERE
PASSWORD = "Tempn0257d!"          # CHANGE HERE

# ===== CHANGE HERE: TASK DETAILS =====
# NOTE: TASK_TITLE is COMPULSORY. Do not leave empty.
TASK_TITLE = "Selenium Test Task " + datetime.now().strftime("%Y%m%d%H%M%S")
TASK_DESCRIPTION = "Task created using Selenium automation"

# Validation check: Ensure mandatory field is populated before running
if not TASK_TITLE or not TASK_TITLE.strip():
    raise ValueError("Validation Error: Task Title is COMPULSORY and cannot be empty! Task creation cannot proceed.")

LOGIN_URL = "https://taskmanagement.ai.studio/login"
TASKS_URL = "https://taskmanagement.ai.studio/tasks"

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)


# Helper function to click elements safely
def safe_click(locator):
    element = wait.until(
        EC.presence_of_element_located(locator)
    )

    # Scroll the element to the center of the screen
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        element
    )
    time.sleep(0.5)

    try:
        element.click()
    except (ElementClickInterceptedException, Exception):
        # Fallback to JavaScript click if intercepted by overlay or animation
        driver.execute_script("arguments[0].click();", element)


try:
    # STEP 1: Open login page
    driver.get(LOGIN_URL)
    print("Login page opened")

    # STEP 2: Clear prefilled credentials and enter credentials from code
    email_field = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[type='email']")
        )
    )
    # Clear pre-filled admin email using Ctrl+A + Backspace
    email_field.send_keys(Keys.CONTROL + "a")
    email_field.send_keys(Keys.BACKSPACE)
    time.sleep(0.3)
    email_field.send_keys(EMAIL)
    print(f"Cleared default and entered Email: {EMAIL}")

    password_field = driver.find_element(
        By.CSS_SELECTOR, "input[type='password']"
    )
    # Clear pre-filled admin password using Ctrl+A + Backspace
    password_field.send_keys(Keys.CONTROL + "a")
    password_field.send_keys(Keys.BACKSPACE)
    time.sleep(0.3)
    password_field.send_keys(PASSWORD)
    print("Cleared default and entered Password")

    # STEP 3: Submit login form
    time.sleep(0.5)
    password_field.send_keys(Keys.ENTER)

    wait.until(
        lambda d: "/login" not in d.current_url
    )
    print("Login successful - redirected to:", driver.current_url)

    # STEP 4: Navigate to Tasks page
    driver.get(TASKS_URL)

    wait.until(
        EC.presence_of_element_located(
            (By.TAG_NAME, "body")
        )
    )
    time.sleep(1)
    print("Tasks page opened")

    # STEP 5: Click Create Task button
    create_button = (
        By.XPATH,
        "//button[contains(., 'Create Task') or "
        "contains(., 'New Task') or "
        "contains(., 'Add Task')]"
    )

    safe_click(create_button)
    print("Create Task button clicked")
    time.sleep(1)

    # STEP 6: Enter compulsory field (Placeholder starts with "e.g.,")
    print("\nSTEP 6: Filling Compulsory Field (placeholder: 'e.g., Upgrade API Authentication Middleware & Tokens')")
    compulsory_title_field = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[placeholder*='e.g.,' i], "
                "input[placeholder*='Upgrade API' i], "
                "input[name='title']"
            )
        )
    )

    # Verify that this field is compulsory/mandatory in the DOM
    is_required = compulsory_title_field.get_attribute("required") is not None
    print(f" -> Field checked: Compulsory = {is_required} (Task cannot be created without filling this)")

    # Clear and enter the compulsory task title
    compulsory_title_field.click()
    compulsory_title_field.send_keys(Keys.CONTROL + "a")
    compulsory_title_field.send_keys(Keys.BACKSPACE)
    time.sleep(0.3)
    compulsory_title_field.send_keys(TASK_TITLE)
    print(f" -> Compulsory field filled with: '{TASK_TITLE}'")
    time.sleep(1)

    # STEP 7: Enter task description (Rich Text)
    print("\nSTEP 7: Entering Task Description")
    description_fields = driver.find_elements(
        By.CSS_SELECTOR,
        "textarea[name='description'], textarea"
    )

    if description_fields:
        description_fields[0].send_keys(TASK_DESCRIPTION)
        print(f" -> Description entered: '{TASK_DESCRIPTION}'")

    time.sleep(1)

    # STEP 8: Scroll down inside modal dialog after description is filled
    print("\nSTEP 8: Scrolling down inside modal dialog...")
    modal_containers = driver.find_elements(
        By.XPATH,
        "//div[contains(@class, 'overflow-y-auto')]"
    )
    if modal_containers:
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight;",
            modal_containers[0]
        )
    time.sleep(1)

    # STEP 9: Locate submit button, scroll into view, and click
    print("\nSTEP 9: Submitting task form ('Assign & Launch Task')...")
    submit_btn = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[contains(., 'Assign & Launch Task') or "
                "@type='submit']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        submit_btn
    )
    time.sleep(1)

    try:
        submit_btn.click()
    except Exception:
        driver.execute_script("arguments[0].click();", submit_btn)

    print(" -> 'Assign & Launch Task' button clicked")

    # Wait for the modal dialog to disappear (verifies submission succeeded)
    wait.until(
        EC.invisibility_of_element_located(
            (By.XPATH, "//button[contains(., 'Assign & Launch Task')]")
        )
    )
    print(" -> Task modal closed successfully - creation confirmed by UI")
    time.sleep(2)

    # STEP 10: Verify task creation in the dashboard / task list
    print("\nSTEP 10: Verifying task in Dashboard / Task list...")
    # Navigate to Tasks page to verify task appears in the list
    driver.get(TASKS_URL)
    time.sleep(2)

    wait.until(
        lambda d: len(d.find_elements(
            By.XPATH,
            f"//*[not(self::input) and not(self::textarea) and contains(., '{TASK_TITLE}')]"
        )) > 0
    )

    print("\n" + "=" * 70)
    print("TEST CASE TC_016: PASS")
    print("Task created successfully and verified in dashboard/tasks:", TASK_TITLE)
    print("=" * 70)

except Exception as error:
    print("\nTEST CASE TC_016: FAIL")
    print("Error:", str(error))

    driver.save_screenshot("TC_016_Failure.png")
    print("Screenshot saved: TC_016_Failure.png")

finally:
    time.sleep(3)
    driver.quit()
