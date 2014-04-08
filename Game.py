import Map.py
import Player.py
import Monsters.py

def init():
def checkHealth():
def descript():
def altDescript():
def move(direction):
    position = Player.getPosition()
    answer = Map.checkDirection(position,direction)
    if answer == 0:
	descript = 'Il y a un mur dans cette direction'
    elif answer == 1 :
        Player.move(direction)
        Player.getPosition()
        descript = Map.getDescript(position,description)
    else :
        win()
