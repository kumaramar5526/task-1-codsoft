class TodoItem:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TodoList:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        print("Item added to the to-do list.")
        
    def view_items(self):
        if not self.items:
            print("To-do list is empty.")
        else:
            print("\nTo-Do List:")
            for index, item in enumerate(self.items, start=1):
                status = "✓" if item.completed else " "
                print(f"{index}. [{status}] {item.description}")
    
    def mark_completed(self, index):
        if 0 < index <= len(self.items):
            self.items[index - 1].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")
    
    def delete_item(self, index):
        if 0 < index <= len(self.items):
            deleted_item = self.items.pop(index - 1)
            print(f"Task '{deleted_item.description}' deleted.")
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            new_item = TodoItem(description)
            todo_list.add_item(new_item)
        elif choice == "2":
            todo_list.view_items()
        elif choice == "3":
            index = int(input("Enter index of task to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == "4":
            index = int(input("Enter index of task to delete: "))
            todo_list.delete_item(index)
        elif choice == "5":
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
