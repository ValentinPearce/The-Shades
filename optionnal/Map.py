import random, Monsters, Items
map=[]
path=[]
visited=0
i=0
j=0

def createEmpty(size): # Cree une carte vide.
    for i in range (size):
        map.append([])
        for j in range (size):
            map[i].append({'items':[],'north':0,'south':0,'east':0,'west':0, "monster" : [] })

    
def createMaze(size): # Cree un labyrinthe parfait.
    global visited,i,j
    chosen = 0
    n = 0
    s = 0
    e = 0
    w = 0
    dir = 0

    if i>0 :
        if map[i-1][j]['north']== 0 and map[i-1][j]['south']== 0 and map[i-1][j]['east']== 0 and map[i-1][j]['west']== 0 :
            n = 1
    if i<size - 1 :
        if map[i+1][j]['north']== 0 and map[i+1][j]['south']== 0 and map[i+1][j]['east']== 0 and map[i+1][j]['west']== 0 :
            s = 1
    if j>0 :
        if map[i][j-1]['north']== 0 and map[i][j-1]['south']== 0 and map[i][j-1]['east']== 0 and map[i][j-1]['west']== 0 :
            w = 1
    if j<size - 1 :
        if map[i][j+1]['north']== 0 and map[i][j+1]['south']== 0 and map[i][j+1]['east']== 0 and map[i][j+1]['west']== 0 :
            e = 1
    if n+s+e+w > 0:
        while chosen == 0:
            dir = random.randint(0,3)
            if dir == 0 and w == 1:
                chosen = 1
                map[i][j]['west'] = 1
                map[i][j-1]['east'] = 1
                j = j - 1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
#                printMap()
#                print 'west'
            elif dir == 1 and e == 1:
                chosen = 1
                map[i][j]['east'] = 1
                map[i][j+1]['west'] = 1
                j = j + 1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
#                printMap()
#                print 'east'
            elif dir == 2 and s == 1:
                chosen = 1
                map[i][j]['south'] = 1
                map[i+1][j]['north'] = 1
                i = i + 1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
#                printMap()
#                print 'south'
            elif dir == 3 and n == 1:
                chosen = 1
                map[i][j]['north'] = 1
                map[i-1][j]['south'] = 1
                i = i - 1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
#                printMap()
#                print 'north'
    else:
#         print 'BACK'
         path.pop(len(path)-1)
         i = path[len(path) - 1][0]
         j = path[len(path) - 1][1]

def printMap(): # Affiche un visuel de la carte. Destine aux developpeurs.
    line=['','','','','','']
    for i in range (size): 
        for j in range (size):
            if map[i][j]['west']== 0:
                line[i]=line[i]+'|'
            else:
                line[i]=line[i]+' '
            if map[i][j]['north']== 0 and map [i][j]['south']== 0:
                line[i]=line[i]+'='
            elif map[i][j]['north']== 0:
                line[i]=line[i]+'^'
            elif map[i][j]['south']== 0:
                line[i]=line[i]+'_'
            else:
                line[i]=line[i]+' '
            if map[i][j]['east']== 0:
                line[i]=line[i]+'|'
            else:
                line[i]=line[i]+' '
        print line[i]

def addExits(size): # Ajoute des sorties (condition de victoire) au labyrinte
    quantum = random.randint(2,4)
    for exit in range(quantum):
        side = random.randint(0,1)
        if side == 0:
            map[size - 1][random.randint(0,size - 1)]['south'] = 2
        else:
            map[random.randint(0,size - 1)][size - 1]['east'] = 2

def setMonstersItems(size):
    for i in range (size):
        for j in range (size):
            if (i,j) != (0,0) :
                site = random.randint(0,4)
                if site >= 3:
                    map[i][j]["monster"] = dict(Monsters.addRandom())
                elif site > 0:
                    map[i][j]["items"].append(Items.addRandom())


def addItem(position,item):
    map[position[0]][position[1]]['items'].append(item)            

def removeItem(position,index):
    map[position[0]][position[1]]['items'].pop(index)            


def check(position, direction):
    answer = map[position[0]][position[1]][direction]
    return answer

def getDescript(position): # Genere la description de la zone dans laquelle se trouve le joueur.
    n = check(position,'north')
    s = check(position,'south')
    e = check(position,'east')
    w = check(position,'west')
    descript = "The area you're in has"
    if n>0 and s+e+w>0 :
        descript = descript + " an exit north"
        if s > 0 and e+w>0:
            descript = descript + ", an exit south"
            if e>0 and w>0:
                descript = descript + ", and exits east and west."
            elif e>0 and w==0:
                descript = descript + " and an exit east."
            else :
                descript = descript + " and an exit west."
        elif s>0 :
            descript = descript + " and an exit south"
        elif e>0 and w>0:
            descript = descript + ", and exits east and west."
        elif e>0 and w==0:
            descript = descript + " and an exit east."
        else:
            descript = descript + " and an exit west."
    elif n>0:
        descript = descript + " an exit north."
    elif s > 0 and e+w>0:
        descript = descript + " an exit south"
        if e>0 and w>0:
            descript = descript + ", an exit east and another west."
        elif e>0 and w==0:
            descript = descript + " and  an exit east."
        else:
            descript = descript + " and an exit west."
    elif s>0:
        descript = descript + " an exit south."
    elif e>0 and w>0:
        descript = descript + " exits east and west."
    elif e>0 and w==0:
        descript = descript + " an exit east."
    else:
        descript = descript + " an exit west."
    if len(map[position[0]][position[1]]["monster"]) != 0:
        descript += " ~~~~~~~~~~~~~~~~~~~~~~~~~ " + " A wild " + map[position[0]][position[1]]["monster"]["name"] + " appears! You must fight!"
    return descript

def getAltDescript(position): # Ajoute quelques informations a la description de base
    descript = getDescript(position)
    s = check(position,'south')
    e = check(position,'east')
    if s == 2:
        descript += " ~~~~~~~~~~~~~~~~~~~~~~~~~ The suthern exit is particularly bright."
    if e == 2:
        descript += " ~~~~~~~~~~~~~~~~~~~~~~~~~ The eastern exit is particularly bright."
    list = map[position[0]][position[1]]["items"]
    if len(list) > 0:
        descript += " ~~~~~~~~~~~~~~~~~~~~~~~~~ On the ground you can see k "
        for i in range (len(list)):
            descript += list[i]["name"]
        if len(list) - i ==1:
            descript += "."
        elif len(list) - i == 2:
            descript += " et "
        else:
            descript += ", "
    return descript

def generate(size): # Fonction principale du module
    global i,j,visited
    createEmpty(size)
    visiting = random.randint(0,size - 1),random.randint(0,size - 1)
    i = visiting[0]
    j = visiting[1]
    path.append(visiting)
    visited = 1

    while visited < size*size :
        createMaze(size)
    addExits(size)
    setMonstersItems(size)

def isItem(position):
    return len(map[position[0]][position[1]]["items"])

def getItemList(position):
    descript = ""
    for i in range(len(map[position[0]][position[1]]["items"])) :
        descript += "("
        if i == 0:
            descript += "W) "
        elif i == 1:
            descript += "X) "
        elif i == 2:
            descript += "C) "
        elif i == 3:
            descript += "V) "
        elif i == 4:
            descript += "B) "
        elif i == 5:
            descript += "N) "
        descript += map[position[0]][position[1]]["items"][i]["liste"]
    return descript

def getItem(position, index):
    return map[position[0]][position[1]]["items"][index]

def getItemName(position, index):
    return map[position[0]][position[1]]["items"][index]["name"]

def isMonster(position):
    return len(map[position[0]][position[1]]["monster"])

def getMonsterHealth(position):
    return map[position[0]][position[1]]["monster"]["health"]

def getMonsterPower(position):
    return map[position[0]][position[1]]["monster"]["power"]

def editMonsterHealth(position, modifier):
    map[position[0]][position[1]]["monster"]["health"] += modifier

def removeMonster(position):
    map[position[0]][position[1]]["monster"]=[]



#        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
#generate(6)
#printMap()
#print getDescript((4,2),0)
#print getAltDescript((4,2))
