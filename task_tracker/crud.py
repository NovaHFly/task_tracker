from .models import StatusEnum, Task
from .storage import database, get_next_id


def create_task(description: str) -> Task:
    """Create new task.

    :param str description: Task description.
    :returns Task: New task.
    """
    new_task = Task(
        id=get_next_id(),
        description=description,
    )
    database[new_task.id] = new_task
    return new_task


def update_task(
    id_: int,
    description: str | None = None,
    status: StatusEnum | None = None,
) -> Task:
    """Update existing task.

    :param str | None description: New task description.
        Default is None (no changes).
    :param StatusEnum | None status: New task status.
        Default is None (no changes).
    :returns Task: Updated task.
    :raises KeyError: Id not found in database.
    """
    task = database[id_]
    if description is not None:
        task.description = description
    if status is not None:
        task.status = status
    return task


def delete_task(id_: int) -> Task:
    """Delete task from database.

    :param int id_: Id of task to delete.
    :param Task: Deleted task.
    :raises KeyError: Id not found in database.
    """
    task = database.pop(id_)
    return task


def list_tasks(filter_by_status: StatusEnum | None = None) -> list[Task]:
    """List existing tasks.

    :param StatusEnum | None filter_by_status: Return tasks with this status.
        None means no filter (default).

    :returns list[Task]: List of tasks.
    """
    if filter_by_status is None:
        return list(database.values())
    return [
        task for task in database.values() if task.status == filter_by_status
    ]
