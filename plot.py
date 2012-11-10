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

class Player():
    def __init__():
        self.hp = 100

class Enemy():
    def __init__():
        self.hp = 100


GAME_END = False
win = False

def main():
    print(ALL_DIALOGUES[start])

    while not GAME_END:
        action()

if __name__ == '__main__': main()

def action():

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
    end



BATTLE_CHOICES ={Attack: attack(), Items: pickItem}

ALL_DIALOGUES = {start : """You are an EECS major at the University of California at Berkeley, and you wake up on a desk after a long, restful nap.
                            Looking around, the room is empty; all that is around is you and your trusty laptop. What will you do?""",
                 battle: "START BATTLE"}
ALL_CHOICES = {start: {}}





class Map():
    def __init__()