import random
monsters = (
    {"name" : "pink fluffy unicorn", "rate" : 1, "power" : 1, "health" : 1,"fight" : "The pink fluffy unicorn"},
    {"name" : "starving beggar", "rate" : 3, "power" : 6, "health" : 6, "fight" : "The starving beggar"},
    {"name" : "beggar", "rate" : 4, "power" : 7, "health" : 6, "fight" : "The beggar"},
    {"name" : "angry beggar", "rate" : 6, "power" :  7, "health" : 8, "fight" : "The angry beggar"},
    {"name" : "raving dog", "rate" : 7, "power" : 8, "health" : 8, "fight" : "The raving dog"},
    {"name" : "old kobold", "rate" : 7, "power" :  8, "health" : 10, "fight" : "The old kobold"},
    {"name" : "kobold", "rate" : 8, "power" :  8, "health" : 10, "fight" : "The kobold"},
    {"name" : "Lebowski", "rate" : 10, "power" :  9, "health" : 10, "fight" : "The Dude"},
    {"name" : "'armless bandit", "rate" : 9, "power" :  9, "health" : 12, "fight" : "The 'armless bandit"},
    {"name" : "legless bandit", "rate" : 8, "power" : 9, "health" : 12, "fight" : "The legess bandit"},
    {"name" : "assassin", "rate" : 7, "power" :  9, "health" : 14, "fight" : "The assassin"},
    {"name" : "gang leader", "rate" : 6, "power" :  10, "health" : 14, "fight" : "The gang leader"},
    {"name" : "vampire", "rate" : 6, "power" :  10, "health" : 14, "fight" : "The vampire"},
    {"name" : "ilama", "rate" : 5, "power" : 10, "health" : 10, "fight" : "Th ilama"},
    {"name" : "werewolf", "rate" : 5, "power" : 10, "health" : 14, "fight" : "The werewolf"},
    {"name" : "troll", "rate" : 5, "power" : 11, "health" : 14, "fight" : "The troll"},
    {"name" : "Lord helix", "rate" : 5, "power" : 12 , "health" : 14, "fight" : "Lord Helix"},
    {"name" : "Alduin", "rate" : 3, "power" : 12, "health" : 16, "fight" : "Alduin"},
    {"name" : "Invisible Pink Unicorn", "rate" : 1, "power" :  14, "health" : 20, "fight" : "The Invisible Pink Unicorn"})

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
