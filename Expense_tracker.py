expenses = []

print("Welcome to the expense tracker")

while True:
    print("\nMenu:")
    print("1.Add an expense")
    print("2.View Total expenses")
    print("3.Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        description = input("Enter the description of the expense: ")
        try:
            amount = float(input("Enter the amount of the expense: "))
            expenses.append({"description": description, "amount": amount})
            print(f"Expense '{description}' of amount {amount} added successfully!")
        except ValueError:
            print("Invalid amount entered")
     
    elif choice == '2':
        if not expenses:
            print("No expenses to show yet")
        else:
            print("\nExpenses:")
            total = 0
            for expense in expenses:
                print(f"{expense['description']} : ${expense['amount']:.2f}")
                total += expense['amount']
            print(f"Total: ${total:.2f}")

    elif choice == '3':
        print("Thank you for using the expense tracker")
        break
    else:
        print("This is not a valid choice")