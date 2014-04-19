import Game

description = 'bijour'

def init():
    global description
    description = Game.init()
def display():
    global description
    Game.display(description)
def interact():
    global description
    description = Game.getAction()
def run():
    while 1:
        Game.checkHealth()
        Game.checkTime()
        display()
        interact()
def main():
    init()
    run()
#========================
main()
