#!/usr/bin/env python3

from random import choice

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
        """
        +--------+
        |
        |
        |
        |
        |
        |
       ===============
        """,
        """
        +--------+
        |        |
        |        O
        |
        |
        |
        |
       ===============
        """,
        """
        +--------+
        |        |
        |        O
        |        |
        |
        |
        |
       ===============
        """,
        """
        +--------+
        |        |
        |        O
        |       -|
        |
        |
        |
       ===============
        """,
        """
        +--------+
        |        |
        |        O
        |       -|-
        |
        |
        |
       ===============
        """,
        """
        +--------+
        |        |
        |        O
        |       -|-
        |       / 
        |
        |
       ===============
        """,
        """
        +--------+
        |        |
        |        O
        |       -|-
        |       / \\
        |
        |
       ===============
        """
    ]

    print(graphic[hangman])
    return

def start():
    print("Let's play a game of Machine Learning Hangman")
    while game():
        pass
    scores()

def game():
    dictionary = ["theta","linear_regression","svm","features","inference"]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while(letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print(letter," already picked!")
            else:
                letters_tried = letters_tried+letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong +=1
                    print(f"Sorry {letter} isn't what we're looking for.")
                else:
                    print(f"Congrats! {letter} is correct, keep going!")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("choose another...")
        hangedman(letters_wrong)
        print(" ".join(clue))
        print(f"Guesses: {letters_tried}")

        if letters_wrong == tries:
            print(f"Game over :/\n The word was {word}")
            computer_score += 1
            break
        if "".join(clue) == word:
            print(f"You win !\n The word was {word}")
            player_score += 1
            break
    return play_again()

def guess_letter():
    letter = input("Guess the word: ")
    letter.strip()
    letter.lower()
    return letter

def play_again():
    answer = input("Would you like to play again? y/n")
    if answer in ('Y','y','yes'):
        return answer
    else:
        print("Thank you for playing. To the next time!")

def scores():
    global player_score, computer_score
    print(f"Player: {player_score}\nComputer: {computer_score}")

if __name__=="__main__":
    start()
    