import argparse
from task_functions import TaskManager


parser = argparse.ArgumentParser(description="Task CLI App")

subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="Add new task")
add_parser.add_argument("description", help="Task description")

update_parser = subparsers.add_parser("update", help="Update task")
update_parser.add_argument("id", type=int, help="Id of task")
update_parser.add_argument("description", help="Task description")

delete_parser = subparsers.add_parser("delete", help="Delete task")
delete_parser.add_argument("id", type=int, help="Id of task")

mark_in_progress_parser = subparsers.add_parser("mark-in-progress")
mark_in_progress_parser.add_argument("id", type=int)

mark_done_parser = subparsers.add_parser("mark-done")
mark_done_parser.add_argument("id", type=int)

list_parser = subparsers.add_parser("list")
list_parser.add_argument(
    "status",
    nargs="?",
    choices=["todo","done","in-progress"]
)

args = parser.parse_args()

tm = TaskManager()

if args.command == "add":
    tm.add_task(args.description)
elif args.command == "update":
    tm.update_task(args.id, args.description)
elif args.command == "delete":
    tm.delete_task(args.id)
elif args.command == "mark-in-progress":
    tm.change_status_task(args.id, "in-progress")
elif args.command == "mark-done":
    tm.change_status_task(args.id, "done")
elif args.command == "list":
    tm.list_task(args.status)
