import random
map=[]
path=[]
for i in range (6): #creation d'une carte vierge
    map.append([])
    for j in range (6):
        map[i].append({'items':[],'north':0,'south':0,'east':0,'west':0})

def nextArea():
    global i,j,visited
    chosen = 0
    n = 0
    s = 0
    e = 0
    w = 0
    dir = 0

    if i>0 :
        if map[i-1][j]['north']== 0 and map[i-1][j]['south']== 0 and map[i-1][j]['east']== 0 and map[i-1][j]['west']== 0 :
            w = 1
    if i<5 :
        if map[i+1][j]['north']== 0 and map[i+1][j]['south']== 0 and map[i+1][j]['east']== 0 and map[i+1][j]['west']== 0 :
            e = 1
    if j>0 :
        if map[i][j-1]['north']== 0 and map[i][j-1]['south']== 0 and map[i][j-1]['east']== 0 and map[i][j-1]['west']== 0 :
            s = 1
    if j>5 :
        if map[i][j+1]['north']== 0 and map[i][j+1]['south']== 0 and map[i][j+1]['east']== 0 and map[i][j+1]['west']== 0 :
            n = 1
    if n+s+e+w > 0:
        while chosen == 0:
            dir = random.randint(0,3)
            if dir == 0 and w == 1:
                chosen = 1
                map[i][j]['west'] = 1
                map[i-1][j]['east'] = 1
                i = i-1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
            elif dir == 1 and e == 1:
                chosen = 1
                map[i][j]['east'] = 1
                map[i+1][j]['west'] = 1
                i = i+1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
            elif dir == 2 and n == 1:
                chosen = 1
                map[i][i]['north'] = 1
                map[i][j+1]['south'] = 1
                j = j-1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
            elif dir == 3 and s == 1:
                chosen = 1
                map[i][j]['south'] = 1
                map[i][j-1]['north'] = 1
                j = j+1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
        else:
         path.pop(len(path)-1)
         i = path[len(path) - 1][0]
         j = path[len(path) - 1][1]
#=========================================================
i = random.randint(0,5)
j = random.randint(0,5)
visiting = i,j
path.append(visiting)
visited = 1

for i in range (6): #creation d'une carte vierge
    map.append([])
    for j in range (6):
        map[i].append({'items':[],'north':0,'south':0,'east':0,'west':0})

loop = 0
while visited < 37 :
    nextArea()
    print visited
    loop = loop + 1
    print loop

#""" 
line=['','','','','','']
for i in range (6): #creation d'un visuel de carte
    for j in range (6):
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
#"""            
print visited
