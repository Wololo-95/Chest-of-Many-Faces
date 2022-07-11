import random
from numpy.random import choice
import os

OUTPUT_FOLDER = "NPCs"

# Generates race with human bias, then elf (most cities in faerun are mostly populated by humans then elves)
# Slightly increased Tiefling bias for my own uses in Baldur's Gate - also plan to add other races
races = ["Human", "Elf", "Dwarf", "Halfling", "Tiefling", "Gnome", "Satyr", "Changeling"]
# Probabilities correspond 1:1 to the race list, modify to change frequency -- must equal 1 & be float
race = choice(races, 1, p=[0.40, 0.20, 0.12, 0.10, 0.14, 0.033, 0.002, 0.005])

# Determines sex - biased male for my own convenience, easier to voice male characters
sexes = ["Male", "Female"]
# Again, probability corresponds 1:1, values must be float
sex = choice(sexes, 1, p=[0.60, 0.40])

# Selects name based on race
name = ""
if race == "Human":  # Pulls if human
    if sex == "Male":  # Pulls if human and male
        with open("male human names", "r") as names:
            mh_list = names.readlines()  # goes through each line, and converts to list
            mh_list_filtered = []  # Creates empty list used to hold the name value
            mh_count = 0  # optional metric to gather the number of items in the list
            for each in mh_list:
                mh_count += 1
                mh_list_filtered.append(each.replace("\n", ""))  # Necessary step to remove the line breaks for items
        name = random.choice(mh_list_filtered)  # Chooses a random name from the filtered list, and assigns it
    if sex == "Female":  # Pulls if human and female
        with open("female human names", "r") as names:
            fh_list = names.readlines()
            fh_list_filtered = []
            fh_count = 0
            for each in fh_list:
                fh_count += 1
                fh_list_filtered.append(each.replace("\n", ""))
        name = random.choice(fh_list_filtered)
elif race == "Elf":  # Pulls if elf
    if sex == "Male":  # pulls if male and elf
        with open("male elf names", "r") as names:
            me_list = names.readlines()
            me_list_filtered = []
            me_count = 0
            for each in me_list:
                me_count += 1
                me_list_filtered.append(each.replace("\n", ""))
        name = random.choice(me_list_filtered)
    if sex == "Female":  # pulls if female and elf
        with open("female elf names", "r") as names:
            fe_list = names.readlines()
            fe_list_filtered = []
            fe_count = 0
            for each in fe_list:
                fe_count += 1
                fe_list_filtered.append(each.replace("\n", ""))
        name = random.choice(fe_list_filtered)
else:
    name = "Not Valid - under construction"  # Should never be reached - mostly placeholder for missing lists

# Generates alignment - no biases currently, difficult to ascertain motives of the average citizen
alignments = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil",
              "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
alignment = random.choice(alignments)

# Generates flaw(s)
with open("Flaws", "r") as flaws:  # opens document containing all the flaws separated by line
    flaw_list = flaws.readlines()  # iterates through to generate a python list
    flaw_list_filtered = []
    flaw_count = 0
    for each in flaw_list:
        flaw_count += 1  # iterates through to determine total number of flaws in list
        flaw_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
flaw = random.choice(flaw_list_filtered)  # chooses a random flaw from list

# Generates bond(s)
with open("Bonds", "r") as bonds:
    bond_list = bonds.readlines()
    bond_list_filtered = []
    bond_count = 0
    for each in bond_list:
        bond_count += 1
        bond_list_filtered.append(each.replace("\n", ""))
bond = random.choice(bond_list_filtered)

# Generates Personality Trait(s)
with open("Personality Traits", "r") as pt:
    pt_list = pt.readlines()
    pt_list_filtered = []
    pt_count = 0
    for each in pt_list:
        pt_count += 1
        pt_list_filtered.append(each.replace("\n", ""))
pt = random.choice(pt_list_filtered)

# Generates Ideal(s)
with open("Ideals", "r") as ideals:
    ideals_list = ideals.readlines()
    ideals_list_filtered = []
    ideals_count = 0
    for each in ideals_list:
        ideals_count += 1
        ideals_list_filtered.append(each.replace("\n", ""))
ideal = random.choice(ideals_list_filtered)

# Generates Quirk(s)
with open("Quirks", "r") as quirks:
    quirks_list = quirks.readlines()
    quirks_list_filtered = []
    quirks_count = 0
    for each in quirks_list:
        quirks_count += 1
        quirks_list_filtered.append(each.replace("\n", ""))
quirk = random.choice(quirks_list_filtered)

# Generates physical trait(s)
with open("Physical Traits", "r") as phys:
    phys_list = phys.readlines()
    phys_list_filtered = []
    phys_count = 0
    for each in phys_list:
        phys_count += 1
        phys_list_filtered.append(each.replace("\n", ""))
physical = random.choice(phys_list_filtered)

# attributes determined for below average (low as 7) and above average (high as 18)
status = ["Peasant", "Commoner", "Adventurer", "Aristocrat"]  # 4 levels of status, determines skills
social_status = choice(status, 1, p=[0.2, 0.5, 0.1, 0.2])
# Establish the variables to be referenced elsewhere
strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0
if social_status == "Peasant":  # peasants have skills between 7-10
    strength = random.randrange(7, 10)
    dexterity = random.randrange(7, 10)
    constitution = random.randrange(7, 10)
    intelligence = random.randrange(7, 10)
    wisdom = random.randrange(7, 10)
    charisma = random.randrange(7, 10)
elif social_status == "Commoner":  # commoners have skills between 8-14
    strength = random.randrange(8, 14)
    dexterity = random.randrange(8, 14)
    constitution = random.randrange(8, 14)
    intelligence = random.randrange(8, 14)
    wisdom = random.randrange(8, 14)
    charisma = random.randrange(8, 14)
elif social_status == "Adventurer":  # adventurers are 10-18, with emphasis on martial stats
    strength = random.randrange(10, 18)
    dexterity = random.randrange(10, 18)
    constitution = random.randrange(10, 18)
    intelligence = random.randrange(10, 16)
    wisdom = random.randrange(10, 16)
    charisma = random.randrange(10, 16)
elif social_status == "Aristocrat":  # Aristocrats have moderate stats with emphasis on charisma/wisdom
    strength = random.randrange(10, 16)
    dexterity = random.randrange(10, 14)
    constitution = random.randrange(10, 12)
    intelligence = random.randrange(10, 14)
    wisdom = random.randrange(10, 18)
    charisma = random.randrange(10, 18)
else:
    print("Invalid selection made for value 'social_status'")  # never reached

# System for determining the NPC's occupation, determined at random, may add system for bias with social status
occupation = ""  # Create variable to be called later
if social_status == "Peasant":
    occupations = ["Farmer", "Bar-hand", "Stable Boy/Girl", "Blacksmith - Weapons", "Farrier", "Leather-worker",
                   "Tanner", "Tailor", "Brewer", "Dyer", "Furrier", "Blacksmith - Armorer", "Parchment maker",
                   "Basket Weaver", "Food Vendor", "Unemployed", "Butcher", "Baker", "Stonemason", "Weaver", "Cobbler",
                   "Roofer", "Locksmith", "Carpenter", "Cook", "Unemployed - Shady or Illegal Business", "Miner",
                   "Woodcarver", "Wine Seller", "Torturer", "Tinker", "Toymaker", "Clergyman/woman", "Water Carrier",
                   "Builder", "Trapper", "Street Sweeper", "Thief", "Wrestler", "Gladiator", "Slave", "Potter",
                   "Ropemaker", "Rugmaker", "Seamster/tress", "Servant", "Pastry cook", "Plasterer", "Priest/ess",
                   "Professor", "Prostitute", "Alchemist", "Artist", "Fisherman", "Dock worker", "Latrine Cleaner",
                   "Beggar", "Unemployed"]
    occupation = random.choice(occupations)  # Peasants have no skill-based occupations
if social_status == "Commoner":
    occupations = ["Farmer", "Bar-hand", "Stable Boy/Girl", "Slave", "Servant", "Tailor", "Cook", "Prostitute",
                   "Torturer", "Jailer", "Roofer", "Toymaker", "Dock worker", "Water Carrier",
                   "Unemployed - Shady or illegal business", "Drunkard", "Latrine Cleaner", "Builder", "Unemployed",
                   "Butcher", "Baker", "Street Sweeper", "Seamster/tress", "Fisherman", "Beggar"]
    if strength > 10:
        strength_occupations = ["Blacksmith - Weapons", "Blacksmith - Armorer", "Stonemason", "Carpenter", "Builder",
                                "Gladiator", "Wrestler", "Woodcutter", "Miner", "Brick Maker", "Pirate", "Dock Worker",
                                "Fisherman", "Torturer", "Water Carrier", "Roofer", "Butcher" "Miner", "Gravekeeper",
                                "Buckle-maker", "Cobbler", "Farrier", "Guard (Town)", "Soldier"]
        for each in strength_occupations:
            occupations.append(each)
    if dexterity > 10:
        dexterity_occupations = ["Leather-worker", "Farrier", "Basket Weaver", "Weaver", "Silversmith", "Goldsmith",
                                 "Locksmith", "Thief", "Tinker", "Artist", "Wrestler", "Gladiator", "Ropemaker",
                                 "Seamster/tress", "Pirate", "Wood Carver", "Cobbler", "Fisherman", "Hunter",
                                 "Archer (Sport)", "Archer (Guard)", "Circus Performer", "Furrier", "Barber",
                                 "Seamster/tress", "Archer (Soldier)", "Crossbowman (Soldier)"]
        for each in dexterity_occupations:
            occupations.append(each)
    if constitution > 10:
        constitution_occupations = ["Gladiator", "Drunkard", "Wrestler", "Bodyguard", "Pirate", "Carpenter",
                                    "Blacksmith - Weapons", "Blacksmith - Armorer", "Butcher", "Dock Worker",
                                    "Beekeeper", "Latrine Cleaner", "Brewer", "Mortician", "Soldier"]
        for each in constitution_occupations:
            occupations.append(each)
    if intelligence > 10:
        intelligence_occupations = ["Alchemist", "Scholar", "Professor", "Artist", "Tinker", "Inventor",
                                    "Historian", "Wizard's Apprentice", "Herbalist", "Brewer", "Poisoner",
                                    "Architect", "Scrivener", "Scribe", "Magic Item Enthusiast", "Arcanist",
                                    "Librarian", "Translator", "Mathematician", "Investigator", "Vendor - Books",
                                    "Wine Maker", "Nurse", "Doctor"]
        for each in intelligence_occupations:
            occupations.append(each)
    if wisdom > 10:
        wisdom_occupations = ["Clergyman/woman", "Priest/Priestess", "Farrier", "Naturalist", "Herbalist", "Poisoner",
                              "Alchemist", "Trapper", "Stable Manager", "Animal Breeder", "Vendor - General",
                              "Vendor - Spices", "Vendor - Wood", "Vendor - Alcohol", "Vendor - Books",
                              "Vendor - Jewelry", "Artist", "Vendor - Furs", "Vendor - Food", "Vendor - Meat",
                              "Dyer", "Beekeeper", "Philosopher", "Cleric's Assistant", "Rug Maker", "Furrier", "Scout",
                              "Watchman (guard)", "Barber"]
        for each in wisdom_occupations:
            occupations.append(each)
    if charisma > 10:
        charisma_occupations = ["Town Crier", "Vendor - General", "Vendor - Spices", "Vendor - Wood",
                                "Vendor - Alcohol", "Vendor - Books", "Vendor - Jewelry", "Artist", "Vendor - Furs",
                                "Vendor - Food", "Vendor - Meat", "Charlatan", "Gambler", "Warlock's Apprentice",
                                "Drunkard", "Entertainer", "Circus Performer", "Musician", "Interrogator", "Salesman",
                                "Writer", "Poet", "Public Speaker"]
        for each in charisma_occupations:
            occupations.append(each)
    occupation = random.choice(occupations)  # each position is based on the skills of the NPC
    # Duplicates serve to reinforce that x would be a good career for the given NPC

if social_status == "Adventurer":  # Adventurers will choose more rare careers
    occupations = ["Odd Jobs - Adventurer", "Unemployed", "Unemployed - Shady or Illegal Business"]
    if strength or dexterity or constitution > 12:
        martial_careers = ["Bounty Hunter", "Hunter", "Fighter", "Odd Jobs - Adventurer", "Unemployed",
                           "Guard", "Guard-for-hire", "Sword-for-hire", "Tax Collector", "Ranger", "Pirate", "Paladin",
                           "Soldier", "Outlander", "Squire"]
        for each in martial_careers:
            occupations.append(each)
    if intelligence > 12:
        intelligence_occupations = ["Scholar", "Alchemist", "Wizard", "Necromancer", "Investigator", "Conjurer"]
        for each in intelligence_occupations:
            occupations.append(each)
    if wisdom > 12:
        wisdom_occupations = ["Philosopher", "Druid", "Cleric", "Inquisitor", "Ranger", "Outlander", "Paladin"]
        for each in wisdom_occupations:
            occupations.append(each)
    if charisma > 12:
        charisma_occupations = ["Sorcerer/Sorceress", "Tax Collector", "Pirate", "Bard", "Squire", "Musician"]
        for each in charisma_occupations:
            occupations.append(each)
    occupation = random.choice(occupations)

if social_status == "Aristocrat":  # Aristocrats will likely be involved with guilds, merchants or politics
    occupations = ["Lord/Lady", "Nobleman/woman"]
    if strength > 12 and constitution > 12:  # Martial and Soldier Careers
        martial_careers = ["Commander - Army", "Commander - Guard", "Knight", "Soldier", "Squire"]
        for each in martial_careers:
            occupations.append(each)
    elif charisma > 12:  # Politician and orator careers
        oration_careers = ["Politician - Councilman/Senator", "Politician - Mayor/Count", "Politician - Magistrate",
                           "Advocate (Lawyer)", "Diplomat", "Interpreter", "Interrogator"]
        for each in oration_careers:
            occupations.append(each)
    elif intelligence > 13:
        intelligence_careers = ["Investor", "Inventor", "Historian", "Scholar", "Architect", "Doctor", "Surgeon"]
        for each in intelligence_careers:
            occupations.append(each)
    elif wisdom > 12:  # Wise investor/businessperson careers
        business_careers = ["Investor", "Brothel Keeper", "Caravan Leader", "Inn Owner", "Merchant"]
        for each in business_careers:
            occupations.append(each)
    else:
        occupation = "Unemployed"
    occupation = random.choice(occupations)

# Wealth statuses
wealth = ""
if social_status == "Peasant":
    wealth_options = ["Wretched", "Squalid", "Poor", "Modest"]
    wealth = choice(wealth_options, 1, p=[0.2, 0.35, 0.35, 0.1])
elif social_status == "Commoner":
    wealth_options = ["Squalid", "Poor", "Modest", "Comfortable"]
    wealth = choice(wealth_options, 1, p=[0.25, 0.4, 0.25, 0.1])
elif social_status == "Adventurer":
    wealth_options = ["Poor", "Modest", "Comfortable", "Wealthy", "Aristocratic"]
    wealth = choice(wealth_options, 1, p=[0.05, 0.15, 0.45, 0.3, 0.05])
elif social_status == "Peasant":
    wealth_options = ["Modest", "Comfortable", "Wealthy", "Aristocratic"]
    wealth = choice(wealth_options, 1, p=[0.1, 0.3, 0.3, 0.3])

# File write and output
filename = "{}.txt".format(name)  # Uses name variable to name the file for ease of access
file = open(filename, 'w')  # Opens document to log generation & for future reference
file.write("BASIC INFO\n\n")
file.write("Race: {}\n".format(race))
file.write("Sex: {}\n".format(sex))
file.write("Name: {}\n".format(name))
file.write("Alignment: {}\n".format(alignment))
file.write("-------------------------\n\n")
file.write("TRAITS/FLAWS \n\n")
file.write("Bond: {}\n".format(bond))
file.write("Flaw: {}\n".format(flaw))
file.write("Personality trait: {}\n".format(pt))
file.write("Ideal: {}\n".format(ideal))
file.write("------------------------\n\n")
file.write("QUIRK/PHYSICAL TRAIT\n\n")
file.write("Quirk: {}\n".format(quirk))
file.write("Physical Trait: {}\n".format(physical))
file.write("------------------------\n\n")
file.write("ATTRIBUTES, GOALS, OCCUPATIONS\n\n")
file.write("Social Class: {}\n".format(social_status))
file.write("Occupation: {}\n".format(occupation))
file.write("Goal:\n")
file.write("Wealth Status: {}\n\n".format(wealth))

file.write("Strength: {}\n".format(strength))
file.write("Dexterity: {}\n".format(dexterity))
file.write("Constitution: {}\n".format(constitution))
file.write("Intelligence: {}\n".format(intelligence))
file.write("Wisdom: {}\n".format(wisdom))
file.write("Charisma: {}\n".format(charisma))

file.close()  # Safely closes the new document
os.rename(filename, "{}/{}".format(OUTPUT_FOLDER, filename))  # Searches for path NPCs/name to move document
print("File {} is complete!\n".format(filename))

# Prints to console for local use
print("NPC Generator [Version 1]")
print("-------------------------")
print("Race: " + str(race))
print("Sex: " + str(sex))
print("Name: " + name)
print(name + " is " + alignment)
print("-------------------------\n")
print("Bond: " + bond)
print("Flaw: " + flaw)
print("Personality Trait: " + pt)
print("Ideal: " + ideal)
print("-------------------------\n")
print("Quirk: " + quirk)
print("Physical Trait: " + physical)
print("-------------------------\n")
print("Social Class: " + str(social_status))
print("Occupation: " + str(occupation))
print("Wealth Status: " + str(wealth))
print("Goal: FEATURE TBA \n\n")
print("Attribute Array:")
print("Strength: " + str(strength))
print("Dexterity: " + str(dexterity))
print("Constitution: " + str(constitution))
print("Intelligence: " + str(intelligence))
print("Wisdom: " + str(wisdom))
print("Charisma: " + str(charisma))
