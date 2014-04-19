import Game

description = ''

def init():
    description = Game.init()
def display():
    global description
    Game.display(description)
def interact():
    Game.getAction()
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
