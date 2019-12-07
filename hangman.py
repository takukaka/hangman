# Challenge 10_01

import random

def hangman():
    answers = ["cat", "doc", "boy", "girl"]
    numbers = len(answers)
    choice = random.randint(0,numbers)
    word = answers[choice]
    wrong = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You won!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose. The answer is {}.".format(word))

answers = ["cat", "doc", "boy", "girl"]
numbers = len(answers)
choice = random.randint(0,numbers)

hangman()
