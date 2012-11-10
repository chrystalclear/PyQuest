#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Angie
#
# Created:     09/11/2012
# Copyright:   (c) Angie 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from characters import Player, Enemy

BATTLE_CHOICES ={Attack: attack(), Items: pickItem}

ALL_DIALOGUES = {start : """You are an EECS major at the University of California at Berkeley, and you wake up on a desk after a long, restful nap.
                            Looking around, the room is empty; all that is around is you and your trusty laptop. What will you do?""",
                 battle: "START BATTLE"}
ALL_CHOICES = {start: {}}
GAME_END = False
win = False

def action():
    print(1)

def getenemy():
    return Enemy()

def battle(enemy = getenemy()):
    battle_end = False
    while not battle_end:

        if player.hp == 0 or enemy.hp == 0:
            battle_end = True
            if player.hp == 0:
                win = False
                GAME_END = True

class Map():
    def __init__():
        print(1)

def main():
    print(ALL_DIALOGUES[start])

    while not GAME_END:
        action()
        GAME_END = True

if __name__ == '__main__': main()