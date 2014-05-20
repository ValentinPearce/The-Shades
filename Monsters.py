import random
monsters = (
    {"name" : "Une licorne rose touffue", "rate" : 1, "power" : 1, "health" : 1, "fight" : "La licorne rose touffue"},
    {"name" : "Un mendiant affame", "rate" : 3, "power" : 6, "health" : 6, "fight" : "Le mendiant affame"},
    {"name" : "Un mendiant", "rate" : 4, "power" : 7, "health" : 6, "fight" : "Le mendiant"},
    {"name" : "Un mendiant en colere", "rate" : 6, "power" :  7, "health" : 8, "fight" : "Le mendiant en colere"},
    {"name" : "Un chien enrage", "rate" : 7, "power" : 8, "health" : 8, "fight" : "Le chien enrage"},
    {"name" : "Un vieux kobold", "rate" : 7, "power" :  8, "health" : 10, "fight" : "Le vieux kobold"},
    {"name" : "Un kobold", "rate" : 8, "power" :  8, "health" : 10, "fight" : "Le kobold"},
    {"name" : "Un Dude", "rate" : 10, "power" :  9, "health" : 10, "fight" : "The Dude"},
    {"name" : "Un bandit manchot", "rate" : 9, "power" :  9, "health" : 12, "fight" : "Le bandit manchot"},
    {"name" : "Un bandit cul-de-jatte", "rate" : 8, "power" : 9, "health" : 12, "fight" : "Le bandit cul-de-jatte"},
    {"name" : "Un assassin", "rate" : 7, "power" :  9, "health" : 14, "fight" : "L'assassin"},
    {"name" : "Un chef de gang", "rate" : 6, "power" :  10, "health" : 14, "fight" : "Le chef de gang"},
    {"name" : "Un vampire", "rate" : 6, "power" :  10, "health" : 14, "fight" : "Le vampire"},
    {"name" : "Un lama", "rate" : 5, "power" : 10, "health" : 10, "fight" : "Le loup-garou"},
    {"name" : "Un loup-garou", "rate" : 5, "power" : 10, "health" : 14, "fight" : "Le loup-garou"},
    {"name" : "Un troll", "rate" : 5, "power" : 11, "health" : 14, "fight" : "Le troll"},
    {"name" : "Lord helix", "rate" : 5, "power" : 12 , "health" : 14, "fight" : "Lord Helix"},
    {"name" : "Un Alduin", "rate" : 3, "power" : 12, "health" : 16, "fight" : "Alduin"},
    {"name" : "Une licorne rose invisible", "rate" : 1, "power" :  14, "health" : 20, "fight" : "La Licorne Rose Invisible"})

def addRandom():
    rate = monsters[0]["rate"]
    maxRate = 0
    for i in range (len(monsters)):
        maxRate += monsters[i]["rate"]
    monster = random.randint(1,maxRate)
    index = 0
    while rate < monster:
        rate += monsters[index + 1]["rate"] 
        index += 1
    return monsters[index]
