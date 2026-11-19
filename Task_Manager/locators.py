"""
Centralized UI Locators for Task Management Application
Target: https://taskmanagement.ai.studio
"""

from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    DEMO_ADMIN_BUTTON = (By.XPATH, "//button[contains(., 'Admin')]")
    DEMO_EMPLOYEE_BUTTON = (By.XPATH, "//button[contains(., 'Employee')]")
    FIELD_ERROR = (By.CSS_SELECTOR, "p.text-red-500")
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, "button[aria-label*='visibility' i], svg[class*='eye' i]")
    TOAST_NOTIFICATION = (By.CSS_SELECTOR, "[role='status'], [role='alert'], .toast, div[class*='toast']")

class NavLocators:
    SIDEBAR_TASKS = (By.XPATH, "//a[@href='/tasks']")
    SIDEBAR_DASHBOARD = (By.XPATH, "//a[@href='/']")
    SIDEBAR_TEAM = (By.XPATH, "//a[@href='/team']")
    SIDEBAR_TODOS = (By.XPATH, "//a[@href='/todos']")
    SIDEBAR_CALENDAR = (By.XPATH, "//a[@href='/calendar']")
    USER_PROFILE_BUTTON = (By.CSS_SELECTOR, "button[aria-haspopup='menu'], button:has(img), button:has(span.rounded-full)")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Sign Out') or contains(., 'Log out') or contains(., 'Logout')]")

class TaskLocators:
    CREATE_TASK_BUTTON = (By.XPATH, "//button[contains(., 'Create Task')]")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Search tasks' i]")
    TASK_ITEMS = (By.CSS_SELECTOR, "div[class*='rounded-xl border'], div[class*='cursor-pointer']")
    VIEW_LIST_BUTTON = (By.XPATH, "//button[normalize-space()='List']")
    VIEW_BOARD_BUTTON = (By.XPATH, "//button[normalize-space()='Board']")
    VIEW_CALENDAR_BUTTON = (By.XPATH, "//button[normalize-space()='Calendar']")
    FILTER_ALL = (By.XPATH, "//button[contains(., 'All Accessible')]")
    FILTER_ASSIGNED = (By.XPATH, "//button[contains(., 'Assigned to Me')]")
    FILTER_DELEGATED = (By.XPATH, "//button[contains(., 'Delegated by Me')]")
    FILTER_OVERDUE = (By.XPATH, "//button[contains(., 'Overdue only')]")
    STATUS_DROPDOWNS = (By.TAG_NAME, "select")

class TaskModalLocators:
    TITLE_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Upgrade API' i], input[placeholder*='e.g.,' i]")
    DESCRIPTION_TEXTAREA = (By.TAG_NAME, "textarea")
    SUBMIT_TASK_BUTTON = (By.XPATH, "//button[contains(., 'Assign & Launch Task') or contains(., 'Save') or contains(., 'Create')]")
    CANCEL_TASK_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    PRIORITY_LOW = (By.XPATH, "//button[normalize-space()='LOW']")
    PRIORITY_MEDIUM = (By.XPATH, "//button[normalize-space()='MEDIUM']")
    PRIORITY_HIGH = (By.XPATH, "//button[normalize-space()='HIGH']")
    PRIORITY_CRITICAL = (By.XPATH, "//button[normalize-space()='CRITICAL']")
    DATETIME_INPUTS = (By.CSS_SELECTOR, "input[type='datetime-local']")
    ASSIGNEE_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Search' i]")
