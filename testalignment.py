from math import exp
import random
import sqlite3 as lite
import pandas as pd

party_size = input("Party Size? ")
party_level = input("Party Level? ")
encounter_difficulty = input("Encounter Difficulty? (easy, medium, hard, deadly): ")
if encounter_difficulty.lower() == "easy":
    party_level_xp_values = {
        "1":25,
        "2":50,
        "3":75,
        "4":125,
        "5":250,
        "6":300,
        "7":350,
        "8":450,
        "9":550,
        "10":600,
        "11":800,
        "12":1000,
        "13":1100,
        "14":1250,
        "15":1400,
        "16":1600,
        "17":2000,
        "18":2100,
        "19":2400,
        "20":2800
    }
elif encounter_difficulty.lower() == "medium":
    party_level_xp_values = {
        "1":50,
        "2":100,
        "3":150,
        "4":250,
        "5":500,
        "6":600,
        "7":700,
        "8":900,
        "9":1100,
        "10":1200,
        "11":1600,
        "12":2000,
        "13":2200,
        "14":2500,
        "15":2800,
        "16":3200,
        "17":3900,
        "18":4200,
        "19":4900,
        "20":5700
    }
elif encounter_difficulty.lower() == "hard":
    party_level_xp_values = {
        "1":75,
        "2":150,
        "3":225,
        "4":375,
        "5":750,
        "6":900,
        "7":1100,
        "8":1400,
        "9":1600,
        "10":1900,
        "11":2400,
        "12":3000,
        "13":3400,
        "14":3800,
        "15":4300,
        "16":4800,
        "17":5900,
        "18":6300,
        "19":7300,
        "20":8500
    }
elif encounter_difficulty.lower() == "deadly":
    party_level_xp_values = {
        "1":100,
        "2":200,
        "3":400,
        "4":500,
        "5":1100,
        "6":1400,
        "7":1700,
        "8":2100,
        "9":2400,
        "10":2800,
        "11":3600,
        "12":4500,
        "13":5100,
        "14":5700,
        "15":6400,
        "16":7200,
        "17":8800,
        "18":9500,
        "19":10900,
        "20":12700
    }
    
num_monsters_multiplier = {
    0:1,
    1:1,
    2:1.5,
    3:2,
    4:2,
    5:2,
    6:2,
    7:2.5,
    8:2.5,
    9:2.5,
    10:2.5,
    11:3,
    12:3,
    13:3,
    14:3,
    15:4,
    16:4,
    17:4,
    18:4,
    19:4,
    20:4
}
# Calculate expected XP SUM for party
base_xp = int(party_level_xp_values[party_level])  # finds xp value corresponding to party level
xp_sum = base_xp * int(party_size) # multiplies party size by the base xp expected of one player
print("Total party xp distribution for encounter generation: " + str(xp_sum))


#Generate List based on terrain -- in this case, arctic
mon_list = []
con = lite.connect("encounter_sheets/arctic.db")  # connect to db

cur = con.cursor() # Create cursor object to manipulate sqlite db
min_CR = input("Minimum Challenge Rating?: ")
max_CR = input("Maximum Challenge Rating?: ")
cur.execute("SELECT Monster, Xp FROM arctic WHERE CR>=? AND CR<=?", (min_CR, max_CR)) # Filters out any Monsters with CR rating lower than set parameter
rows = cur.fetchall()

print(rows) # Shows current filtering of mons DEBUGGING
for row in rows:
    mon_list.append(row)  # Adds result from above filtering to py list
    # data sets are appended as tuples to the list, need to filter out name and xp values, preferably able to call upon type and other vars

used_xp = 0
encounter_list = []
experience = 0

while xp_sum >= used_xp:
    encounter_length = len(encounter_list)
    used_xp = used_xp
    if encounter_length == 0 and xp_sum >= used_xp:
        mon_select = random.choice(mon_list)
        encounter_list.append(mon_select[0])
        encounter_length = int(len(encounter_list))
        experience = int(mon_select[1])
        print("\n\nExperience for mon 1: " + str(experience))
        used_xp = used_xp + experience
        print("Used: " +str(experience) + "so far \n\n")

    if encounter_length >= 1 and xp_sum >= used_xp:
        mon_select = random.choice(mon_list)
        encounter_list.append(mon_select[0])
        multiplier = num_monsters_multiplier[encounter_length]
        print("Length of encounter list: " + str(encounter_length)) # Should be at minimum 2 by this point
        print("Multiplier value: " + str(multiplier))
        print("Initial value for mon n: " + str(mon_select[1]))
        experience = int(mon_select[1])
        print("Modified Experience value for mon n: " + str(experience))
        used_xp = used_xp + experience
        



    '''    
    elif encounter_length >= 1 and xp_sum >= used_xp:
        mon_select = random.choice(mon_list)
        encounter_list.append(mon_select[0])
        multiplier = num_monsters_multiplier[encounter_length]
        print("Length of encounter list: " + str(encounter_length)) # Should be at minimum 2 by this point
        print("Multiplier value: " + str(multiplier))
        print("Initial value for mon n: " + str(mon_select[1]))
        experience = int(mon_select[1]) * multiplier
        print("Modified Experience value for mon n: " + str(experience))
        used_xp = used_xp + experience
    '''
    if used_xp >= xp_sum:
        print("Threshold reached, terminating")
        break
    
    print("Used experience: " + str(used_xp))
    

print("Your encounter consists of: " + str(encounter_list) + "\nWith " + str(xp_sum) + "xp remaining for distribution." )



