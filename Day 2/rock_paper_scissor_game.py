import random

options = ("rock","paper", "scissor")

print("Welcome to rock paper scissor game!")
computer_score = 0
user_score = 0

while True:
    computer_choice = random.choice(options)
    user_choice = input("choose between rock, paper, and scissor: ").lower()

    print(f"computer chooses {computer_choice}")

    if computer_choice == user_choice:
        print("its a draw!")
    
    elif user_choice == "rock" or user_choice =="paper" or user_choice == "scissor":
        
        if computer_choice == "paper":
            if user_choice == "scissor":
                print("user wins!")
                user_score+=1
            elif user_choice == "rock":
                print("computer wins!")
                computer_score+=1
        elif computer_choice == "rock":
            if user_choice == "scissor":
                print("computer wins!")
                computer_score += 1
            elif user_choice == "paper":
                print("user wins!")
                user_score+=1
        elif computer_choice == "scissor":
            if user_choice == "rock":
                print("user wins!")
                user_score += 1
            elif user_choice == "paper":
                print("computer wins!")
                computer_score+=1

    else:
        print("invalid guess!")

    print(f"{user_score}:{computer_score}")
    print("____________________________________")
    if user_score == 10 or computer_score == 10:
        print("max score reached, game ended")
        break






