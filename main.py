from argparse import ArgumentParser

from tasks import read_tasks, update_tasks

tasks = read_tasks()

parser = ArgumentParser(description='Clock')
parser.add_argument('command', type=str, help='Clock in or clock out; Manage tasks; Sync data.', choices=['in', 'out', 'task', 'sync'])
parser.add_argument('task', type=str, help="Name of your current task")
parser.add_argument('-c', '--create', action='store_true', help="Flag to create something in the context of current command.")
parser.add_argument('-d', '--delete', action='store_true', help="Flag to delete something in the context of current command.")
parser.add_argument('-v', '--verbose', action='store_true', help="Prints more information.")
args = parser.parse_args()

if args.command == 'task':
    if args.create:
        if args.task in tasks:
            raise Exception(f"{args.task} is already listed as a task")
        tasks.add(args.task)
        update_tasks(tasks)
    if args.delete:
        if args.task not in tasks:
            raise Exception(f"{args.task} is not listed as a task")
        tasks = set((filter(lambda x: x != args.task, tasks)))
        update_tasks(tasks)
    