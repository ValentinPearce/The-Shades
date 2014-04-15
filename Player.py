#Module Player

import random

player={'name' :'Bob','position' :(0,0),'health' :0, 'time' :1,'inventory' :[],'equip' :[]}

def setName():
	player['name']=raw_input("Quel est votre nom ? ")

def getHealth():
	return player['health']

def editHealth(modifier):
	player['health']=player['health']+modifier

def setHealth():
	player['health']=12+random.randint(1,6)+random.randint(1,6)

def move(direction):
	if direction=="north":
		player['position']=player['position'][0]-1, player['position'][1]
	elif direction=="south":
		player['position']=player['position'][0]+1, player['position'][1]
	elif direction=="east":
		player["position"]=palyer['position'][0], player['position'][1]+1
	elif direction=="weast":
		player['position']=player['position'][0], player['position'][1]-1

def getPosition():
	return player['position']

def getTime():
	return player['time']

def editTime(modifier):
	player['time']=player['time']+modifier

def getInventory():
	return player['inventory']

def addItem(index):
	player['inventory'].append(index)

def removeItem(index):
	player['inventory'].remove(index)

def equip(index):
	player['equip'].pop(0)
	player['equip'].append(index)
