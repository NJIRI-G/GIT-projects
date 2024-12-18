def show_balance():
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to be deposited: "))

    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient funds")
    elif amount < 0:
        print("Amount must be greater than 0")
    else:
        return amount
    


balance  = 0 
is_running = True

while is_running :
    print("Banking program")
    print("1.show balance")
    print("2.Deposit")
    print("3.withdraw")
    print("4.Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("This is not a valid choice")


print("Thank you for banking with us")