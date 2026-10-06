# TaskFlow API

TaskFlow API is a small REST API built with FastAPI for managing users and tasks.

The project is intentionally simple and includes Markdown documentation that can be monitored by a Self-Healing Documentation system.

---

## Features

- User management
- Task management
- Task assignment
- Task status management
- REST APIs
- Swagger API documentation
- ReDoc API documentation
- In-memory data storage
- Automated tests
- Docker support
- Markdown project documentation

---

## Tech Stack

- Python 3.12+
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- Docker

---

## Project Structure

```text
taskflow-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── tasks.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── user_service.py
│       └── task_service.py
│
├── docs/
│   ├── api/
│   │   ├── users.md
│   │   └── tasks.md
│   ├── architecture.md
│   ├── database.md
│   └── development.md
│
├── tests/
│   ├── test_users.py
│   └── test_tasks.py
│
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt