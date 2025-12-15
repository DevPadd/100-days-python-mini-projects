import random

print("--- welcome to number guessing game! ---")

a = int(input("type in minimum number: "))
b = int(input("type in maximum number: "))
attempt = 0

answer = random.randint(a,b)

while True:
    print(f"guess the number ranging from {a} to {b}")
    guess = input("type your guess: ")
    attempt +=1
    try:
        guess = int(guess)
        if guess == answer:
            print(f"correct! the answer is {answer}!")
            print(f"it took you {attempt} guesses to get it right.")
            break
        elif guess > answer:
            print("too high!")
            
        elif guess < answer:
            print("too low!")
    except:
        print("invalid guess")

