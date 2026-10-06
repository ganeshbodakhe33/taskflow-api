
### `docs/architecture.md`

```text
# Architecture

TaskFlow API follows a simple layered architecture.

---

## Architecture Flow

Client

↓

FastAPI Routes

↓

Pydantic Schemas

↓

Service Layer

↓

In-Memory Storage

---

## API Layer

The API layer is located in:

app/api/

It contains:

- `users.py`
- `tasks.py`

### Available Routes

- `/api/users`
- `/api/tasks`
- `/health`

---

## Schema Layer

The schema layer is located in:

app/schemas/

It contains the Pydantic request and response models.

### Available Schemas

- `UserCreate`
- `UserResponse`
- `TaskCreate`
- `TaskResponse`

---

## Service Layer

The service layer is located in:

app/services/

It contains the application business logic.

### Available Services

- `user_service.py`
- `task_service.py`

---

## Storage

TaskFlow API currently uses Python lists for storage.

There is no persistent database.

### User Storage

Users are stored in:

`app.services.user_service.users`

### Task Storage

Tasks are stored in:

`app.services.task_service.tasks`

---

## Application Entry Point

The application starts from:

`app/main.py`

The FastAPI application is created there and the routers are registered there.

---

## Health Check

The application provides a health-check endpoint:

GET /health

### Response

```json
{
  "status": "healthy",
  "service": "taskflow-api"
}