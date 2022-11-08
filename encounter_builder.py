import random
import os
import sqlite3 as lite
import pandas as pd

class Encounter:
    def __init__(self):
        self.min_CR = 0
        self.max_CR = 30
        self.terrain_choice = "None"
        self.party_size = 4
        self.party_level = 8
        self.threat = "None"
        self.number_creatures = 1
        self.available_monsters = {}
        self.encounter_difficulty = "None"
        self.multiplier_val = 0
        self.xp_total = 0
        self.used_xp = 0
        self.mon_list = []
        self.encounter_list = []

    def terrain(self):
        terrains = ["arctic", "desert", "forest", "hills", "grasslands", "jungle", "mountains", "ocean", "plains", "riverland", "swamp", "urban", "underdark", "underground", "elemental", "avernus"]
        
        # Generate List based on terrain
        self.mon_list = []
        con = lite.connect("encounter_sheets/" + self.terrain_choice + ".db")  # connect to db

        cur = con.cursor() # Create cursor object to manipulate sqlite db

        cur.execute("SELECT Monster, Xp FROM " + self.terrain_choice + " WHERE CR>=? AND CR<=?", (self.min_CR, self.max_CR)) # Filters out any Monsters with CR rating lower than set parameter
        rows = cur.fetchall()
        for row in rows:
            self.mon_list.append(row)  # Adds result from above filtering to py list
            
    def multiplier(self, num_monsters):
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

        self.multiplier_val = num_monsters_multiplier[num_monsters]

    def difficulty(self):
        if self.threat.lower() == "easy":
            party_level_xp_values = {
                1:25,
                2:50,
                3:75,
                4:125,
                5:250,
                6:300,
                7:350,
                8:450,
                9:550,
                10:600,
                11:800,
                12:1000,
                13:1100,
                14:1250,
                15:1400,
                16:1600,
                17:2000,
                18:2100,
                19:2400,
                20:2800
            }

        elif self.threat.lower() == "medium":
            party_level_xp_values = {
                1:50,
                2:100,
                3:150,
                4:250,
                5:500,
                6:600,
                7:700,
                8:900,
                9:1100,
                10:1200,
                11:1600,
                12:2000,
                13:2200,
                14:2500,
                15:2800,
                16:3200,
                17:3900,
                18:4200,
                19:4900,
                20:5700
            }

        elif self.threat.lower() == "hard":
            party_level_xp_values = {
                1:75,
                2:150,
                3:225,
                4:375,
                5:750,
                6:900,
                7:1100,
                8:1400,
                9:1600,
                10:1900,
                11:2400,
                12:3000,
                13:3400,
                14:3800,
                15:4300,
                16:4800,
                17:5900,
                18:6300,
                19:7300,
                20:8500
            }

        elif self.threat.lower() == "deadly":
            party_level_xp_values = {
                1:100,
                2:200,
                3:400,
                4:500,
                5:1100,
                6:1400,
                7:1700,
                8:2100,
                9:2400,
                10:2800,
                11:3600,
                12:4500,
                13:5100,
                14:5700,
                15:6400,
                16:7200,
                17:8800,
                18:9500,
                19:10900,
                20:12700
            }
        
        individual_xp_threshold = party_level_xp_values[self.party_level]
        self.xp_total = individual_xp_threshold * self.party_size

    def encounter_build(self):
        self.encounter_list.append(random.choice(self.mon_list))
        self.multiplier(len(self.encounter_list))
        for each in self.encounter_list:
            experience_change = self.multiplier_val * each[1]
        self.used_xp += experience_change


# Testing
encounter = Encounter()

encounter.terrain_choice = input("Select Terrain: ")
encounter.min_CR = int(input("Minimum CR for monsters? "))
encounter.max_CR = int(input("Maximum CR for monsters? "))
encounter.terrain()
encounter.party_level = int(input("Party Level? "))
encounter.party_size = int(input("Party Size? "))
encounter.threat = input("Encounter challenge? ")
encounter.difficulty()

print("Creating encounter with following parameters: ")
print("Encounter terrain: " + str(encounter.terrain_choice))
print("Encounter Min/Max CR: " + str(encounter.min_CR) + "/" + str(encounter.max_CR))
print("Total monsters available for selection: \n")
for each in encounter.mon_list:
    print(str(each))
print("\nParty level: " + str(encounter.party_level))
print("Party size: " + str(encounter.party_size))
print("Desired difficulty of encounter: " + str(encounter.threat))
print("Total xp available for distribution: " + str(encounter.xp_total))

while encounter.used_xp <= encounter.xp_total:
    encounter.encounter_build()
    print("Currently used xp: " + str(encounter.used_xp))

print(encounter.encounter_list)
