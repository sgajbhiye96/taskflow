# main.py

import argparse
from manager import TaskManager

def main():
    parser = argparse.ArgumentParser(description="📋 TaskFlow - Command Line Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add Task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument("--priority", default="medium", choices=["low", "medium", "high"], help="Priority level")

    # List Tasks
    subparsers.add_parser("list", help="List all tasks")

    # Delete Task
    delete_parser = subparsers.add_parser("delete", help="Delete a task by ID")
    delete_parser.add_argument("id", help="Task ID")

    # Update Task
    update_parser = subparsers.add_parser("update", help="Update task status or priority")
    update_parser.add_argument("id", help="Task ID")
    update_parser.add_argument("--status", choices=["pending", "completed"], help="Update task status")
    update_parser.add_argument("--priority", choices=["low", "medium", "high"], help="Update task priority")

    # Search Tasks
    search_parser = subparsers.add_parser("search", help="Search tasks by keyword")
    search_parser.add_argument("keyword", help="Keyword to search for in task titles")

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add":
        manager.add_task(args.title, args.priority)
    elif args.command == "list":
        manager.list_tasks()
    elif args.command == "delete":
        manager.delete_task(args.id)
    elif args.command == "update":
        manager.update_task(args.id, args.status, args.priority)
    elif args.command
