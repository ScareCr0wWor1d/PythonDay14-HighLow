# HighLow Game

from art import logo, vs
from game_data import data
from random import choice
from os import system


def display(c1, c2):
    print(logo)
    print(f"Comparer A: {c1['name']}, {c1['description']}, {c1['country']}")
    print(vs)
    print(f"Comparer B: {c2['name']}, {c2['description']}, {c2['country']}")


def winning(choix, guess1, guess2):
    if guess1['follower_count'] > guess2['follower_count']:
        return choix == 'A'
    else:
        return choix == 'B'


win = True
score = 0
choix1 = choice(data)
while win:

    choix2 = choice(data)
    while choix1 == choix2:
        choix2 = choice(data)
    display(choix1, choix2)
    print(f"Score: {score}")
    selection = input("Qui a le plus de Followers? A ou B? ").upper()
    win = winning(selection, choix1, choix2)

    if win:
        score += 1
    else:
        win = False
    choix1 = choix2
    system('cls')

print(logo)
print(f"Votre score final est : {score}")
