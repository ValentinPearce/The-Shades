line=['','','','','','']
map=[]
for i in range (6): #creation d'une carte vierge
    map.append([])
    for j in range (6):
        map[i].append({'items':[],'north':0,'south':0,'east':0,'west':0})
#""" 
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
            line[i]=[i]+' '
    print line[i]
#"""            
print len(line)
