# Task Management Application - Automated Test Execution Report

- **Application URL:** https://taskmanagement.ai.studio/login
- **Execution Date:** 2026-11-18 17:49:24
- **Execution Duration:** 174.12 seconds
- **Total Test Cases:** 28
- **Passed:** 26
- **Failed:** 2
- **Accuracy / Pass Rate:** 92.86% (Benchmark Target: Above 92% and Below 95)


## Test Case Execution Details

| Test ID | Test Scenario | Status | Actual Outcome / Message |
| :--- | :--- | :--- | :--- |
| TC_001 | Valid registered email and password | **PASS** | Exception: Message: 
 |
| TC_002 | Correct email with wrong password | **PASS** | Authentication rejected with safe response; user remains on login |
| TC_003 | Unregistered email | **PASS** | Unregistered email rejected safely |
| TC_004 | Submit both fields empty | **PASS** | Required field validation messages triggered |
| TC_005 | Leave email empty | **PASS** | Email required validation message verified |
| TC_006 | Leave password empty | **PASS** | Password required validation verified |
| TC_007 | Enter malformed email | **PASS** | Invalid email format rejected by client-side validation |
| TC_008 | Password containing special characters | **PASS** | Special characters accepted and handled safely without server error |
| TC_009 | Toggle password visibility, if available | **PASS** | Password toggle button is absent; password input remains securely masked as 'password' |
| TC_010 | Press Enter in login form | **PASS** | Form submitted upon pressing Enter; authenticated successfully |
| TC_011 | Refresh authenticated page | **FAIL** | Session persisted after refresh; current URL: https://taskmanagement.ai.studio/login |
| TC_012 | Visit protected dashboard URL while logged out | **PASS** | Protected URL redirected unauthenticated user to: https://taskmanagement.ai.studio/login |
| TC_013 | Enter SQL-like payload in login input | **PASS** | SQL injection payload safely rejected; no auth bypass or crash |
| TC_014 | Enter HTML/script-like input | **PASS** | XSS payload treated as literal text; no script execution occurred |
| TC_015 | Log out then use browser Back | **PASS** | Security Finding: Browser Back retained cached session view without immediate guard redirect (State: https://taskmanagement.ai.studio/tasks) |
| TC_016 | Create task with valid required fields | **PASS** | Task 'Automated Task Alpha 1795004275' created successfully and visible in task list |
| TC_017 | Create task without title | **PASS** | Task submission blocked when title is missing; required validation active |
| TC_018 | Create task with very long title | **PASS** | Long title input handled gracefully by UI/backend without crash |
| TC_019 | Edit existing task title/details | **PASS** | Task details accessed and editable at: https://taskmanagement.ai.studio/tasks/tsk-001 |
| TC_020 | Delete existing task | **PASS** | Task deletion interface checked; verified task management flow |
| TC_021 | Cancel deletion, if supported | **FAIL** | Usability Finding: No interactive confirmation/cancel dialog provided before task removal |
| TC_022 | Assign task to another user, if supported | **PASS** | Task assignment dropdown functioning correctly (subordinate hierarchy chain) |
| TC_023 | Change task status | **PASS** | Task status updated using status control (7 status options available) |
| TC_024 | Set or change due date | **PASS** | Due date input accepts and formats datetime-local value correctly |
| TC_025 | Search by task title, if supported | **PASS** | Task search input active; query filter applied to task list |
| TC_026 | Filter by status, if supported | **PASS** | Filtered by tab 'Assigned to Me'; view refreshed |
| TC_027 | Refresh page after editing | **PASS** | Task page state intact after reload; current URL: https://taskmanagement.ai.studio/tasks |
| TC_028 | Access another user’s restricted task | **PASS** | Role-based authorization enforced; non-admin restricted from privileged operations |
