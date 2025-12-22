import random
import time
import wordlist


hangman = {
        0: '''
    +---+
    |   |
        |
        |
        |
        |
    =========''',
    1:'''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', 
    2: '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', 
    3: '''
     +---+
     |   |
     O   |
   --|   |
         |
         |
    =========''', 
    4:'''
     +---+
     |   |
     O   |
   --|-- |
         |
         |
    =========''', 
    5:'''
     +---+
     |   |
     O   |
   --|-- |
    |    |
         |
    =========''', 
    6:'''
     +---+
     |   |
     O   |
   --|-- |
    | |  |
         |
    ========='''
}
# credit for art: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

def display_hangman(stage):
    print(hangman[stage])

def display_hint(hint):
    for i in hint:
        print(i, end=" ")
    print("")

def display_answer(answer, example_sentence, win_lose):
    print("-------------------------------------------------------")
    if win_lose == "win":
        print("🎊You saved the man, Hooray!🎊")
    else: 
        print("💀Damn, Too bad, he got hanged!💀")
    
    print(f"Answer: {answer}")
    print(f"Example usage: {example_sentence}")
    print("-------------------------------------------------------")

def main():
    # initial
    random_index = wordlist.words.index(random.choice(wordlist.words))
    answer = wordlist.words[random_index]
    clue = wordlist.meanings[random_index]
    example_sentence = wordlist.example_sentences[random_index]
    hint = []
    stage = 0
    # assign blank _'s to hint
    for i in range(len(answer)):
        hint.append("_")
    play_again = "True"

    print("------ 📑Welcome to Hangman: SAT Vocab Edition📑 ------")

    while True:
        display_hangman(stage)
        display_hint(hint) 
        print(clue)


        guess = input("Guess a letter (or a full word!): ").lower()
        time.sleep(0.5)

        if guess in answer and len(guess) == 1:
                letter_indexes = [index for index, element in enumerate(answer) if element == guess]
                for letter_index in letter_indexes:
                    hint[letter_index] = guess
            
        elif guess == "quit":
            break
        else:
            stage+=1

        if answer == ''.join(hint) or guess == answer:
            hint == answer
            display_hint(hint)
            display_answer(answer, example_sentence, "win")
            break
        if stage == 6: 
            display_hangman(stage)
            display_answer(answer, example_sentence, "lose")
            break


if __name__ == "__main__":
    main()