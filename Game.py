import Map
import Player
import Monsters
import Background
import select, tty, termios, sys, time, random
defaultTerminal = termios.tcgetattr(sys.stdin)
items = 0
pick = 0
throw = 0
use = 0

def init(): # Defini les variables de depart
    global descript, myBackground
    myBackground=Background.create("background","victoire","defaite","menu")
    Background.show(myBackground,"menu")
    Player.setName()
    Player.setHealth()
    Player.setPower()
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
    if Map.isMonster() == 0:
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
    else:
        Player.editHealth(-1)
        return "Votre adversaire vous attrappe par le col et frappe a l'estomac. Battez-vous que diable!"
         

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
        if len(descript[line]) + len(description[word]) + 1 <= 27:
            descript[line] += " " + description[word]
            word += 1
        elif word < len(description):
            descript.append("")
            line +=1
    for line in range (len(descript)):
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (6+line, 10, descript[line]))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (22,70,Player.getName()))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (23,67,str(Player.getHealth())))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (23,78,str(Player.getPower())))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (24,76,str(Player.getTime())))
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (25,76,'500'))
    sys.stdout.flush()
    
def getAction(): # Traite les interactions clavier
    global items, pick, throw, use
    while 1:
        if isInput():
            key = sys.stdin.read(1)
            if key == '1' :
                if pick == 1:
                    return pickItem(Player.getPosition(),0)
                elif throw == 1:
                    return throwItem(Player.getPosition(),0)
                elif use == 1:
                    return useItem(0)
            elif key == '2' :
                if pick == 1:
                    return pickItem(Player.getPosition(),1)
                elif throw == 1:
                    return throwItem(Player.getPosition(),1)
                elif use == 1:
                    return useItem(1)
            elif key == '3' :
                if pick == 1:
                    return pickItem(Player.getPosition(),2)
                elif throw == 1:
                    return throwItem(Player.getPosition(),2)
                elif use == 1:
                    return useItem(2)
            elif key == '4' :
                if pick == 1:
                    return pickItem(Player.getPosition(),3)
                elif throw == 1:
                    return throwItem(Player.getPosition(),3)
                elif use == 1:
                    return useItem(3)
            elif key == '5' :
                if pick == 1:
                    return pickItem(Player.getPosition(),4)
                elif throw == 1:
                    return throwItem(Player.getPosition(),4)
                elif use == 1:
                    return useItem(4)
            elif key == 'z' :
                return move('north')
            elif key == 'q' :
                return move('west')
            elif key == 's' :
                return move('south')
            elif key == 'd' :
                return move('east')
            elif key == 'o' :
                return altDescript()
            elif key == 'r' :
                return pickList()
            elif key == 'j' :
                return throwList()
            elif key == 'e' :
                return useList()
            elif key == 'a' :
                return attack()
            elif key == '\x1b' :
                exitGame()
            time.sleep(0.2)	

def checkTime(): # Verifie si le joueur est considere comme perdu a jamais
    if (Player.getTime()>500):
        lose()
        exitGame()

def pickList():
    global items, throw
    items = Map.isItem(Player.getPosition())
    if items == 0:
        return "Il n'y a pas d'objets dans cette zone."
    else:
        pick = 1
        return "Quel objet voulez-vous ramasser? (Tapez le numero correspondant) ~~~~~~~~~~~~~~~~~~~~~~~~~~ " + Map.getItemList(Player.getPosition())

def pickItem(position,index):
    Player.addItem(Map.getItem(position,index))
    descript = "Vous ramassez " + Map.getItemName(position,index)
    Map.removeItem(position,index)
    return descript

def throwList():
    global items, throw
    items = Player.isItem()
    if items == 0:
        return "Vous n'avez pas d'objets dans votre inventaire."
    else:
        throw = 1
        return "Quel objet voulez-vous jeter? (Tapez le numero correspondant) ~~~~~~~~~~~~~~~~~~~~~~~~~~ " + Player.getItemList()

def throwItem(position,index):
    Map.addItem(position,Player.getItem(index))
    descript = "Vous jetez " + Player.getItemName(index)
    Player.removeItem(index)
    return descript

def useList():
    global items, use
    items = Player.isItem()
    if items == 0:
        return "Vous n'avez pas d'objets dans votre inventaire."
    else:
        use = 1
        return "Quel objet voulez-vous utiliser? (Tapez le numero correspondant) ~~~~~~~~~~~~~~~~~~~~~~~~~~ " + Player.getItemList()

def useItem(index):
    item = Player.getItem(index)
    if item["type"] == 1:
        Player.equxip(item)
    else:
        Player.editHealth(item["Modifier"])
    Player.removeItem(index)

def attack():
    if Map.isMonster(Player.getPosition()) == 1:
        playerPow = Player.getPower()
        monsterPow = Map.getMonsterPower(Player.getPosition())
        player1, player2, monster1, monster2 = random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)
        if Player.isEquip() == 1:
            equipPow = Player.getModifier()
        else:
            equipPow = 0
        descript = "Vous chargez tous les deux."
        if playerPow+player1+player2+equipPow >= monsterPow+monster1+monster2:
            Map.editMonsterHealth(Player.getPosition(),-2)
            descript += "Vous blessez votre adversaire."
        else:
            Player.editHealth(-2)
            descript += "Votre adversaire vous blesse."
        if Map.getMonsterHealth(Player.getPosition()) <= 0:
            descript += "CE coup lui est fatal. Son corps tombe tel un pantin desarticule et, quelques secondes plus tard, il se desintegre." 
            Map.removeMonster(Player.getPosition())
    else :
        descript = "Qui voulez-vous attaquer dites-moi? Les murs?"
    return descript
def exitGame(): # Quitte le jeu en remettant les parametres par defaut
    global defaultTerminal
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, defaultTerminal)
    sys.exit()


