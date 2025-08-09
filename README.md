# Task tracker
Simple cli task tracker application. Stores all data in json file in cwd.

## Requirements
- Python 3.11 or higher

## Installation
```bash
$ pip install git+https://github.com/NovaHFly/task_tracker
```

## Usage
```bash
task_tracker [-h] <subcommand> ...
```

## Commands
- Add new task
```bash
$ task_tracker add "Wash dishes"
| 1 |              Wash dishes               |   todo    |2025-08-09T06:00:00.000000|2025-08-09T06:00:00.000000|
```
- View task details. Shows full task description (Even if it's too long)
```bash
$ task_tracker view <id>
| 4 | Some very long name for a very very long and tedious task |   todo    |2025-08-09T07:00:00.000000|2025-08-09T06:00:00.000000|
```
- Update task description
```bash
$ task_tracker update <id> <description>
| 1 |             Play with cat              |   todo    |2025-08-09T06:00:00.000000|2025-08-09T08:00:00.000000|
```
- Delete task
```bash
$ task_tracker delete <id>
| 1 |             Play with cat              |   todo    |2025-08-09T06:00:00.000000|2025-08-09T08:00:00.000000|
```
- Update task status. Available statuses:
  - todo
  - in-progress
  - done
```bash
$ task_tracker mark <id> <status>
| 1 |             Play with cat              |in-progress|2025-08-09T06:00:00.000000|2025-08-09T08:00:00.000000|
```
- List tasks with filtering by status. If no status provided, show all tasks.
```bash
$ task_tracker list [<status>]
| 1 |             Play with cat              |in-progress|2025-08-09T06:00:00.000000|2025-08-09T08:00:00.000000|
| 4 | Some very long name for a very very... |   todo    |2025-08-09T07:00:00.000000|2025-08-09T06:00:00.000000|
```