import Map
import Player
import Monsters
import Background
import select, tty, termios, sys
description = ' '

def init():
    global descript, myBackground
    Player.setName()
    Player.setHealth()
    Map.generate()
    descript = descript()
    myBackground=Background.create("background","victoire","defaite","menu")
    Background.show(myBackground,"menu")
    return descript
def checkHealth():
    if Player.getHealth()<= 0:
	lose()

def descript():
    global description
    description = Map.getDescript(Player.getPosition())

def altDescript():
    global description
    description = Map.getAltDescript(Player.getPosition())

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
    return descript

def isInput():
   return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def win():
    Background.show(myBackground,"win")	
  
def lose():
    Background.show(myBackground,"lose")

def display(description):
    Background.show(myBackground,"bg")
    sys.stdout.write("\033[9;43\n")
    sys.stdout.write(descritption)
    #affichage des commandes et de la description
    
def getAction():
    if isInput():
        key = sys.stdin.read(1)
        if key == 'z' :
           decript = move('north')
        if key == 'q' :
           descript = move('west')
        if key == 's' :
           descrit = move('south')
        if key == 'd' :
           descript = move('east')
        if key == 'o' :
           descript = altDescript()
        if key == '\x1b' :
            exitGame()
    
def checkTime():
    if (Player.getTime()>180):
        lose()
def exitGame():
    sys.exit()
