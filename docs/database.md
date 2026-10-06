
### `docs/database.md`

```text
# Database Documentation

---

## Current Storage

TaskFlow API currently uses in-memory Python lists instead of a persistent database.

---

## User Storage

Users are stored in:

`app.services.user_service.users`

The storage is initialized as:

```python
users = []