#==============
#INITIALISATION
#==============

import Game
import termios, sys
description = ''

def init(): # Mets en place les elements du jeu.
    global description
    description = Game.init()

def display(): # Affiche certains elements du jeu et le texte relatif a la derniere action effectuee
    global description
    Game.display(description,36)

def interact(): # Releve toute interaction du joueur.
    global description
    description = Game.getAction()

def run():
    while 1: # Boucle de simulation.
        Game.checkHealth()
        Game.checkTime(36)
        display()
        interact()

def main(): # Fonction principale
    init()
    run()

#=========
#EXECUTION
#=========
main()
