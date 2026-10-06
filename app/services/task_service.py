tasks = []


def create_task(task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "assignee_id": task.assignee_id,
        "status": "todo",
    }

    tasks.append(new_task)

    return new_task


def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None