import random
import time

# dice text art
# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: (
    "┌─────────┐",
    "│         │",
    "│    ●    │",
    "│         │",
    "└─────────┘"
    ),
    2: (
    "┌─────────┐",
    "│         │",
    "│  ●   ●  │",
    "│         │",
    "└─────────┘"
    ),
    3: (
    "┌─────────┐",
    "│    ●    │",
    "│         │",
    "│  ●   ●  │",
    "└─────────┘"
    ),
    4: (
    "┌─────────┐",
    "│  ●   ●  │",
    "│         │",
    "│  ●   ●  │",
    "└─────────┘"
    ),
    5: (
    "┌─────────┐",
    "│  ●   ●  │",
    "│    ●    │",
    "│  ●   ●  │",
    "└─────────┘"
    ),
    6: (
    "┌─────────┐",
    "│ ●  ●  ● │",
    "│         │",
    "│ ●  ●  ● │",
    "└─────────┘"
    )
}
total = 0
rolled = []

number_of_dice = int(input("how many number of dices you want to roll: "))

for roll in range(number_of_dice):
    rolled.append(random.randint(1,6))
    

for line in range(5):
    for die in rolled:
        print(dice_art.get(die)[line], end="")
    print("")

for dice_side in rolled:
    total+=dice_side

print(f"total: {total}")

# print(f"total: {total}")