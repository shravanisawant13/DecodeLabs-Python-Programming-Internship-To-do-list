tasks = []

while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Python")
    print("2. SQL")
    print("3. Tableau")
    print("4. Power BI")

    choice = input("Enter your choice: ")

    if choice == "1":

        task = input("Enter your task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            count = 1

            for task in tasks:
                print(str(count) + ". " + task)
                count += 1

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available.")

        else:

            print("\nYour Tasks:")

            count = 1

            for task in tasks:
                print(str(count) + ". " + task)
                count += 1

            delete = int(input("Enter task number to delete: "))

            if delete >= 1 and delete <= len(tasks):

                removed_task = tasks.pop(delete - 1)

                print(removed_task + " deleted successfully!")

            else:

                print("Invalid task number.")

    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")