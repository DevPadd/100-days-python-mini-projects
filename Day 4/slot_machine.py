import time
import random
from collections import Counter

def spin():
    spinned_items = [random.choice(("🍉","🍇","🍊","🍌")) for item in range(3)]
    
    print("=====================")
    for item in spinned_items:
        
        print(f"| {item} |",end=" ")
    print(" ")
    print("=====================")

    counts = Counter(spinned_items)
    for count in counts.values():
        if count == 3:
            print("🎊YOU WIN!!! $100 were added to your balance!🎊")
            return 100
    return -1

def main():
    print("------ Fruity Slots ------")
    print("symbols: 🍉🍇🍊🍌")
    print("price: 1$/spin")
    print("--------------------------")
    balance = int(input("how many balance would you like to start with: $"))

    while True:
        print(f"current balance: ${balance}")
        action = input("do you want to spin (y/n): ").lower()
        if action == "y" or action == "":
            if balance <= 0:
                print("cant spin anymore, your officially broke and bankrupt 🥲")
                break
            else:
                time.sleep(0.8)
                balance += spin()
        elif action == "n":
            print("thank you for playing!")
            break
        else:
            print("invalid command")




if __name__ == '__main__':
    main()