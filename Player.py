#Module Player

import random

player={'name' :'Bob','position' :(0,0),'health' :0,'power' : 0 , 'time' :0,'inventory' :[],'equip' :[]}

def setName(): # Defini le nom du joueur
	player['name']=raw_input()

def getName(): # Renvoie le nom du joueur
	return player['name']

def setHealth(): # Defini la vie du joueur
	player['health']=12+random.randint(1,6)+random.randint(1,6)

def getHealth(): # Renvoie la vie du joueur
	return player['health']

def editHealth(modifier): # Modifie la vie du joueur
	player['health']=player['health']+modifier

def move(direction): # Modifie la position du joueur
	if direction=="north":
		player['position']=(player['position'][0]-1, player['position'][1])
	elif direction=="south":
		player['position']=(player['position'][0]+1, player['position'][1])
	elif direction=="east":
		player["position"]=(player['position'][0], player['position'][1]+1)
	elif direction=="west":
		player['position']=(player['position'][0], player['position'][1]-1)

def getPosition(): # Renvoie la position du joueur
	return player['position']

def getTime(): # Renvoie le temps passe par le joueur
	return player['time']

def setPower():
	player['power']= random.randint(1,6) + random.randint(1,6)

def getPower():
	return player["power"]

def editTime(modifier): # Modifie le temps passe par le joueur
	player['time']=player['time']+modifier

def addItem(item): # Ajoute un objet a l'inventaire
	player['inventory'].append(item)

def removeItem(index): # Retire un objet de l'inventaire
	player['inventory'].pop(index)

def equip(item): # Equipe un objet
        if len(player['equip']) == 1:
		player['equip'] = []
	player['equip']= dict(item)

def getEquipModifier():
	if len(player['equip']):
		return player['equip']['Modifier'] 
	else:
		return 0
def isItem(): # Renvoie le nombre d'objets dans l'inventaire
	return len(player["inventory"])

def getItem(index):
	return player["inventory"][index]

def getItemName(index):
	return player["inventory"][index]["name"]

def isEquip():
	return len(player["equip"])
 
def getItemList(): # Renvoie la 
    descript = ""
    for i in range(len(player["inventory"])) :
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
        descript += player["inventory"][i]["name"]
    return descript
