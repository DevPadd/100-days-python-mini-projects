def show_balance(balance):
    print(f"Your balance: ${balance}")

def deposit():
    amount = float(input("how much would you like to deposit: $"))
    if amount < 0:
        print("amount cannot be negative")
        input("continue...")
        return 0
    else:
        return amount
        

def withdraw(balance):
    amount = float(input("how much would you like to withdraw: $"))
    if amount < 0:
        print("amount cannot be negative")
        input("continue...")
        return 0
    elif amount > balance:
        print("amount is bigger than your current balance")
        input("continue...")
        return 0
    else:
        return amount


def main():
    
    balance = 0
    is_running = True

    while is_running:
        print("----- Banking Program -----")
        print("1. show balance")
        print("2. deposit")
        print("3. withdrawal")
        print("4. exit")
        print("---------------------------")
        action = input("enter command choice (1-4): ")

        match action:
            case "1":
                show_balance(balance)
                input("continue...")
            case '2':
                balance += deposit()
            case "3":
                balance -= withdraw(balance) 
            case "4":
                print("program exited")
                is_running = False
            case _:
                print("invalid command")
                input("continue...")

if __name__ == "__main__":
    main()


