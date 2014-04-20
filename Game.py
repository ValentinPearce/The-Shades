import Map
import Player
import Monsters
import Background
import select, tty, termios, sys, time


def init():
    global descript, myBackground
    myBackground=Background.create("background","victoire","defaite","menu")
    Background.show(myBackground,"menu")
    Player.setName()
    Player.setHealth()
    Map.generate()
    descript = descript()
    tty.setcbreak(sys.stdin.fileno())
    return descript
def checkHealth():
    if Player.getHealth()<= 0:
	lose()
        exitGame()

def descript():
    return  Map.getDescript(Player.getPosition())

def altDescript():
    return Map.getAltDescript(Player.getPosition())

def move(direction):
    answer = Map.checkDirection(Player.getPosition(),direction)
    if answer == 0:
	return 'Il y a un mur dans cette direction'
    elif answer == 1 :
        Player.move(direction)
        Player.editTime(10)
        return Map.getDescript(Player.getPosition())
    else :
        win()
        exitGame()

def isInput():
   return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def win():
    Background.show(myBackground,"win")	
  
def lose():
    Background.show(myBackground,"lose")

def display(description):
    Background.show(myBackground,"bg")
    sys.stdout.write("\033[43;9H\n")
    sys.stdout.write(description+"\n Que voulez vous faire?")
    sys.stdout.write("\033[95;27H\n")
    sys.stdout.write(Player.getName())
    sys.stdout.write("\033[92;28H\n")
    sys.stdout.write(str(Player.getHealth()))
    sys.stdout.write("\033[101;29H\n")
    sys.stdout.write(str(Player.getTime()))
    sys.stdout.write("\033[101;30H\n")
    sys.stdout.write('500')
    sys.stdout.flush()
    #affichage des commandes et de la description
    
def getAction():
    while 1:
        if isInput():
            key = sys.stdin.read(1)
            if key == 'z' :
                return move('north')
            elif key == 'q' :
                return move('west')
            elif key == 's' :
                return move('south')
            elif key == 'd' :
                return move('east')
            elif key == 'o' :
                return altDescript()
            elif key == '\x1b' :
                exitGame()
            time.sleep(0.2)	
def checkTime():
    if (Player.getTime()>500):
        lose()
        exitGame()
def exitGame():
    sys.exit()
