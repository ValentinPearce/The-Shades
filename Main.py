import Game
import tty
import sys
import select
import termios

def init():
    Game.init()
def display():
    global description
    Game.display(description)
def interact():
    Game.getaction()
def run():
    Game.checkHealth()
    Game.checkTime()
    display()
    interact()
def main():
    init()
    run()
#========================
main()
