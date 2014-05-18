import random
monsters = (
    {"name" : "Un mendiant affame", "rate" : 3, "skill" : 6, "health" : 6, "fight" : "Le mendiant affame"},
    {"name" : "Un mendiant", "rate" : 4, "skill" : 7, "health" : 6, "fight" : "Le mendiant"},
    {"name" : "Un mendiant en colere", "rate" : 6, "skill" :  7, "health" : 8, "fight" : "Le mendiant en colere"},
    {"name" : "Un chien enrage", "rate" : 7, "skill" : 8, "health" : 8, "fight" : "Le chien enrage"},
    {"name" : "Un vieux kobold", "rate" : 7, "skill" :  8, "health" : 10, "fight" : "Le vieux kobold"},
    {"name" : "Un kobold", "rate" : 8, "skill" :  8, "health" : 10, "fight" : "Le kobold"},
    {"name" : "Un Dude", "rate" : 10, "skill" :  9, "health" : 10, "fight" : "The Dude"},
    {"name" : "Un bandit manchot", "rate" : 9, "skill" :  9, "health" : 12, "fight" : "Le bandit manchot"},
    {"name" : "Un bandit cul-de-jatte", "rate" : 8, "skill" : 9, "health" : 12, "fight" : "Le bandit cul-de-jatte"},
    {"name" : "Un assassin", "rate" : 7, "skill" :  9, "health" : 14, "fight" : "L'assassin"},
    {"name" : "Un chef de gang", "rate" : 6, "skill" :  10, "health" : 14, "fight" : "Le chef de gang"},
    {"name" : "Un vampire", "rate" : 6, "skill" :  10, "health" : 14, "fight" : "Le vampire"},
    {"name" : "Un loup-garou", "rate" : 5, "skill" : 10, "health" : 14, "fight" : "Le loup-garou"},
    {"name" : "Un troll", "rate" : 5, "skill" : 11, "health" : 14, "fight" : "Le troll"},
    {"name" : "Lord helix", "rate" : 5, "skill" : 12 , "health" : 14, "fight" : "Lord Helix"},
    {"name" : "Un Alduin", "rate" : 3, "skill" : 12, "health" : 16, "fight" : "Alduin"},
    {"name" : "Une licorne rose invisible", "rate" : 1, "skill" :  14, "health" : 20, "fight" : "La Licorne Rose Invisible"})

def addRandom():
    monster = random.randint(1,100)
    rate = monsters[0]["rate"]
    index = 0
    while rate < monster:
        rate += monsters[index + 1]["rate"] 
        index += 1
    return monsters[index]
