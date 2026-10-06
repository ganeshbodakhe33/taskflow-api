
### `docs/api/tasks.md`

```text
# Task APIs

Base URL:

/api/tasks

---

## Create Task

Creates a new task.

### Endpoint

POST /api/tasks/

### Request Body

```json
{
  "title": "Complete documentation",
  "description": "Update project documentation",
  "assignee_id": 1
}