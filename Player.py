#Module Player

import random
#===========================================================
#INITIALISATION
#===========================================================
player={'name' :'Bob','position' :(0,0),'health' :0,'power' : 0 , 'time' :0,'inventory' :[],'equip' :[]}

def setName(): # Defini le nom du joueur
	player['name']=raw_input()

def setHealth(): # Defini la vie du joueur
	player['health']=12+random.randint(1,6)+random.randint(1,6)

def setPower():
	player['power']= random.randint(1,6) + random.randint(1,6)

#===========================================================
#ACCESSEURS
#===========================================================

def getHealth(): # Renvoie la vie du joueur
	return player['health']

def getName(): # Renvoie le nom du joueur
	return player['name']

def getPosition(): # Renvoie la position du joueur
	return player['position']

def getTime(): # Renvoie le temps passe par le joueur
	return player['time']

def getPower(): # Renvoie la force du joueur
	return player["power"]

def getEquipModifier(): # Renvoie le bonus de force de l'objet equipé
	if len(player['equip']):
		return player['equip']['Modifier'] 
	else:
		return 0

def isEquip(): # Renvoie 0 si aucun objet n'est équipé et 1 si un objet est équipé
	return len(player["equip"])
 
def isItem(): # Renvoie le nombre d'objets dans l'inventaire
	return len(player["inventory"])

def getItem(index): # Renvoie l'objet nºindex de l'inventaire
	return player["inventory"][index]

def getItemName(index): # Renvoie le nom de l'objet nºindex de l'inventaire
	return player["inventory"][index]["name"]

def getItemList(): # Renvoie la liste des objets de l'inventaire avec un index (wxcvbn) 
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
        descript += player["inventory"][i]["liste"]
    return descript

#=============================================
#MODIFICATEURS
#=============================================

def editHealth(modifier): # Modifie la vie du joueur d'une valeur égale à "modifier"
	player['health']=player['health']+modifier

def move(direction): # Modifie la position du joueur dans la direction souhaitée
	if direction=="north":
		player['position']=(player['position'][0]-1, player['position'][1])
	elif direction=="south":
		player['position']=(player['position'][0]+1, player['position'][1])
	elif direction=="east":
		player["position"]=(player['position'][0], player['position'][1]+1)
	elif direction=="west":
		player['position']=(player['position'][0], player['position'][1]-1)

def editTime(modifier): # Modifie le temps passe par le joueur de modifier
	player['time']=player['time']+modifier

def addItem(item): # Ajoute un objet a l'inventaire
	player['inventory'].append(item)

def removeItem(index): # Retire un objet de l'inventaire
	player['inventory'].pop(index)

def equip(item): # Equipe un objet
        if len(player['equip']) == 1:
		player['equip'] = []
	player['equip']= dict(item)


