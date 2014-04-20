import Map
import Player
import Monsters
import Background
import select, tty, termios, sys, time
defaultTerminal = termios.tcgetattr(sys.stdin)


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
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (8, 8, description+"\n Que voulez vous faire?"))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (22,70,Player.getName()))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (23,67,str(Player.getHealth())))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (24,76,str(Player.getTime())))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (25,76,'500'))
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
    global defaultTerminal
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, defaultTerminal)
    sys.exit()
