# create an empty list to store the tasks and their status
todo_list = []

# Function to add a new task
def add_task():
    task = input("enter a task:")
    todo_list.append({"Task": task,"status":"pending"})
    print("A new task added Successfully!")
# Function to view all task
def view_task():
    print("your do list:")
    if len(todo_list) == 0:
        print("no printing tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}:{task} - {task['status']}")
    print("\n")

# function remove task
def remove_task():
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
           search_index = int(input("enter the task number that you want to remove:")) - 1
           if 0 <=search_index < len(todo_list):
               remove_task = todo_list.pop(search_index)
               print(f"task removed:{remove_task['Task']}")
           else:
               print("Invalid Task Number.")
        except ValueError:
            print("Please Enter a Valid Task Number.")

# function for mark_done

def mark_done ():
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
           search_index = int(input("enter the task number that you want to as complete:")) - 1
           if 0 <=search_index < len(todo_list):
              todo_list[search_index]['status'] = 'done'
              print(f"task to list[search_index][task] hasbeen marked as done!")
           else:
               print("Invalid Task Number.")
        except ValueError:
            print("Please Enter a Valid Task Number.")
def menu():
    while(True):
        print("****Main Menu****")
        print("1. Add a new task")
        print("2. view all task")
        print("3. Remove a task")
        print("4. Mark a task as Completed")
        print("5. exit")

        choice = input("Enter your choice:")
        if choice == "1":
          add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application...")
            exit()
        else:
            print("Invalid choice! try again!")
menu()
