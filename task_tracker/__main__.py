from argparse import ArgumentParser
from textwrap import shorten

from task_tracker.crud import create_task, delete_task, list_tasks, update_task
from task_tracker.models import StatusEnum, Task
from task_tracker.storage import database, save_database

STATUS_MAP = {
    'todo': StatusEnum.TO_DO,
    'in-progress': StatusEnum.IN_PROGRESS,
    'done': StatusEnum.DONE,
}
DEFAULT_DESCRIPTION_LENGTH = 40


def _format_task_message(
    task: Task,
    description_length: int | None = DEFAULT_DESCRIPTION_LENGTH,
) -> str:
    if description_length is None:
        description_str = task.description
    else:
        truncated_description = shorten(
            task.description,
            description_length,
            placeholder='...',
        )
        description_str = f'{truncated_description:^{description_length}}'
    return (
        f'|{task.id:^3}|{description_str}|{task.status:^11}|'
        f'{task.createdAt.isoformat():26}|{task.updatedAt.isoformat():26}|'
    )


def _construct_argparser() -> ArgumentParser:
    parser = ArgumentParser()

    subparsers = parser.add_subparsers(dest='subcommand')

    add_subcommand = subparsers.add_parser('add')
    add_subcommand.add_argument('description')

    update_subcommand = subparsers.add_parser('update')
    update_subcommand.add_argument('id', type=int)
    update_subcommand.add_argument('description')

    delete_subcommand = subparsers.add_parser('delete')
    delete_subcommand.add_argument('id', type=int)

    mark_subcommand = subparsers.add_parser('mark')
    mark_subcommand.add_argument('id', type=int)
    mark_subcommand.add_argument(
        'status',
        choices=['done', 'todo', 'in-progress'],
    )

    list_subcommand = subparsers.add_parser('list')
    list_subcommand.add_argument(
        'status',
        choices=['done', 'todo', 'in-progress'],
        nargs='?',
        default=None,
    )

    return parser


def _main_cli():
    parser = _construct_argparser()
    args = parser.parse_args()

    if 'id' in args and args.id not in database:
        print(f'Id does not exist in database: {args.id}')
        return

    match args.subcommand:
        case 'add':
            task = create_task(args.description)
            print(_format_task_message(task))

        case 'update':
            task = update_task(
                args.id,
                description=args.description,
            )
            print(_format_task_message(task))

        case 'delete':
            task = delete_task(args.id)
            print(_format_task_message(task))

        case 'mark':
            status = STATUS_MAP.get(args.status)
            task = update_task(args.id, status=status)
            print(_format_task_message(task))

        case 'list':
            status = args.status and STATUS_MAP.get(args.status)
            for task in list_tasks(filter_by_status=status):
                print(_format_task_message(task))

        case _:
            parser.print_help()

    save_database(database)


if __name__ == '__main__':
    _main_cli()
