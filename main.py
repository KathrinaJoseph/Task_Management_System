
from service.task_manager import TaskManager
from util.exceptions import *

def main():
    """
    Command-line interface (CLI) for managing tasks and users.

    Provides a simple text-based menu for performing the following operations:
    The menu will display, and the user can interact via standard input.
    """
    tm = TaskManager()

    while True:
        print("\nTask Management Menu:\n")
        print("1. Create User")
        print("2. Create Task")
        print("3. Assign Task to User")
        print("4. View All Tasks")
        print("5. View Tasks by User")
        print("6. View Tasks by Status")
        print("7. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                uid = input("User ID: ")
                name = input("Name: ")
                email = input("Email: ")
                tm.create_user(uid, name, email)

            elif choice == "2":
                tid = input("Task ID: ")
                title = input("Title: ")
                desc = input("Description: ")
                due = input("Due Date: ")
                priority = input("Priority (Low/Medium/High): ")
                tm.create_task(tid, title, desc, due, priority)

            elif choice == "3":
                tid = input("Task ID: ")
                uid = input("User ID: ")
                tm.assign_task_to_user(tid, uid)

            elif choice == "4":
                for task in tm.list_all_tasks():
                    print(task)

            elif choice == "5":
                uid = input("User ID: ")
                for task in tm.list_tasks_by_user(uid):
                    print(task)

            elif choice == "6":
                status = input("Enter status (To Do/In Progress/Done): ")
                for task in tm.list_tasks_by_status(status):
                    print(task)

            elif choice == "7":
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

        except TaskManagerException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"System Error: {e}")

if __name__ == "__main__":
    main()
