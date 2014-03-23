controls = ["observer","nord","sud","est","west","n","s","e","w","crier","merde","help"]

def act():
    print "Que voulez-vous faire?"
    command = raw_input()
    command = command.split()
    if command[0] == controls[0]:
        print("Description avancee")
    elif command[0] == ( controls[1] or controls[5] ) :
        print "Vous vous deplacez vers le Nord."
    elif command[0] == ( controls[2] or controls[6] ) :
        print "Vous vous deplacez vers le sud."
    elif command[0] == ( controls[3] or controls[7] ) :
        print "Vous vous deplacez vers l'Est"
    elif command[0] == ( controls[4] or controls[8] ) :
        print "Vous vous deplacez vers l'Ouest"
    elif command[0] ==  controls[9] :
        for i in range (1,len(command)):
            print uppercase(command[i]),
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    elif command[0] == controls[10] :
        print "Ne soyez tout de meme pas vulgaire."
    elif command[0] == controls[11] :
        print "voici la liste des commandes possibles."
        for j in range (len(controls)) :
            print controls[j]
    else:
        print "Je ne comprends pas le terme",command[0]

act()
