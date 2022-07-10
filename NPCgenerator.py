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
if race == "Human" and sex == "Male":
    with open("male human names", "r") as names:
        mh_list = names.readlines()
        mh_list_filtered = []
        mh_count = 0
        for each in mh_list:
            mh_count += 1
            mh_list_filtered.append(each.replace("\n", ""))
    name = random.choice(mh_list_filtered)
elif race == "Human" and sex == "Female":
    with open("female human names", "r") as names:
        fh_list = names.readlines()
        fh_list_filtered = []
        fh_count = 0
        for each in fh_list:
            fh_count += 1
            fh_list_filtered.append(each.replace("\n", ""))
    name = random.choice(fh_list_filtered)
elif race == "Elf" and sex == "Male":
    with open("male elf names", "r") as names:
        me_list = names.readlines()
        me_list_filtered = []
        me_count = 0
        for each in me_list:
            me_count += 1
            me_list_filtered.append(each.replace("\n", ""))
    name = random.choice(me_list_filtered)
elif race == "Elf" and sex == "Female":
    with open("female elf names", "r") as names:
        fe_list = names.readlines()
        fe_list_filtered = []
        fe_count = 0
        for each in fe_list:
            fe_count += 1
            fe_list_filtered.append(each.replace("\n", ""))
    name = random.choice(fe_list_filtered)
else:
    name = "Not Valid - under construction"
    # Generates alignment
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
with open("Bonds", "r") as bonds:  # opens document containing all the bonds separated by line
    bond_list = bonds.readlines()  # iterates through to generate a python list
    bond_list_filtered = []
    bond_count = 0
    for each in bond_list:
        bond_count += 1  # iterates through to determine total number of bonds in list
        bond_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
bond = random.choice(bond_list_filtered)  # chooses a random bond from list

# Generates Personality Trait(s)
with open("Personality Traits", "r") as pt:  # opens document containing all the traits separated by line
    pt_list = pt.readlines()  # iterates through to generate a python list
    pt_list_filtered = []
    pt_count = 0
    for each in pt_list:
        pt_count += 1  # iterates through to determine total number of traits in list
        pt_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
pt = random.choice(pt_list_filtered)  # chooses a random trait from list

# Generates Ideal(s)
with open("Ideals", "r") as ideals:  # opens document containing all the ideals separated by line
    ideals_list = ideals.readlines()  # iterates through to generate a python list
    ideals_list_filtered = []
    ideals_count = 0
    for each in ideals_list:
        ideals_count += 1  # iterates through to determine total number of ideals in list
        ideals_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
ideal = random.choice(ideals_list_filtered)  # chooses a random ideal from list

# Generates Quirk(s)
with open("Quirks", "r") as quirks:  # opens document containing all the quirks separated by line
    quirks_list = quirks.readlines()  # iterates through to generate a python list
    quirks_list_filtered = []
    quirks_count = 0
    for each in quirks_list:
        quirks_count += 1  # iterates through to determine total number of quirks in list
        quirks_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
quirk = random.choice(quirks_list_filtered)  # chooses a random quirk from list


# Generates physical trait(s)
with open("Physical Traits", "r") as phys:  # opens document containing all the phys traits separated by line
    phys_list = phys.readlines()  # iterates through to generate a python list
    phys_list_filtered = []
    phys_count = 0
    for each in phys_list:
        phys_count += 1  # iterates through to determine total number of traits in list
        phys_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
physical = random.choice(phys_list_filtered)  # chooses a random trait from list

# attributes determined for below average (low as 7) and above average (high as 16)
status = ["Peasant", "Commoner", "Adventurer", "Aristocrat"]
social_status = choice(status, 1, p=[0.2, 0.5, 0.1, 0.2])
strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0
if social_status == "Peasant":
    strength = random.randrange(7, 10)
    dexterity = random.randrange(7, 10)
    constitution = random.randrange(7, 10)
    intelligence = random.randrange(7, 10)
    wisdom = random.randrange(7, 10)
    charisma = random.randrange(7, 10)
elif social_status == "Commoner":
    strength = random.randrange(8, 14)
    dexterity = random.randrange(8, 14)
    constitution = random.randrange(8, 14)
    intelligence = random.randrange(8, 14)
    wisdom = random.randrange(8, 14)
    charisma = random.randrange(8, 14)
elif social_status == "Adventurer":
    strength = random.randrange(10, 16)
    dexterity = random.randrange(10, 16)
    constitution = random.randrange(10, 16)
    intelligence = random.randrange(10, 16)
    wisdom = random.randrange(10, 16)
    charisma = random.randrange(10, 16)
elif social_status == "Aristocrat":
    strength = random.randrange(10, 14)
    dexterity = random.randrange(10, 14)
    constitution = random.randrange(10, 12)
    intelligence = random.randrange(10, 14)
    wisdom = random.randrange(10, 16)
    charisma = random.randrange(10, 18)
else:
    print("Invalid selection made for value 'social_status'")


# File write and output
filename = "{}.txt".format(name)
file = open(filename, 'w')
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
file.write("ATTRIBUTES\n\n")
file.write("Social Class: {}\n\n".format(social_status))
file.write("Strength: {}\n".format(strength))
file.write("Dexterity: {}\n".format(dexterity))
file.write("Constitution: {}\n".format(constitution))
file.write("Intelligence: {}\n".format(intelligence))
file.write("Wisdom: {}\n".format(wisdom))
file.write("Charisma: {}\n".format(charisma))

file.close()
os.rename(filename, "{}/{}".format(OUTPUT_FOLDER, filename))
print("File {} is complete!\n".format(filename))


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
print("Attribute Array:")
print("Strength: " + str(strength))
print("Dexterity: " + str(dexterity))
print("Constitution: " + str(constitution))
print("Intelligence: " + str(intelligence))
print("Wisdom: " + str(wisdom))
print("Charisma: " + str(charisma))