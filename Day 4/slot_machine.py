import time
import random
from collections import Counter

def spin():
    spinned_items = [random.choice(("🍉","🍇","🍊","🍌")) for item in range(3)]
    return spinned_items

def display(spin_result):
    print("=====================")
    for item in spin_result:
        print(f"| {item} |",end=" ")
    print(" ")
    print("=====================")

def get_payout(spinned_items, bet):
    counts = Counter(spinned_items).values()
    if 3 in counts:
        print(f"🎊YOU GOT 3 PERFECT MATCH!!! You got ${bet*10}🎊")
        return bet*10
    elif 2 in counts:
        print(f"🎊YOU GOT 2 MATCH!!! You got ${bet*2}🎊")
        return bet*2
    else:
        print("bad luck, try again")
        return 0

def main():
    print("------ Fruity Slots ------")
    print("symbols: 🍉🍇🍊🍌")
    print("--------------------------")
    balance = 50

    while True:
        print(f"current balance: ${balance}")

        if balance <=0:
            print("you cant bet anymore, you're out of balance!")
            break
        bet = int(input("how much do you want to bet: $"))
        if bet > balance:
            print("bet is bigger than current balance, try betting lower")
        elif bet<=0:
            print("you cant bet $0 or negative number!")
        else:
            balance -= bet
            print("spinning...\n")
            time.sleep(0.8)

            spin_result = spin()
            display(spin_result)
            balance += get_payout(spin_result, bet)

if __name__ == '__main__':
    main()