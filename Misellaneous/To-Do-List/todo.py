import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, file_name):
        self.file_name = file_name
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def view_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            status = "Done" if task["done"] else "Pending"
            due_date = task["due_date"] if task["due_date"] else "None"
            print(f"{task['id']}. {task['name']} (Due: {due_date}, Status: {status}, Priority: {task['priority']}, Category: {task['category']})")

    def add_task(self):
        task_name = input("Enter task name: ")
        due_date = input("Enter due date (YYYY-MM-DD, optional): ")
        due_date = due_date if due_date else None
        priority = input("Enter priority (High/Medium/Low): ")
        category = input("Enter category (Work/Personal): ")
        new_task = {
            "id": len(self.tasks) + 1,
            "name": task_name,
            "due_date": due_date,
            "done": False,
            "priority": priority,
            "category": category
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully!")

    def delete_task(self):
        task_id = int(input("Enter task ID to delete: "))
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted successfully!")
                return
        print("Task not found.")

    def mark_done(self):
        task_id = int(input("Enter task ID to mark as done: "))
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                self.save_tasks()
                print("Task marked as done!")
                return
        print("Task not found.")

    def sort_tasks(self):
        print("Sort by:")
        print("1. Due Date")
        print("2. Priority")
        print("3. Category")
        choice = input("Choose an option: ")
        if choice == "1":
            self.tasks.sort(key=lambda x: x['due_date'] if x['due_date'] else '')
        elif choice == "2":
            self.tasks.sort(key=lambda x: x['priority'])
        elif choice == "3":
            self.tasks.sort(key=lambda x: x['category'])
        self.save_tasks()
        self.view_tasks()

    def search_tasks(self):
        keyword = input("Enter search keyword: ")
        found_tasks = [task for task in self.tasks if keyword.lower() in task['name'].lower()]
        if found_tasks:
            print("Search results:")
            for task in found_tasks:
                status = "Done" if task["done"] else "Pending"
                due_date = task["due_date"] if task["due_date"] else "None"
                print(f"{task['id']}. {task['name']} (Due: {due_date}, Status: {status}, Priority: {task['priority']}, Category: {task['category']})")
        else:
            print("No tasks found.")


def main():
    todo = TodoList('tasks.json')
    
    while True:
        print("\nTodo List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Sort Tasks")
        print("6. Search Tasks")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            todo.view_tasks()
        elif choice == "2":
            todo.add_task()
        elif choice == "3":
            todo.delete_task()
        elif choice == "4":
            todo.mark_done()
        elif choice == "5":
            todo.sort_tasks()
        elif choice == "6":
            todo.search_tasks()
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()