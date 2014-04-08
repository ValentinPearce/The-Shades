import Map
import Player
import Monsters

def init():
    global descript
    Player.setName()
    Player.setHealth()
    Map.generate()
    descript = descript()

def checkHealth():
    if Player.getHealth()<= 0:
	lose()

def descript():
    Map.getDescript(Player.getPosition())

def altDescript():
    Map.getAltDescript(Player.getPosition())

def move(direction):
    answer = Map.checkDirection(Player.getPosition(),direction)
    if answer == 0:
	descript = 'Il y a un mur dans cette direction'
    elif answer == 1 :
        Player.move(direction)
        descript = Map.getDescript(Player.getPosition,description)
    else :
        win()
    Player.editTime(-10)
def win():
    print 'bob'
  
def lose():
    print 'bob'

def display(description):
    print 'bob'
    
def getAction():
    print 'bob'
    
