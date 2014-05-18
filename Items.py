import random

items = (
	{"name" : "une Fee" , "rate" : 4 , "type" : 0 , "Modifier" : 6},
	{"name" : "un Coeur" , "rate" : 10 , "type" : 0 , "Modifier" : 1},
	{"name" : "une Galette Saucisse" , "rate" : 9 , "type" : 0 , "Modifier" : 2},
	{"name" : "des Abats" , "rate" : 10 , "type" : 0 , "Modifier" : 1},
	{"name" : "des Jelly Babies" , "rate" : 7 , "type" : 0 , "Modifier" : 4},
	{"name" : "une Fleu de Feu" , "rate" : 7 , "type" : 1 , "Modifier" : 1},
	{"name" : "un Arc" , "rate" : 7 , "type" : 1 , "Modifier" : 1},
	{"name" : "une Arbalette" , "rate" : 5 , "type" : 1 , "Modifier" : 3},
	{"name" : "un Morgenstern" , "rate" : 5 , "type" : 1 , "Modifier" : 3},
	{"name" : "une Masse" , "rate" : 7 , "type" : 1 , "Modifier" : 2},
	{"name" : "la Master Sword" , "rate" : 2 , "type" : 1 , "Modifier" : 6},
	{"name" : "un Lance-Pierre" , "rate" : 7 , "type" : 1 , "Modifier" : 1},
	{"name" : "une Catapulte" , "rate" : 3 , "type" : 1 , "Modifier" : 5},
	{"name" : "une Claymore" , "rate" : 5 , "type" : 1 , "Modifier" : 3},
	{"name" : "un Katana" , "rate" : 6 , "type" : 1 , "Modifier" : 2},
	{"name" : "un Tromblon" , "rate" : 6 , "type" : 1 , "Modifier" : 2})


def addRandom():
	item = random.randint(1,100)
	rate = items[0]["rate"]
	index = 0
	while rate < item:
		rate += items[index + 1]["rate"]
		index += 1
	return items[index]
