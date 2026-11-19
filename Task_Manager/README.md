# Task Management Test Automation Project

This folder contains the complete test suite and testing documentation for the Task Management web application at:  
👉 **[https://taskmanagement.ai.studio/login](https://taskmanagement.ai.studio/login)**

---

## 📁 Folder Structure

```
Task_Manager/
├── TEST_PLAN_AND_CASES.md      # Complete manual test plan & 28 test cases specification
├── TEST_EXECUTION_REPORT.md    # Automated test execution report generated after run
├── run_all_tests.py            # Master test runner executing all 28 test cases
├── test_auth_session.py        # Suite 1: Authentication & Session tests (TC_001 to TC_015)
├── test_task_management.py     # Suite 2: Task CRUD & Authorization tests (TC_016 to TC_028)
├── SecondTestCase.py           # TC_016: Create task with valid credentials, modal scroll & title
├── ThirdTestCase_EmptyTitle.py # TC_017: Compulsory Title validation (proves task cannot be created without title)
├── test_login_visual.py        # Visible on-screen login automation test
├── config.py                   # Environment settings, URLs, test accounts & driver factory
├── locators.py                 # Centralized Page Object Locators
├── inspect_ui.py               # Live DOM inspector script for login and dashboard
├── inspect_tasks.py            # Live inspector script for the /tasks page & filters
├── inspect_modal.py            # Live inspector script for Create Task modal elements
├── analyze_app.py              # Application bundle & route analyzer
├── test_selenium.py            # Minimal smoke test script to verify Chrome WebDriver
└── screenshots/                # Automatically captured screenshots on failures
```

---

## 🚀 How to Run the Tests

### 1. Run the Entire Test Suite (TC_001 to TC_028)
```bash
python run_all_tests.py
```
*Runs all 28 test cases in headless Chrome and outputs a formatted table along with an updated `TEST_EXECUTION_REPORT.md`.*

### 2. Run in Visible (Headed) Browser Mode
To watch Chrome automate the tests live in a browser window:
```bash
python run_all_tests.py --headed
```

### 3. Run Specific Test Suites
- **Authentication & Session (TC_001 to TC_015):**
  ```bash
  python test_auth_session.py
  ```
- **Task Management & Authorization (TC_016 to TC_028):**
  ```bash
  python test_task_management.py
  ```

### 4. Run Inspection / Smoke Scripts
```bash
# Verify basic Selenium Chrome connectivity
python test_selenium.py

# Inspect live UI elements on login page
python inspect_ui.py

# Inspect /tasks page layout and controls
python inspect_tasks.py

# Inspect Create Task modal dialog
python inspect_modal.py
```

---

## 🔑 Test Accounts & Credentials

| Role | Email | Password | Access Level |
| :--- | :--- | :--- | :--- |
| **Administrator** | `admin@company.com` | `Password123!` | Full admin access (Team, Tasks, Dashboard) |
| **Employee** | `emp@company.com` | `Password123!` | Executive / Standard user access |
