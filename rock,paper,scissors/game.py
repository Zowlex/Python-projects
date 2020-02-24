#!/usr/bin/env python3

# Rock, paper, scissors game implementation in python

import random, time

rock = 1
paper = 2
scissors = 3

names = {rock:"Rock",
        paper:"Paper",
        scissors:"Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

def start():
    print("Let's play a game of Rock, Paper, Scissors!")
    while game():
        pass
    scores()

def game():
    player_choice = move()
    computer_choice = random.randint(1,3)
    result(player_choice, computer_choice)
    return play_again()

def move():
    while True:
        print
        player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move:")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Oops! wrong input. Please enter 1,2 or 3.")

def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    print(f"I threw {names[computer]} !")
    global player_score, computer_score
    if player == computer:
        print(" Tie game! ")
    else:
        if rules[player] == computer:
            print("You win !")
            player_score += 1
        else:
            print("Hahaha you lost!")
            computer_score += 1
def play_again():
    answer = input("Wanna rematch ? y/n:")
    if answer in ("y","Y",'yes','YES','yup'):
        return answer
    else:
        print("Thanks for playing. To the next time!")

def scores():
    global player_score, computer_score
    print('High scores')
    print('You: ', player_score)
    print('Me: ',computer_score)

if __name__ == "__main__":
    start()
