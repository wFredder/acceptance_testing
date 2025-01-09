class Task:
    def __init__(self, description, status="Pending"):
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        if not description:
            print("Task cannot be empty.")
            return
        self.tasks.append(Task(description))

    def list_tasks(self):
        if not self.tasks:
            print("The to-do list is empty.")
            return

        print("Tasks:")
        for task in self.tasks:
            print(f"- {task.description} ({task.status})")

    def mark_task_complete(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = "Completed"
                return
        print(f"Task '{description}' not found.")

    def clear_tasks(self):
        self.tasks = []
        print("To-do list cleared.")