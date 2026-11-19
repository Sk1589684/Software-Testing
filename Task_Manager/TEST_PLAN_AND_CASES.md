# Task Management Application - Manual Testing Plan & Test Cases

**Application URL:** [https://taskmanagement.ai.studio/login](https://taskmanagement.ai.studio/login)  
**Document Status:** Proposed test cases & Automated Suite  
**Execution Status:** Active / Automated  
**Scope Note:** These test scenarios validate authentication, task operations, access control, input validation, usability, and session behavior for the Task Management web application.

---

## 1. Testing Objectives and Scope

- **Authentication & Security:** Validate login, logout, credential verification, validation errors, session persistence, SQL injection protection, XSS protection, and protected route access.
- **Task Operations (CRUD):** Verify task creation, title validation, character limit handling, editing, deleting, deletion cancellation, status updates, and due dates.
- **Workflow & Collaboration:** Validate task assignment, employee search, role-based visibility, status filtering, and search functionality.
- **Session & Navigation:** Verify browser back-button behavior after logout, page reloads, and unauthorized URL manipulation.

---

## 2. Test Cases Specification

### Suite 1: Authentication and Session (TC_001 to TC_015)

| ID / Priority | Test Scenario | Steps | Expected Result | Automated Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC_001 (High)** | Valid registered email and password | 1. Navigate to `/login`<br>2. Enter valid email (`admin@company.com`)<br>3. Enter valid password (`Password123!`)<br>4. Click **Sign In** | User successfully authenticates and reaches the dashboard landing page (`/`) | Implemented |
| **TC_002 (High)** | Correct email with wrong password | 1. Enter valid email<br>2. Enter incorrect password (`WrongPass!`)<br>3. Click **Sign In** | Authentication rejected with safe error message (e.g., "Invalid email or password credentials") | Implemented |
| **TC_003 (High)** | Unregistered email | 1. Enter unregistered email (`unknown_user_99@test.com`)<br>2. Enter password<br>3. Click **Sign In** | Authentication rejected safely | Implemented |
| **TC_004 (High)** | Submit both fields empty | 1. Clear email and password fields<br>2. Click **Sign In** | Required field error messages appear ("Please enter a valid email address", "Password is required") | Implemented |
| **TC_005 (High)** | Leave email empty | 1. Clear email field<br>2. Enter valid password<br>3. Click **Sign In** | Email required validation message displayed | Implemented |
| **TC_006 (High)** | Leave password empty | 1. Enter valid email<br>2. Clear password field<br>3. Click **Sign In** | Password required validation message displayed | Implemented |
| **TC_007 (Medium)** | Enter malformed email | 1. Enter `invalid-email-format`<br>2. Enter password<br>3. Submit form | Invalid format validation is triggered and rejected | Implemented |
| **TC_008 (Medium)** | Password with special characters | 1. Enter email<br>2. Enter password containing `@#$%^&*!()` (`Password123!`)<br>3. Submit | Special characters handled safely without error; login follows credential validity | Implemented |
| **TC_009 (Medium)** | Toggle password visibility | 1. Enter password<br>2. Click visibility eye icon if present<br>3. Verify input type changes between `password` and `text` | Password visibility toggles without modifying underlying string value | Implemented |
| **TC_010 (Medium)** | Press Enter in login form | 1. Enter valid credentials<br>2. Press `Enter` key on password field | Form automatically submits and user is logged in | Implemented |
| **TC_011 (High)** | Refresh authenticated page | 1. Sign in successfully<br>2. Refresh browser (`F5` / reload) | User session persists; page does not kick user back to login | Implemented |
| **TC_012 (High)** | Visit protected URL while logged out | 1. Open fresh session without logging in<br>2. Navigate directly to `https://taskmanagement.ai.studio/tasks` or `/` | Access denied or user is redirected back to `/login` | Implemented |
| **TC_013 (High)** | Enter SQL-like payload in login | 1. Enter `' OR '1'='1` in email and password fields<br>2. Submit form | Input rejected safely; no SQL injection bypass or server error | Implemented |
| **TC_014 (High)** | Enter HTML/script-like input (XSS) | 1. Enter `<script>alert('XSS')</script>` in fields<br>2. Submit form | Input treated as raw text; script does not execute in the browser | Implemented |
| **TC_015 (High)** | Log out then use browser Back | 1. Login to app<br>2. Log out via logout button<br>3. Click browser Back button | User cannot view cached protected data; redirected to login | Implemented |

---

### Suite 2: Task Management and Authorization (TC_016 to TC_028)

| ID / Priority | Test Scenario | Steps | Expected Result | Automated Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC_016 (High)** | Create task with valid required fields *(Title is Compulsory)* | 1. Navigate to `/tasks`<br>2. Click **Create Task**<br>3. Enter mandatory title, optional description<br>4. Scroll down & click **Assign & Launch Task** | Task created and visible in the task list | Implemented |
| **TC_017 (High)** | Create task without title *(Compulsory Validation)* | 1. Open Create Task modal<br>2. Leave title empty<br>3. Fill description, scroll down & click submit | Required title validation prevents creation; modal remains open; task cannot be created | Implemented |
| **TC_018 (Medium)** | Create task with very long title | 1. Enter 300+ character title<br>2. Submit | Length handled per specification; no UI crash or layout overflow | Implemented |
| **TC_019 (High)** | Edit existing task title/details | 1. Select a task<br>2. Edit title/description<br>3. Save | Changes saved and updated details displayed | Implemented |
| **TC_020 (High)** | Delete existing task | 1. Select task<br>2. Click delete and confirm | Task removed from list following expected confirmation flow | Implemented |
| **TC_021 (Medium)** | Cancel deletion, if supported | 1. Click delete on a task<br>2. Click Cancel in confirmation dialog | Deletion cancelled; task remains unchanged | Implemented |
| **TC_022 (High)** | Assign task to another user | 1. Open task assignment dropdown/modal<br>2. Select assignee employee<br>3. Save | Assignee updated and displayed on task card | Implemented |
| **TC_023 (High)** | Change task status | 1. Open task status selector (e.g. TO_DO -> IN_PROGRESS -> COMPLETED)<br>2. Update status | New status saved and reflected immediately | Implemented |
| **TC_024 (Medium)** | Set or change due date | 1. Select date picker on task<br>2. Set target due date<br>3. Save | Due date persists correctly | Implemented |
| **TC_025 (Medium)** | Search by task title | 1. Type keyword into task search input<br>2. Observe filtered list | Only tasks matching query are returned | Implemented |
| **TC_026 (Medium)** | Filter by status | 1. Select status filter (e.g., IN_PROGRESS, COMPLETED)<br>2. Review list | Only tasks with selected status are shown | Implemented |
| **TC_027 (High)** | Refresh page after editing | 1. Edit task details<br>2. Refresh page | Persisted changes still show correctly after reload | Implemented |
| **TC_028 (High)** | Access another user's restricted task | 1. Sign in as Executive/Employee<br>2. Try to access restricted task URL or admin-only action | Unauthorized access blocked safely | Implemented |

---

## 3. Test Execution Procedure

1. **Environment Setup:** Ensure Python 3.10+ and Google Chrome are installed.
2. **Dependencies:** `selenium` 4.x is installed in the workspace environment.
3. **Running the Automation:**
   ```bash
   cd c:\Users\hp\PythonPractice\Task_Manager
   python run_all_tests.py
   ```
4. **Individual Test Suites:**
   ```bash
   # Run Authentication & Session tests (TC_001 to TC_015)
   python test_auth_session.py

   # Run Task Management & Authorization tests (TC_016 to TC_028)
   python test_task_management.py
   ```
5. **Headless vs Headed Mode:** By default, scripts run in headless mode for speed. Set `--headed` or pass `headless=False` in `config.py` to see the live browser window.

---

## 4. Detailed Test Execution Template

```text
Test Case ID: TC_001
Preconditions: Authorized test account exists; login page is open.
Steps: 
  1. Enter registered email.
  2. Enter correct password.
  3. Select Login.
Expected result: Authenticated user reaches the authorized landing page.
Actual result: _____________________________________
Status: [ PASS | FAIL | BLOCKED | NOT APPLICABLE ]
Evidence / Defect ID: _____________________________________
```

---

## 5. Defect Reporting Template

```text
Defect ID / Title: __________________________________________
Environment (browser, OS, build): Chrome / Windows 11 / v1.0.0
Severity / Priority: [ Critical | High | Medium | Low ]
Preconditions and test data: __________________________________________
Steps to reproduce:
  1. Navigate to ...
  2. Enter ...
  3. Click ...
Expected result: __________________________________________
Actual result: __________________________________________
Screenshot / evidence: screenshots/defect_XXXX.png
Status / retest notes: [ New | In Progress | Resolved | Closed ]
```

---

## 6. Test Summary Matrix

| Category | Total Proposed | Automated | Passed | Failed | Blocked |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Authentication & Session** | 15 | 15 | - | - | - |
| **Task Operations & Authorization** | 13 | 13 | - | - | - |
| **Total** | **28** | **28** | - | - | - |
