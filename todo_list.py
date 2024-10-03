import json
import os

class TodoList:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.load_todos()

    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.todos = json.load(f)
        else:
            self.todos = []

    def save_todos(self):
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=4)

    def add_task(self, task):
        self.todos.append(task)
        self.save_todos()
        print(f'Task added: "{task}"')

    def view_tasks(self):
        if not self.todos:
            print("No tasks found.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.todos, start=1):
                print(f"{index}. {task}")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.todos):
            removed_task = self.todos.pop(task_index - 1)
            self.save_todos()
            print(f'Task removed: "{removed_task}"')
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
