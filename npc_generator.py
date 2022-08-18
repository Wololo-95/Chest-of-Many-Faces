from importlib.resources import path
import random
import os
from numpy.random import choice

class NpcGenerator():
    def __init__(self):
        self.name = ""
        self.race = ""
        self.sex = ""
        self.alignment = ""
        self.MAXIMUM_ATTRIBUTE_SCORE = 14
        self.MINIMUM_ATTRIBUTE_SCORE = 6
        self.attribute_scores = []
        self.pt = ""
        self.quirk = ""
        self.ideal = ""
        self.bond = ""
        self.flaw = ""
        self.physical = ""
        self.traits = []
        # separate attribute score lineup so that if a user desires to manually set their attributes, they can
        self.custom_attributes_enabled = False
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        # designates target folder for saved NPCs, folder must exist before running generator or it will be saved locally.
        self.OUTPUT_FOLDER = "NPCs"
        
    def race_gen(self):  # races are biased towards the earlier part of the list, as these are more prevalent races in major cities
        races = ["Human", "Elf", "Dwarf", "Half-Elf", "Tiefling", "Halfling", "Half-Orc", "Dragonborn", "Gnome", "Goblin", "Hobgoblin", "Drow",  "Satyr", "Changeling"]
        self.race = choice(races, 1, p=[0.23, 0.20, 0.10, 0.10, 0.10, 0.05, 0.05, 0.04, 0.03, 0.03, 0.02, 0.02, 0.02, 0.01])
        
    def sex_gen(self):
        sexes = ["Male", "Female"]
        self.sex = choice(sexes, 1, p=[0.60, 0.40])
        
    def name_gen(self):
        if self.race == "Human":
            if self.sex == "Male":
                with open("names/male human names", "r") as names:  # All names are saved in txt docs locally to save processing power and document space to exponentially increase num of options
                    import_male_human_names = names.readlines()
                    male_human_names = []
                    for each in import_male_human_names:
                        male_human_names.append(each.replace("\n", ""))
                self.name = random.choice(male_human_names)
            elif self.sex == "Female":
                with open("names/female human names", "r") as names:
                    import_female_human_names = names.readlines()
                    female_human_names = []
                    for each in import_female_human_names:
                        female_human_names.append(each.replace("\n", ""))
                self.name = random.choice(female_human_names)
        elif self.race == "Elf":
            if self.sex == "Male":
                with open ("names/male elf names", "r") as names:
                    import_male_elf_names = names.readlines()
                    male_elf_names = []
                    for each in import_male_elf_names:
                        male_elf_names.append(each.replace("\n", ""))
                self.name = random.choice(male_elf_names)
            elif self.sex == "Female":
                with open ("names/female elf names", "r") as names:
                    import_female_elf_names = names.readlines()
                    female_elf_names = []
                    for each in import_female_elf_names:
                        female_elf_names.append(each.replace("\n", ""))
                self.name = random.choice(female_elf_names)
        elif self.race == "Dwarf":
            if self.sex == "Male":
                with open("names/male dwarf names", "r") as names:
                    import_male_dwarf_names = names.readlines()
                    male_dwarf_names = []
                    for each in import_male_dwarf_names:
                        male_dwarf_names.append(each.replace("\n", ""))
                self.name = random.choice(male_dwarf_names)
            elif self.sex == "Female":
                with open("names/female dwarf names", "r") as names:
                    import_female_dwarf_names = names.readlines()
                    female_dwarf_names = []
                    for each in import_female_dwarf_names:
                        female_dwarf_names.append(each.replace("\n", ""))
                self.name = random.choice(female_dwarf_names)
        elif self.race == "Half-Elf":
            if self.sex == "Male":
                with open("names/male half elf names", "r") as names:
                    import_male_halfelf_names = names.readlines()
                    male_halfelf_names = []
                    for each in import_male_halfelf_names:
                        male_halfelf_names.append(each.replace("\n", ""))
                self.name = random.choice(male_halfelf_names)
            elif self.sex == "Female":
                with open("names/female half elf names", "r") as names:
                    import_female_halfelf_names = names.readlines()
                    female_halfelf_names = []
                    for each in import_female_halfelf_names:
                        female_halfelf_names.append(each.replace("\n", ""))
                self.name = random.choice(female_halfelf_names)
        elif self.race == "Tiefling":
            if self.sex == "Male":
                with open("names/male tiefling names", "r") as names:
                    import_male_tiefling_names = names.readlines()
                    male_tiefling_names = []
                    for each in import_male_tiefling_names:
                        male_tiefling_names.append(each.replace("\n", ""))
                self.name = random.choice(male_tiefling_names)
            elif self.sex == "Female":
                with open("names/female tiefling names", "r") as names:
                    import_female_tiefling_names = names.readlines()
                    female_tiefling_names = []
                    for each in import_female_tiefling_names:
                        female_tiefling_names.append(each.replace("\n", ""))
                self.name = random.choice(female_tiefling_names)
        elif self.race == "Halfling":
            if self.sex == "Male":
                with open("names/male halfling names", "r") as names:
                    import_male_halfling_names = names.readlines()
                    male_halfling_names = []
                    for each in import_male_halfling_names:
                        male_halfling_names.append(each.replace("\n", ""))
                self.name = random.choice(male_halfling_names)
            elif self.sex == "Female":
                with open("names/female halfling names", "r") as names:
                    import_female_halfling_names = names.readlines()
                    female_halfling_names = []
                    for each in import_female_halfling_names:
                        female_halfling_names.append(each.replace("\n", ""))
                self.name = random.choice(female_halfling_names)
        elif self.race == "Half-Orc":
            if self.sex == "Male":
                with open("names/male half orc names", "r") as names:
                    import_male_halforc_names = names.readlines()
                    male_halforc_names = []
                    for each in import_male_halforc_names:
                        male_halforc_names.append(each.replace("\n", ""))
                self.name = random.choice(male_halforc_names)
            elif self.sex == "Female":
                with open("names/female half orc names", "r") as names:
                    import_female_halforc_names = names.readlines()
                    female_halforc_names = []
                    for each in import_female_halforc_names:
                        female_halforc_names.append(each.replace("\n", ""))
                self.name = random.choice(female_halforc_names)
        elif self.race == "Dragonborn":
            if self.sex == "Male":
                with open("names/male dragonborn names", "r") as names:
                    import_male_dragonborn_names = names.readlines()
                    male_dragonborn_names = []
                    for each in import_male_dragonborn_names:
                        male_dragonborn_names.append(each.replace("\n", ""))
                self.name = random.choice(male_dragonborn_names)
            elif self.sex == "Female":
                with open("names/female dragonborn names", "r") as names:
                    import_female_dragonborn_names = names.readlines()
                    female_dragonborn_names = []
                    for each in import_female_dragonborn_names:
                        female_dragonborn_names.append(each.replace("\n", ""))
                self.name = random.choice(female_dragonborn_names)
        elif self.race == "Gnome":
            if self.sex == "Male":
                with open("names/male gnome names", "r") as names:
                    import_male_gnome_names = names.readlines()
                    male_gnome_names = []
                    for each in import_male_gnome_names:
                        male_gnome_names.append(each.replace("\n", ""))
                self.name = random.choice(male_gnome_names)
            elif self.sex == "Female":
                with open("names/female gnome names", "r") as names:
                    import_female_gnome_names = names.readlines()
                    female_gnome_names = []
                    for each in import_female_gnome_names:
                        female_gnome_names.append(each.replace("\n", ""))
                self.name = random.choice(female_gnome_names)
        elif self.race == "Goblin":
            if self.sex == "Male":
                with open("names/male goblin names", "r") as names:
                    import_male_goblin_names = names.readlines()
                    male_goblin_names = []
                    for each in import_male_goblin_names:
                        male_goblin_names.append(each.replace("\n", ""))
                self.name = random.choice(male_goblin_names)
            elif self.sex == "Female":
                with open("names/female goblin names", "r") as names:
                    import_female_goblin_names = names.readlines()
                    female_goblin_names = []
                    for each in import_female_goblin_names:
                        female_goblin_names.append(each.replace("\n", ""))
                self.name = random.choice(female_goblin_names)
        elif self.race == "Hobgoblin":
            if self.sex == "Male":
                with open("names/male hobgoblin names", "r") as names:
                    import_male_hobgoblin_names = names.readlines()
                    male_hobgoblin_names = []
                    for each in import_male_hobgoblin_names:
                        male_hobgoblin_names.append(each.replace("\n", ""))
                self.name = random.choice(male_hobgoblin_names)
            elif self.sex == "Female":
                with open("names/female hobgoblin names", "r") as names:
                    import_female_hobgoblin_names = names.readlines()
                    female_hobgoblin_names = []
                    for each in import_female_hobgoblin_names:
                        female_hobgoblin_names.append(each.replace("\n", ""))
                self.name = random.choice(female_hobgoblin_names)
        elif self.race == "Drow":
            if self.sex == "Male":
                with open("names/male drow names", "r") as names:
                    import_male_drow_names = names.readlines()
                    male_drow_names = []
                    for each in import_male_drow_names:
                        male_drow_names.append(each.replace("\n", ""))
                self.name = random.choice(male_drow_names)
            elif self.sex == "Female":
                with open("names/female drow names", "r") as names:
                    import_female_drow_names = names.readlines()
                    female_drow_names = []
                    for each in import_female_drow_names:
                        female_drow_names.append(each.replace("\n", ""))
                self.name = random.choice(female_drow_names)
        elif self.race == "Satyr":
            if self.sex == "Male":
                with open("names/male satyr names", "r") as names:
                    import_male_satyr_names = names.readlines()
                    male_satyr_names = []
                    for each in import_male_satyr_names:
                        male_satyr_names.append(each.replace("\n", ""))
                self.name = random.choice(male_satyr_names)
            elif self.sex == "Female":
                with open("names/female satyr names", "r") as names:
                    import_female_satyr_names = names.readlines()
                    female_satyr_names = []
                    for each in import_female_satyr_names:
                        female_satyr_names.append(each.replace("\n", ""))
                self.name = random.choice(female_satyr_names)
        elif self.race == "Changeling":
            with open("names/changeling names", "r") as names:  # Changelings are intentionally left sexless due to their mutable form
                import_changeling_names = names.readlines()
                changeling_names = []
                for each in import_changeling_names:
                    changeling_names.append(each.replace("\n", ""))
            self.name = random.choice(changeling_names)
        else:
            return "Invalid Race Selection - or - No Available Names"

    def alignment_gen(self):
        alignments = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
        self.alignment = random.choice(alignments)  # alignments are not biased currently, a random character can be chaotic evil without reason, they simply do not need to act on it
    
    def flaw_gen(self):
        with open("personalityelements/Flaws", "r") as flaws:
            flaw_options = flaws.readlines()
            flaw_list = []
            for each in flaw_options:
                flaw_list.append(each.replace("\n", "")) 
        self.flaw = random.choice(flaw_list)

    def bond_gen(self):
        with open("personalityelements/Bonds", "r") as bonds:
            bond_options = bonds.readlines()
            bond_list = []
            for each in bond_options:
                bond_list.append(each.replace("\n", "")) 
        self.bond = random.choice(bond_list)

    def personality_gen(self):
        with open("personalityelements/Personality Traits", "r") as ptraits:
            pt_options = ptraits.readlines()
            pt_list = []
            for each in pt_options:
                pt_list.append(each.replace("\n", "")) 
        self.pt = random.choice(pt_list)

    def ideal_gen(self):
        with open("personalityelements/Ideals", "r") as ideals:
            ideal_options = ideals.readlines()
            ideal_list = []
            for each in ideal_options:
                ideal_list.append(each.replace("\n", "")) 
        self.ideal = random.choice(ideal_list)

    def quirk_gen(self):
        with open("personalityelements/Quirks", "r") as quirks:
            quirk_options = quirks.readlines()
            quirk_list = []
            for each in quirk_options:
                quirk_list.append(each.replace("\n", "")) 
        self.quirk = random.choice(quirk_list)

    def physical_gen(self):
        with open("personalityelements/Physical Traits", "r") as physicals:
            phys_options = physicals.readlines()
            phys_list = []
            for each in phys_options:
                phys_list.append(each.replace("\n", "")) 
        self.physical = random.choice(phys_list)
    
    def attributes_gen(self):  # Uses dictionary to create attributes, then writes them to an ability list for later reference
        abilities = []
        skills = {"Strength":8, "Dexterity":8, "Constitution":8, "Intelligence":8, "Wisdom":8, "Charisma":8}  # sets baseline for stats in the event that it does not generate a stat array.
        for each in skills:
            skills[each] = random.randint(self.MINIMUM_ATTRIBUTE_SCORE,self.MAXIMUM_ATTRIBUTE_SCORE)
        
        for ability, score in skills.items():
            abilities.append(str(ability) + ": " + str(score))
        self.attribute_scores = abilities

    def custom_attribute_selection(self):
        self.custom_attributes_enabled = True
        
    def display(self):  # Returns in-terminal output of the generated NPC
        print("NPC Generated! \n")
        print("Name: ", self.name)
        print("Race: ", self.race)
        print("Sex: ", self.sex)
        print("Alignment: ", self.alignment)
        for each in self.attribute_scores:
            print(each)
        print("\n")
        for each in self.traits:
            print(each)
            
    def output(self):  # Writes the NPC to file for reference
        filename = "{}.txt".format(self.name)
        file = open(filename, "w")
        file.write("Name: {}\n".format(self.name))
        file.write("Race: {} {}\n".format(str(self.sex),str(self.race)))
        file.write("Alignment: {}\n\n".format(self.alignment))

        file.write("-------ATTRIBUTE SCORE ARRAY-------\n")
        if self.custom_attributes_enabled == True:
            file.write("Strength: " + str(self.strength) + "\n")
            file.write("Dexterity: " + str(self.dexterity) + "\n")
            file.write("Constitution: " + str(self.constitution) + "\n")
            file.write("Intelligence: " + str(self.intelligence) + "\n")
            file.write("Wisdom: " + str(self.wisdom) + "\n")
            file.write("Charisma: " + str(self.charisma) + "\n")
        elif self.custom_attributes_enabled == False:
            for each in self.attribute_scores:
                file.write(each + "\n")

        file.write("\n\n")
        file.write("-------TRAITS AND FLAWS-------\n")
        for each in self.traits:
            file.write(each)
            file.write("\n")

        file.close()
        os.rename(filename, "{}/{}".format(self.OUTPUT_FOLDER, filename))
        path = os.path.abspath(filename)
        print("NPC file saved to location ", path)

'''
# Temporarily disabled for GUI Testing, GUI inherently runs each method as selected.
npc = NpcGenerator()
npc.race_gen()
npc.sex_gen()
npc.name_gen()
npc.traits_gen()
npc.attributes_gen()
npc.display()
npc.output()
'''