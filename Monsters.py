import random
monsters = (
    {"name": "un mendiant affame", "rate" : 3, "skill" : 6, "health" : 6, "fight" : "Le mendiant affame"},
    {"name" : "un mendiant", "rate" : 4, "skill" : 7, "health" : 6, "fight" : "Le mendiant"},
    {"name" : "un mendiant en colere", "rate" : 6, "skill" :  7, "health" : 8, "fight" : "Le mendiant en colere"},
    {"name" : "un chien enrage", "rate" : 7, "skill" : 8, "health" : 8, "fight" : "Le chien enrage"},
    {"name" : "un vieux kobold", "rate" : 7, "skill" :  8, "health" : 10, "fight" : "Le vieux kobold"},
    {"name" : "un kobold", "rate" : 8, "skill" :  8, "health" : 10, "fight" : "Le kobold"},
    {"name" : "The Dude", "rate" : 10, "skill" :  9, "health" : 10, "fight" : "The Dude"},
    {"name" : "un bandit manchot", "rate" : 9, "skill" :  9, "health" : 12, "fight" : "Le bandit manchot"},
    {"name" : "un bandit cul-de-jatte", "rate" : 8, "skill" : 9, "health" : 12, "fight" : "Le bandit cul-de-jatte"},
    {"name" : "un assassin", "rate" : 7, "skill" :  9, "health" : 14, "fight" : "L'assassin"},
    {"name" : "un chef de gang", "rate" : 6, "skill" :  10, "health" : 14, "fight" : "Le chef de gang"},
    {"name" : "un vampire", "rate" : 6, "skill" :  10, "health" : 14, "fight" : "Le vampire"},
    {"name" : "un loup-garou", "rate" : 5, "skill" : 10, "health" : 14, "fight" : "Le loup-garou"},
    {"name" : "un troll", "rate" : 5, "skill" : 11, "health" : 14, "fight" : "Le troll"},
    {"name" : "Lord helix", "rate" : 5, "skill" : 12 , "health" : 14, "fight" : "Lord Helix"},
    {"name" : "Alduin le dragon", "rate" : 3, "skill" : 12, "health" : 16, "fight" : "Alduin"},
    {"name" : "une licorne rose invisible", "rate" : 1, "skill" :  14, "health" : 20, "fight" : "La Licorne Rose Invisible"})

def addRandom():
    monster = random.randint(1,100)
    rate = 0
    index = 0
    while rate < monster:
        rate += monsters[index]["rate"] 
        index += 1
    return monsters[index]
