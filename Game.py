import Map
import Player
import Monsters
import Background
import select, tty, termios, sys, time
defaultTerminal = termios.tcgetattr(sys.stdin)


def init(): # Defini les variables de depart
    global descript, myBackground
    myBackground=Background.create("background","victoire","defaite","menu")
    Background.show(myBackground,"menu")
    Player.setName()
    Player.setHealth()
    Map.generate(6)
    descript = descript()
    tty.setcbreak(sys.stdin.fileno())
    return descript

def checkHealth(): # Verifie si le joueur est vivant
    if Player.getHealth()<= 0:
	lose()
        exitGame()

def descript(): # Recupere la description de base de la zone active
    return  Map.getDescript(Player.getPosition())

def altDescript(): # Recupere la description avancee de la zone active
    return Map.getAltDescript(Player.getPosition())

def move(direction): # Deplace le joueur si possible
    answer = Map.check(Player.getPosition(),direction)
    if answer == 0:
	return 'Il y a un mur dans cette direction'
    elif answer == 1 :
        Player.move(direction)
        Player.editTime(10)
        return Map.getDescript(Player.getPosition())
    else :
        win()
        exitGame()

def isInput(): # Recupere les actions du clavier
   return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def win(): # Affiche l'ecran de victoire
    Background.show(myBackground,"win")	
  
def lose(): # Affiche l'ecran de defaite
    Background.show(myBackground,"lose")

def display(description): # Affiche la description correspondant a la derniere action effectuee
    Background.show(myBackground,"bg")
    description = description.split()
    descript = [""]
    word, line = 0, 0
    while word < len(description):
        if len(descript[line]) + len(description[word]) + 1 < 27:
            descript[line] += " " + description[word]
            word += 1
        elif word < len(description):
            descript.append("")
            line +=1
    for line in range (len(descript)):
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (6+line, 10, descript[line]))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (22,70,Player.getName()))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (23,67,str(Player.getHealth())))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (24,76,str(Player.getTime())))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (25,76,'500'))
    sys.stdout.flush()
    
def getAction(): # Traite les interactions clavier
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

def checkTime(): # Verifie si le joueur est considere comme perdu a jamais
    if (Player.getTime()>500):
        lose()
        exitGame()

def exitGame(): # Quitte le jeu en remettant les parametres par defaut
    global defaultTerminal
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, defaultTerminal)
    sys.exit()


