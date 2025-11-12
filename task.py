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

mark_done_parser = subparsers.add_parser("mark-done-progress")
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
    
