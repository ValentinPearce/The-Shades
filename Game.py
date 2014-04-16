import Map
import Player
import Monsters
import Background

description = ' '

def init():
    global descript, myBackground
    Player.setName()
    Player.setHealth()
    Map.generate()
    descript = descript()
    myBackground=Background.create("background","victoire","defaite")

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

def win():
    Background.show(myBackground,"win")
  
def lose():
    Background.show(myBackground,"lose")

def display(description):
    Background.show(myBackground,"bg")
    #affichage des commandes et de la description
    
def getAction():
    print 'bob'
    
def checkTime():
    if (Player.getTime()>180):
        lose()
