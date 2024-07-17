import random
import time
word_list = ["apple", "green", "white", "broad", "gases"]
answer= random.choice(word_list)
def print_menu():
    print("let's play wordle!")
    print("Guess the 5 letter word")
def guess_word(answer, guess):
    clue = ""
    for i, letter in enumerate(guess):
        if letter == answer[i]:
            clue += "G"
        elif letter in answer:
            clue += "Y"
        else:
            clue += "-"
    return clue
print_menu()
for x in range(1,6):
    guess = input("Type a 5 letter word and hit enter: ")
    print(guess_word(answer, guess))
    if guess == answer:
        time.sleep(1)
        print("Congrats, You Win!")
        break
    elif x==5 and guess != answer:
        time.sleep(1)
        print("Damn, You lose. WOMP WOMP")
        break
    if len(guess)>5:
        print("that was too large, you lose a guess")
    elif len(guess)<5:
        print("that was too small, you lose a guess")
    else:
        continue







