from __future__ import annotations

import json
from pathlib import Path

from .models import Task


def _create_blank_database_file() -> None:
    database_file_path.touch()
    with database_file_path.open('w', encoding='UTF-8') as f:
        json.dump([], f)


def save_database(database: dict[int, Task]) -> None:
    """Save database into json file.

    :param dict[int, Task] database: Database to save.
    """
    with database_file_path.open('w', encoding='UTF-8') as f:
        json.dump(
            sorted(
                (task.to_dict() for task in database.values()),
                key=lambda x: x['id'],
            ),
            f,
        )


def load_database() -> dict[int, Task]:
    """Load database from json file.

    :returns dict[int, Task]: Loaded database.
    """
    global database

    if not database_file_path.exists():
        _create_blank_database_file()
        return {}

    with database_file_path.open() as f:
        raw_database = json.load(f)
        return {item['id']: Task.from_dict(item) for item in raw_database}


def get_next_id() -> int:
    """Get next database identifier"""
    global _latest_id
    _latest_id += 1
    return _latest_id


database_file_path = Path('tasks.json')
database: dict[int, Task] = load_database()
_latest_id = max(database) if database else 0
