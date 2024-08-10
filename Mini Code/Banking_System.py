def show_balance(balance):
    print (f"------------------------")
    print(f"Your balance is {balance:.2f}")

def deposit():
    amount = float(input("Enter the amount you want to deposit: "))
    if amount < 0:
        print (f"------------------------")
        print(f"Amount might be greater than 0")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input(f"Enter the amount you want to withdraw: "))
    if amount <= 0:
        print (f"------------------------")
        print (f"Amount might be greater than 0")
        return 0
    elif amount > balance :
        print (f"------------------------")
        print (f"Insufficient balance")
    else :
        return amount


def main():
    balance = 0
    is_running = True
    while(is_running):
        print (f"------------------------")
        print("1. Check Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")
        print (f"------------------------")
        choice = input("Enter the number between (1 to 4): ")
        
        if(choice == "1"):
            show_balance(balance)
        elif(choice == "2"):
            balance += deposit()
        elif(choice == "3"):
            balance -= withdraw(balance)
        elif(choice == "4"):
            is_running = False
            print("Thank you. Have a great day!")
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()