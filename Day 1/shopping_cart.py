# dictionary exercise: shopping cart
groceries = {
    "tomato":1.5,
    "cheese":2.2,
    "broccoli":2.5,
    "lemon":4.0,
    "watermelon": 6.3,
    "spinach":1.1,
    "onion":2.9,
    "tauge": 7.6,
    "milk": 6.7,
    "chili":4.6
    
}

my_cart = []
total = 0

print("___________________")
for key, value in groceries.items():
    print(f"{key}: ${value}")
print("___________________")


while True:
    added_item = input("put something to your cart (q to proceed to the cashier): ").lower()
    
    if added_item in groceries:
        my_cart.append(added_item)
        total+= groceries[added_item]
    else:
        print("the store doesnt have that unfortunately.")
    
    if added_item == "q":
        break

print("Your shopping cart")
for item in my_cart:
    print(f"- {item}")
print(f"your total price is ${total:.2f}") # format specifier