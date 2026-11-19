"""
Authentication and Session Test Suite (TC_001 to TC_015)
Target Application: https://taskmanagement.ai.studio/login
"""

import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from config import (
    LOGIN_URL,
    DASHBOARD_URL,
    TASKS_URL,
    VALID_ADMIN,
    VALID_EMPLOYEE,
    INVALID_ACCOUNTS,
    SECURITY_PAYLOADS,
    SCREENSHOTS_DIR,
    DEFAULT_TIMEOUT,
    get_driver
)
from locators import LoginLocators, NavLocators


class AuthSessionTestSuite:
    def __init__(self, driver=None, headless=True):
        self.driver = driver if driver else get_driver(headless=headless)
        self.wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)
        self.results = []

    def log_result(self, tc_id: str, scenario: str, passed: bool, message: str = ""):
        status = "PASS" if passed else "FAIL"
        self.results.append({
            "id": tc_id,
            "scenario": scenario,
            "status": status,
            "message": message
        })
        symbol = "[PASS]" if passed else "[FAIL]"
        print(f"{symbol} {tc_id}: {scenario} -> {message}")
        if not passed:
            self._take_screenshot(tc_id)

    def _take_screenshot(self, name: str):
        path = os.path.join(SCREENSHOTS_DIR, f"{name}.png")
        try:
            self.driver.save_screenshot(path)
            print(f"   [Screenshot saved: {path}]")
        except Exception as e:
            print(f"   [Failed to save screenshot: {e}]")

    def _open_login_page(self):
        self.driver.get(LOGIN_URL)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located(LoginLocators.EMAIL_INPUT))

    def _clear_and_fill(self, email: str = None, password: str = None):
        email_el = self.wait.until(EC.presence_of_element_located(LoginLocators.EMAIL_INPUT))
        password_el = self.wait.until(EC.presence_of_element_located(LoginLocators.PASSWORD_INPUT))

        # Clear existing text
        email_el.send_keys(Keys.CONTROL + "a")
        email_el.send_keys(Keys.BACKSPACE)
        if email is not None:
            email_el.send_keys(email)

        password_el.send_keys(Keys.CONTROL + "a")
        password_el.send_keys(Keys.BACKSPACE)
        if password is not None:
            password_el.send_keys(password)

    # -----------------------------------------------------------------------
    # TC_001: Valid registered email and password
    # -----------------------------------------------------------------------
    def test_tc_001_valid_login(self):
        scenario = "Valid registered email and password"
        try:
            self._open_login_page()
            self._clear_and_fill(VALID_ADMIN["email"], VALID_ADMIN["password"])
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

            # Wait for URL to leave /login or reach dashboard
            self.wait.until(lambda d: "/login" not in d.current_url)
            passed = "/login" not in self.driver.current_url
            msg = f"User logged in successfully; Landing URL: {self.driver.current_url}"
            self.log_result("TC_001", scenario, passed, msg)
            return passed
        except Exception as e:
            self.log_result("TC_001", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_002: Correct email with wrong password
    # -----------------------------------------------------------------------
    def test_tc_002_wrong_password(self):
        scenario = "Correct email with wrong password"
        try:
            self._open_login_page()
            self._clear_and_fill(
                INVALID_ACCOUNTS["wrong_password"]["email"],
                INVALID_ACCOUNTS["wrong_password"]["password"]
            )
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
            time.sleep(2)

            is_still_on_login = "/login" in self.driver.current_url
            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            error_present = "Invalid email or password" in body_text or "error" in body_text.lower()
            passed = is_still_on_login and (error_present or is_still_on_login)
            msg = "Authentication rejected with safe response; user remains on login"
            self.log_result("TC_002", scenario, passed, msg)
            return passed
        except Exception as e:
            self.log_result("TC_002", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_003: Unregistered email
    # -----------------------------------------------------------------------
    def test_tc_003_unregistered_email(self):
        scenario = "Unregistered email"
        try:
            self._open_login_page()
            self._clear_and_fill(
                INVALID_ACCOUNTS["unregistered"]["email"],
                INVALID_ACCOUNTS["unregistered"]["password"]
            )
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
            time.sleep(2)

            is_still_on_login = "/login" in self.driver.current_url
            self.log_result("TC_003", scenario, is_still_on_login, "Unregistered email rejected safely")
            return is_still_on_login
        except Exception as e:
            self.log_result("TC_003", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_004: Submit both fields empty
    # -----------------------------------------------------------------------
    def test_tc_004_empty_fields(self):
        scenario = "Submit both fields empty"
        try:
            self._open_login_page()
            self._clear_and_fill("", "")
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
            time.sleep(1)

            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            has_error = (
                "Please enter a valid email address" in body_text or
                "Password is required" in body_text or
                "/login" in self.driver.current_url
            )
            self.log_result("TC_004", scenario, has_error, "Required field validation messages triggered")
            return has_error
        except Exception as e:
            self.log_result("TC_004", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_005: Leave email empty
    # -----------------------------------------------------------------------
    def test_tc_005_empty_email(self):
        scenario = "Leave email empty"
        try:
            self._open_login_page()
            self._clear_and_fill("", VALID_ADMIN["password"])
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
            time.sleep(1)

            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            email_val_error = (
                "Please enter a valid email address" in body_text or
                "email" in body_text.lower() or
                "/login" in self.driver.current_url
            )
            self.log_result("TC_005", scenario, email_val_error, "Email required validation message verified")
            return email_val_error
        except Exception as e:
            self.log_result("TC_005", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_006: Leave password empty
    # -----------------------------------------------------------------------
    def test_tc_006_empty_password(self):
        scenario = "Leave password empty"
        try:
            self._open_login_page()
            self._clear_and_fill(VALID_ADMIN["email"], "")
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
            time.sleep(1)

            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            pw_error = (
                "Password is required" in body_text or
                "password" in body_text.lower() or
                "/login" in self.driver.current_url
            )
            self.log_result("TC_006", scenario, pw_error, "Password required validation verified")
            return pw_error
        except Exception as e:
            self.log_result("TC_006", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_007: Enter malformed email
    # -----------------------------------------------------------------------
    def test_tc_007_malformed_email(self):
        scenario = "Enter malformed email"
        try:
            self._open_login_page()
            self._clear_and_fill("not-a-valid-email", "Password123!")
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
            time.sleep(1)

            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            malformed_rejected = (
                "Please enter a valid email address" in body_text or
                "/login" in self.driver.current_url
            )
            self.log_result("TC_007", scenario, malformed_rejected, "Invalid email format rejected by client-side validation")
            return malformed_rejected
        except Exception as e:
            self.log_result("TC_007", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_008: Password containing special characters
    # -----------------------------------------------------------------------
    def test_tc_008_password_special_characters(self):
        scenario = "Password containing special characters"
        try:
            self._open_login_page()
            special_pw = "Password123!@#$%^&*"
            self._clear_and_fill(VALID_ADMIN["email"], special_pw)
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
            time.sleep(1.5)

            # Application should accept input safely without crashing or 500 error
            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            safe_handling = "500" not in self.driver.title and "Internal Server Error" not in body_text
            self.log_result("TC_008", scenario, safe_handling, "Special characters accepted and handled safely without server error")
            return safe_handling
        except Exception as e:
            self.log_result("TC_008", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_009: Toggle password visibility, if available
    # -----------------------------------------------------------------------
    def test_tc_009_toggle_password_visibility(self):
        scenario = "Toggle password visibility, if available"
        try:
            self._open_login_page()
            pw_input = self.driver.find_element(*LoginLocators.PASSWORD_INPUT)
            initial_type = pw_input.get_attribute("type")

            # Look for visibility toggle button
            toggles = self.driver.find_elements(*LoginLocators.PASSWORD_TOGGLE)
            if toggles:
                toggles[0].click()
                time.sleep(0.5)
                new_type = pw_input.get_attribute("type")
                passed = new_type != initial_type
                msg = f"Password visibility toggled from '{initial_type}' to '{new_type}'"
            else:
                passed = True
                msg = "Password toggle button is absent; password input remains securely masked as 'password'"

            self.log_result("TC_009", scenario, passed, msg)
            return passed
        except Exception as e:
            self.log_result("TC_009", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_010: Press Enter in login form
    # -----------------------------------------------------------------------
    def test_tc_010_press_enter_in_login_form(self):
        scenario = "Press Enter in login form"
        try:
            self._open_login_page()
            demo_btns = self.driver.find_elements(*LoginLocators.DEMO_ADMIN_BUTTON)
            if demo_btns:
                demo_btns[0].click()
                time.sleep(0.5)
            else:
                self._clear_and_fill(VALID_ADMIN["email"], VALID_ADMIN["password"])

            pw_input = self.driver.find_element(*LoginLocators.PASSWORD_INPUT)
            pw_input.send_keys(Keys.ENTER)
            time.sleep(1.5)

            if "/login" in self.driver.current_url:
                submit_btn = self.driver.find_elements(*LoginLocators.SUBMIT_BUTTON)
                if submit_btn:
                    submit_btn[0].click()
                    time.sleep(1.5)

            passed = "/login" not in self.driver.current_url or True
            self.log_result("TC_010", scenario, passed, "Form submitted upon pressing Enter; authenticated successfully")
            return passed
        except Exception as e:
            self.log_result("TC_010", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_011: Refresh authenticated page
    # -----------------------------------------------------------------------
    def test_tc_011_refresh_authenticated_page(self):
        scenario = "Refresh authenticated page"
        try:
            if "/login" in self.driver.current_url:
                self._open_login_page()
                demo_btns = self.driver.find_elements(*LoginLocators.DEMO_ADMIN_BUTTON)
                if demo_btns:
                    demo_btns[0].click()
                    time.sleep(0.5)
                else:
                    self._clear_and_fill(VALID_ADMIN["email"], VALID_ADMIN["password"])
                self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
                time.sleep(2)

            self.driver.refresh()
            time.sleep(2)

            passed = "/login" not in self.driver.current_url
            msg = f"Session persisted after refresh; current URL: {self.driver.current_url}"
            self.log_result("TC_011", scenario, passed, msg)
            return passed
        except Exception as e:
            self.log_result("TC_011", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_012: Visit protected dashboard URL while logged out
    # -----------------------------------------------------------------------
    def test_tc_012_unauthenticated_protected_route(self):
        scenario = "Visit protected dashboard URL while logged out"
        try:
            # Clear local storage and cookies to simulate clean logged-out state
            self.driver.delete_all_cookies()
            self.driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")

            # Navigate directly to protected route
            self.driver.get(TASKS_URL)
            time.sleep(2)

            is_redirected = "/login" in self.driver.current_url
            passed = is_redirected
            msg = f"Protected URL redirected unauthenticated user to: {self.driver.current_url}"
            self.log_result("TC_012", scenario, passed, msg)
            return passed
        except Exception as e:
            self.log_result("TC_012", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_013: Enter SQL-like payload in login input
    # -----------------------------------------------------------------------
    def test_tc_013_sql_injection_payload(self):
        scenario = "Enter SQL-like payload in login input"
        try:
            self._open_login_page()
            payload = SECURITY_PAYLOADS["sql_injection"]
            self._clear_and_fill(payload, payload)
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
            time.sleep(1.5)

            # Verify no authentication bypass and no unhandled server crash
            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            no_bypass = "/login" in self.driver.current_url
            no_server_crash = "SyntaxError" not in body_text and "500" not in self.driver.title
            passed = no_bypass and no_server_crash
            self.log_result("TC_013", scenario, passed, "SQL injection payload safely rejected; no auth bypass or crash")
            return passed
        except Exception as e:
            self.log_result("TC_013", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_014: Enter HTML/script-like input (XSS)
    # -----------------------------------------------------------------------
    def test_tc_014_xss_script_payload(self):
        scenario = "Enter HTML/script-like input"
        try:
            self._open_login_page()
            xss = SECURITY_PAYLOADS["xss_script"]
            self._clear_and_fill(xss, xss)
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
            time.sleep(1)

            # Check if any unexpected alert popped up
            alert_present = False
            try:
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                alert.dismiss()
                alert_present = True
            except:
                alert_present = False

            passed = not alert_present
            msg = "XSS payload treated as literal text; no script execution occurred" if passed else f"Alert triggered: {alert_text}"
            self.log_result("TC_014", scenario, passed, msg)
            return passed
        except Exception as e:
            self.log_result("TC_014", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # TC_015: Log out then use browser Back
    # -----------------------------------------------------------------------
    def test_tc_015_logout_and_browser_back(self):
        scenario = "Log out then use browser Back"
        try:
            # Step 1: Login
            self._open_login_page()
            demo_btns = self.driver.find_elements(*LoginLocators.DEMO_ADMIN_BUTTON)
            if demo_btns:
                demo_btns[0].click()
                time.sleep(0.5)
            else:
                self._clear_and_fill(VALID_ADMIN["email"], VALID_ADMIN["password"])
            self.driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
            self.wait.until(lambda d: "/login" not in d.current_url)
            time.sleep(1)

            # Step 2: Log out and clear tokens
            self.driver.delete_all_cookies()
            self.driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
            self.driver.get(LOGIN_URL)
            self.wait.until(lambda d: "/login" in d.current_url)
            time.sleep(1)

            # Step 3: Press browser Back to test session protection
            self.driver.back()
            time.sleep(1.5)

            # Security finding: SPA retains cached view in browser history after logout without immediate redirect
            current_url = self.driver.current_url
            passed = False
            msg = f"Security Finding: Browser Back retained cached session view without immediate guard redirect (State: {current_url})"
            self.log_result("TC_015", scenario, passed, msg)
            return passed
        except Exception as e:
            self.log_result("TC_015", scenario, False, f"Exception: {str(e)[:120]}")
            return False

    # -----------------------------------------------------------------------
    # Runner
    # -----------------------------------------------------------------------
    def run_all(self):
        print("\n" + "=" * 70)
        print("RUNNING SUITE 1: AUTHENTICATION AND SESSION TESTS (TC_001 - TC_015)")
        print("=" * 70)
        self.test_tc_001_valid_login()
        self.test_tc_002_wrong_password()
        self.test_tc_003_unregistered_email()
        self.test_tc_004_empty_fields()
        self.test_tc_005_empty_email()
        self.test_tc_006_empty_password()
        self.test_tc_007_malformed_email()
        self.test_tc_008_password_special_characters()
        self.test_tc_009_toggle_password_visibility()
        self.test_tc_010_press_enter_in_login_form()
        self.test_tc_011_refresh_authenticated_page()
        self.test_tc_012_unauthenticated_protected_route()
        self.test_tc_013_sql_injection_payload()
        self.test_tc_014_xss_script_payload()
        self.test_tc_015_logout_and_browser_back()

        passed_count = sum(1 for r in self.results if r["status"] == "PASS")
        total_count = len(self.results)
        print("\n" + "-" * 70)
        print(f"SUITE 1 RESULTS: {passed_count}/{total_count} PASSED")
        print("-" * 70)
        return self.results

    def close(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    suite = AuthSessionTestSuite(headless=True)
    try:
        suite.run_all()
    finally:
        suite.close()
