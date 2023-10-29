import heapq
import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_date, time, category, priority):
        heapq.heappush(self.tasks, (due_date, time, task, category, priority, False))

    def remove_task(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid index.")
            return
        del self.tasks[index-1]
        heapq.heapify(self.tasks)

    def edit_task(self, index, new_task, new_due_date, new_time, new_category, new_priority):
        if index < 1 or index > len(self.tasks):
            print("Invalid index.")
            return
        _, _, _, _, _, is_completed = self.tasks[index-1]
        self.tasks[index-1] = (new_due_date, new_time, new_task, new_category, new_priority, is_completed)
        heapq.heapify(self.tasks)

    def complete_task(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid index.")
            return
        due_date, time, task, category, priority, _ = self.tasks[index-1]
        self.tasks[index-1] = (due_date, time, task, category, priority, True)
        heapq.heapify(self.tasks)

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\nTasks in To-Do List:")
        for idx, (due_date, time, task, category, priority, is_completed) in enumerate(self.tasks, 1):
            status = "Completed" if is_completed else "Pending"
            print(f"{idx}. {task} - Due: {due_date} at {time} - Category: {category} - Priority: {priority} - Status: {status}")

    def remind(self):
        now = datetime.datetime.now()
        current_date = now.strftime("%m-%d-%Y")
        current_time = now.strftime("%H:%M")
        for due_date, time, task, _, _, is_completed in self.tasks:
            if is_completed:
                continue
            if due_date == current_date and time <= current_time:
                print(f"Reminder: You have a task due! {task} is due today at {time}.")

def get_user_input(prompt):
    return input(prompt)

def main():
    print("Welcome, student!")
    print("This is your School To-Do List Manager.")

    todo = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Edit Task")
        print("4. Complete Task")
        print("5. View Tasks")
        print("6. Remind")
        print("7. Exit")

        choice = get_user_input("\nChoose an option: ")

        if choice == '1':
            task = get_user_input("Enter the task/event: ")
            due_date = get_user_input("Enter the due date (MM-DD-YYYY): ")
            time = get_user_input("Enter the time in military format (HH:MM): ")
            category = get_user_input("Enter the category (Homework, Exam, Personal, etc.): ")
            priority = get_user_input("Enter the priority (High, Medium, Low): ")
            todo.add_task(task, due_date, time, category, priority)
        elif choice == '2':
            todo.view_tasks()
            index = int(get_user_input("Enter the index of the task to remove: "))
            todo.remove_task(index)
        elif choice == '3':
            todo.view_tasks()
            index = int(get_user_input("Enter the index of the task to edit: "))
            new_task = get_user_input("Enter the new task/event: ")
            new_due_date = get_user_input("Enter the new due date (MM-DD-YYYY): ")
            new_time = get_user_input("Enter the new time in military format (HH:MM): ")
            new_category = get_user_input("Enter the new category: ")
            new_priority = get_user_input("Enter the new priority: ")
            todo.edit_task(index, new_task, new_due_date, new_time, new_category, new_priority)
        elif choice == '4':
            todo.view_tasks()
            index = int(get_user_input("Enter the index of the task to mark as completed: "))
            todo.complete_task(index)
        elif choice == '5':
            todo.view_tasks()
        elif choice == '6':
            todo.remind()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
