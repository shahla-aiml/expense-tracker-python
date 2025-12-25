# Expense Tracker Project

expenses = []  # list to store expenses as dictionaries

print("Welcome to Expense Tracker")

while True:
    print("\n~~~~ MENU ~~~~")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total expense")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add expense
    if choice == 1:
        date = input("Enter the date: ")
        category = input("Enter the category (food, travel, stay, stationery): ")
        description = input("Enter description: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    # 2. View all expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\n--- Your Expenses ---")
            count = 1
            for eachexpense in expenses:
                print(
                    f"{count}. Date: {eachexpense['date']}, "
                    f"Category: {eachexpense['category']}, "
                    f"Description: {eachexpense['description']}, "
                    f"Amount: {eachexpense['amount']}"
                )
                count += 1

    # 3. View total expense
    elif choice == 3:
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            total = 0
            for eachexpense in expenses:
                total += eachexpense["amount"]
            print(f"Total expense amount: {total}")

    # 4. Exit
    elif choice == 4:
        print("Thank you for using Expense Tracker. Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")