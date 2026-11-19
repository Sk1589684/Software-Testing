# Software Testing Repository

A collection of automated regression suites, test plans, execution reports, and framework implementations for web application testing by [@Sk1589684](https://github.com/Sk1589684).

---

## 📁 Repository Structure

```text
Software-Testing/
├── Task_Manager/                     # Automated testing suite for Task Management web application
│   ├── config.py                     # Environment URLs, test accounts, and WebDriver config
│   ├── locators.py                   # Page Object Model (POM) locators
│   ├── run_all_tests.py              # Master test runner
│   ├── test_auth_session.py          # Suite 1: Authentication & Session tests
│   ├── test_task_management.py       # Suite 2: Task CRUD, assignment & lifecycle tests
│   ├── TEST_PLAN_AND_CASES.md        # Comprehensive manual & automated test cases specification
│   ├── TEST_EXECUTION_REPORT.md      # Execution summary, metrics, and benchmark findings
│   ├── README.md                     # Suite instructions and setup guide
│   └── screenshots/                  # Execution artifacts and evidence captures
└── .gitignore                        # Git ignore patterns for Python & caches
```

---

## 🚀 Projects Overview

### 1. Task Management Automation Suite (`Task_Manager/`)
- **Target URL:** `https://taskmanagement.ai.studio/login`
- **Framework:** Python + Selenium WebDriver + Pytest
- **Test Scope:**
  - **Authentication & Security:** Login, password masking, enter-key submit, SQL injection & XSS sanitization, session persistence, route guards, and back-button behavior.
  - **Task Operations (CRUD):** Compulsory title validation, rich description, assignee selection, status transitions, and due date configuration.
- **Pass Rate:** 92.86% (26 / 28 Passed)
