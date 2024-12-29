from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_date=None, priority='Low'):
        self.tasks.append({'task': task, 'due_date': due_date, 'priority': priority})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks, 1):
            due_date = task['due_date'] if task['due_date'] else 'No due date'
            completed_status = 'Completed' if task.get('completed') else 'Not completed'
            print(f"{i}. {task['task']} (Due: {due_date}, Priority: {task['priority']}, Status: {completed_status})")

    def delete_task(self, task_index):
        try:
            task = self.tasks.pop(task_index - 1)
            print(f"Task '{task['task']}' deleted.")
        except IndexError:
            print("Invalid task index.")

    def complete_task(self, task_index):
        try:
            task = self.tasks[task_index - 1]
            task['completed'] = True
            print(f"Task '{task['task']}' completed.")
        except IndexError:
            print("Invalid task index.")

    def filter_tasks(self, priority=None, completed=None):
        filtered_tasks = self.tasks
        if priority:
            filtered_tasks = [task for task in filtered_tasks if task['priority'] == priority]
        if completed is not None:
            filtered_tasks = [task for task in filtered_tasks if task.get('completed') == completed]
        return filtered_tasks


def main():
    todo = TodoList()

    todo.add_task("Buy milk", "2024-11-15", "High")
    todo.add_task("Walk the dog", "2024-11-12", "Medium")
    todo.add_task("Do laundry")
    todo.add_task("Clean the house", "2024-11-20", "Low")
    todo.add_task("Prepare dinner", "2024-11-10", "High")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. Filter Tasks")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High/Medium/Low): ")
            todo.add_task(task, due_date, priority)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to delete: "))
            todo.delete_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to complete: "))
            todo.complete_task(task_index)
        elif choice == "5":
            priority = input("Filter by priority (High/Medium/Low/All): ")
            completed = input("Filter by completion (Yes/No/All): ")
            priority = None if priority.lower() == 'all' else priority
            completed = None if completed.lower() == 'all' else completed.lower() == 'yes'
            tasks = todo.filter_tasks(priority, completed)
            for i, task in enumerate(tasks, 1):
                due_date = task['due_date'] if task['due_date'] else 'No due date'
                completed_status = 'Completed' if task.get('completed') else 'Not completed'
                print(f"{i}. {task['task']} (Due: {due_date}, Priority: {task['priority']}, Status: {completed_status})")
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()