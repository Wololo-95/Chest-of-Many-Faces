import random
from numpy.random import choice


def basic_info():
    # Generates race with human bias, then elf (most cities in faerun are mostly populated by humans then elves)
    # Slightly increased Tiefling bias for my own uses in Baldur's Gate - also plan to add other races
    races = ["Human", "Elf", "Dwarf", "Halfling", "Tiefling", "Gnome", "Satyr", "Changeling"]
    # Probabilities correspond 1:1 to the race list, modify to change frequency -- must equal 1 & be float
    race = choice(races, 1, p=[0.40, 0.20, 0.12, 0.10, 0.14, 0.033, 0.002, 0.005])
    print("Race: " + str(race))

    # Determines sex - biased male for my own convenience, easier to voice male characters
    sexes = ["Male", "Female"]
    # Again, probability corresponds 1:1, values must be float
    sex = choice(sexes, 1, p=[0.60, 0.40])
    print("Sex: " + str(sex))

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
        print("Name: " + name)
    elif race == "Human" and sex == "Female":
        with open("female human names", "r") as names:
            fh_list = names.readlines()
            fh_list_filtered = []
            fh_count = 0
            for each in fh_list:
                fh_count += 1
                fh_list_filtered.append(each.replace("\n", ""))
        name = random.choice(fh_list_filtered)
        print("Name: " + name)
    elif race == "Elf" and sex == "Male":
        with open("male elf names", "r") as names:
            me_list = names.readlines()
            me_list_filtered = []
            me_count = 0
            for each in me_list:
                me_count += 1
                me_list_filtered.append(each.replace("\n", ""))
        name = random.choice(me_list_filtered)
        print("Name: " + name)
    elif race == "Elf" and sex == "Female":
        with open("female elf names", "r") as names:
            fe_list = names.readlines()
            fe_list_filtered = []
            fe_count = 0
            for each in fe_list:
                fe_count += 1
                fe_list_filtered.append(each.replace("\n", ""))
        name = random.choice(fe_list_filtered)
        print("Name: " + name)
    else:
        name = "Not Valid - under construction"
        print("Name: " + name)
        # Generates alignment
    alignments = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil",
                  "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
    alignment = random.choice(alignments)
    print(name + " is " + alignment)
    print("")
    print("-------------------------")
    print("")


def flaw():
    # Generates flaw(s)
    with open("Flaws", "r") as flaws:  # opens document containing all the flaws separated by line
        flaw_list = flaws.readlines()  # iterates through to generate a python list
        flaw_list_filtered = []
        flaw_count = 0
        for each in flaw_list:
            flaw_count += 1  # iterates through to determine total number of flaws in list
            flaw_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
    flaw = random.choice(flaw_list_filtered)  # chooses a random flaw from list
    print("Flaw: " + flaw)


def bond():
    # Generates bond(s)
    with open("Bonds", "r") as bonds:  # opens document containing all the bonds separated by line
        bond_list = bonds.readlines()  # iterates through to generate a python list
        bond_list_filtered = []
        bond_count = 0
        for each in bond_list:
            bond_count += 1  # iterates through to determine total number of bonds in list
            bond_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
    bond = random.choice(bond_list_filtered)  # chooses a random bond from list
    print("Bond: " + bond)


def trait():
    # Generates Personality Trait(s)
    with open("Personality Traits", "r") as pt:  # opens document containing all the traits separated by line
        pt_list = pt.readlines()  # iterates through to generate a python list
        pt_list_filtered = []
        pt_count = 0
        for each in pt_list:
            pt_count += 1  # iterates through to determine total number of traits in list
            pt_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
    pt = random.choice(pt_list_filtered)  # chooses a random trait from list
    print("Personality Trait: " + pt)


def ideal():
    # Generates Ideal(s)
    with open("Ideals", "r") as ideals:  # opens document containing all the ideals separated by line
        ideals_list = ideals.readlines()  # iterates through to generate a python list
        ideals_list_filtered = []
        ideals_count = 0
        for each in ideals_list:
            ideals_count += 1  # iterates through to determine total number of ideals in list
            ideals_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
    ideal = random.choice(ideals_list_filtered)  # chooses a random ideal from list
    print("Ideal: " + ideal)
    print("")
    print("-------------------------")
    print("")


def quirk():
    # Generates Quirk(s)
    with open("Quirks", "r") as quirks:  # opens document containing all the quirks separated by line
        quirks_list = quirks.readlines()  # iterates through to generate a python list
        quirks_list_filtered = []
        quirks_count = 0
        for each in quirks_list:
            quirks_count += 1  # iterates through to determine total number of quirks in list
            quirks_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
    quirk = random.choice(quirks_list_filtered)  # chooses a random quirk from list
    print("Quirk: " + quirk)


def phys_trait():
    # Generates physical trait(s)
    with open("Physical Traits", "r") as phys:  # opens document containing all the phys traits separated by line
        phys_list = phys.readlines()  # iterates through to generate a python list
        phys_list_filtered = []
        phys_count = 0
        for each in phys_list:
            phys_count += 1  # iterates through to determine total number of traits in list
            phys_list_filtered.append(each.replace("\n", ""))  # removes each line break in list
    physical = random.choice(phys_list_filtered)  # chooses a random trait from list
    print("Physical Trait: " + physical)
    print("")
    print("-------------------------")
    print("")


print("Npc Generator - Version 1")
print("-------------------------")
basic_info()
flaw()
bond()
trait()
ideal()
quirk()
phys_trait()
