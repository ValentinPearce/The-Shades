#Module Player

import random

player={'name' :'Bob','position' :(0,0),'health' :0, 'time' :0,'inventory' :[],'equip' :[]}

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

def editTime(modifier): # Modifie le temps passe par le joueur
	player['time']=player['time']+modifier

''' Non implement pour l'instant.
def getInventory():
	return player['inventory']

def addItem(index):
	player['inventory'].append(index)

def removeItem(index):
	player['inventory'].remove(index)

def equip(index):
	player['equip'].pop(0)
	player['equip'].append(index)
'''
