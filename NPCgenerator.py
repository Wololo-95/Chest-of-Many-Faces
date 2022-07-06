import random

# Generates race with human bias, then elf (most cities in faerun are mostly populated by humans)
# Slightly increased tiefling bias for my own uses in Baldur's Gate
# Will eventually create actual system to account and select for biases
races = ["Human", "Human", "Human", "Human", "Human", "Human", "Human", "elf", "elf", "elf", "elf", "elf", "dwarf",
         "dwarf", "dwarf", "halfling", "halfling", "halfling", "Tiefling", "Tiefling", "gnome", "Satyr", "Changeling"]
race = random.choice(races)

# Determines sex
sexes = ["Male", "Female"]
sex = random.choice(sexes)

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
    print("Number of Male Human names in list: " + str(mh_count))
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
print("Number of total flaws in list: " + str(flaw_count))

# Generates bond(s)
with open("Bonds", "r") as bonds:  # opens document containing all the bonds separated by line
    bond_list = bonds.readlines()  # iterates through to generate a python list
    bond_list_filtered = []
    bond_count = 0
    for each in bond_list:
        bond_count += 1  # iterates through to determine total number of bonds in list
        bond_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
bond = random.choice(bond_list_filtered)  # chooses a random bond from list
print("Number of total bonds in list: " + str(bond_count))

# Generates Personality Trait(s)
with open("Personality Traits", "r") as pt:  # opens document containing all the traits separated by line
    pt_list = pt.readlines()  # iterates through to generate a python list
    pt_list_filtered = []
    pt_count = 0
    for each in pt_list:
        pt_count += 1  # iterates through to determine total number of traits in list
        pt_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
pt = random.choice(pt_list_filtered)  # chooses a random trait from list
print("Number of total personality traits in list: " + str(pt_count))

# Generates Ideal(s)
with open("Ideals", "r") as ideals:  # opens document containing all the ideals separated by line
    ideals_list = ideals.readlines()  # iterates through to generate a python list
    ideals_list_filtered = []
    ideals_count = 0
    for each in ideals_list:
        ideals_count += 1  # iterates through to determine total number of ideals in list
        ideals_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
ideal = random.choice(ideals_list_filtered)  # chooses a random ideal from list
print("Number of total ideals in list: " + str(ideals_count))

# Generates Quirk(s)
with open("Quirks", "r") as quirks:  # opens document containing all the quirks separated by line
    quirks_list = quirks.readlines()  # iterates through to generate a python list
    quirks_list_filtered = []
    quirks_count = 0
    for each in quirks_list:
        quirks_count += 1  # iterates through to determine total number of quirks in list
        quirks_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
quirk = random.choice(quirks_list_filtered)  # chooses a random quirk from list
print("Number of total quirks in list: " + str(quirks_count))

# Generates physical trait(s)
with open("Physical Traits", "r") as phys:  # opens document containing all the phys traits separated by line
    phys_list = phys.readlines()  # iterates through to generate a python list
    phys_list_filtered = []
    phys_count = 0
    for each in phys_list:
        phys_count += 1  # iterates through to determine total number of traits in list
        phys_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
physical = random.choice(phys_list_filtered)  # chooses a random trait from list
print("Number of total physical traits in list: " + str(phys_count))


print("--------------------------------")
print("Name:")
print(name)
print("Race:")
print(race)
print("Sex:")
print(sex)
print("")
print("Alignment:")
print(alignment)
print("Flaw:")
print(flaw)
print("Bond:")
print(bond)
print("Personality Trait:")
print(pt)
print("Ideal:")
print(ideal)
print("")

print("Quirk:")
print(quirk)
print("Physical trait:")
print(physical)

