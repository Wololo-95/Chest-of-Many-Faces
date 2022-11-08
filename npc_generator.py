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
        # Wealth, occupation, languages, other advanced options
        self.wealth = ""
        self.occupation = ""
        self.knows_common = True #Default value of true as most NPCs would speak common, can be set false only in GUI or webapp
        self.knows_obscure_languages = False
        self.languages = []
        self.languages_known = 1
        self.religion = ""
        # Current coin values are determined based on wealth status
        self.current_gold_pieces = 0
        self.current_silver_pieces = 0
        self.current_copper_pieces = 0

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

    def income_determinator(self):
        wealth_options = ["Aristocratic", "Wealthy", "Comfortable", "Modest", "Poor", "Squalid", "Wretched"]
        self.wealth = choice(wealth_options, 1, p=[0.05, 0.05, 0.23, 0.40, 0.17, 0.07, 0.03])
    
    def current_gold(self):
        if self.wealth == "Aristocratic":
            self.current_gold_pieces = random.randint(20, 85)
            self.current_silver_pieces = random.randint(1, 100)
            self.current_copper_pieces = random.randint(1, 100)
        if self.wealth == "Wealthy":
            self.current_gold_pieces = random.randint(1, 10)
            self.current_silver_pieces = random.randint(1, 100)
            self.current_copper_pieces = random.randint(1, 100)
        if self.wealth == "Comfortable":
            self.current_gold_pieces = random.randint(0,6)
            self.current_silver_pieces = random.randint(0, 100)
            self.current_copper_pieces = random.randint(1, 100)
        if self.wealth == "Modest":
            self.current_gold_pieces = random.randint(0,2)
            self.current_silver_pieces = random.randint(0,45)
            self.current_copper_pieces = random.randint(1, 80)
        if self.wealth == "Poor":
            self.current_gold_pieces = 0
            self.current_silver_pieces = random.randint(0, 30)
            self.current_copper_pieces = random.randint(0,40)
        if self.wealth == "Squalid":
            self.current_gold_pieces = 0
            self.current_silver_pieces = random.randint(0,10)
            self.current_copper_pieces = random.randint(0,20)
        if self.wealth == "Wretched":
            self.current_gold_pieces = 0
            self.current_silver_pieces = 0
            self.current_copper_pieces = random.randint(0,10)


    def job_determinator(self):
        if self.wealth == "Aristocratic" or self.wealth == "Wealthy":
            job_list = ["Politician", "Merchant", "Caravan Owner", "Brothelkeep", "Tavern Chain Owner", "Lord/Lady", "Underworld Crime Lord", "Famed Artist", "Landlord", "Military Doctor", "Surgeon", "Court Advisor", "Diplomat", "Translator", "Con Man", "High-Ranked Military", "Fine Wine Seller", "Artisan", "Real Estate Mogul", "Unemployed/Inherited Wealth"]
            self.occupation = random.choice(job_list)
        if self.wealth == "Comfortable" or self.wealth == "Modest":
            job_list = ["Merchant", "Tavern Owner", "Tavernkeeper", "Underworld Criminal", "Underworld Crime Boss", "Artist", "Artisan", "Farmer/Crops", "Farmer/Animals", "Farmer/All Agriculture", "Doctor", "Shopkeeper", "Small Town Mayor", "Town Guard", "Wine Maker", "Wine Seller", "Basket Weaver", "Smith (Armor)", "Smith (Weapons)", "Cook", "Silversmith", "Jeweler", "Woodcarver", "Woodworker", "Woodcutter", "Soldier", "Famous Fighter", "Bard", "Clockmaker"]
            self.occupation = random.choice(job_list)
        if self.wealth == "Poor" or self.wealth == "Squalid":
            job_list = ["Farmer/Animals", "Farmer/Agriculture", "Farmer/All Agriculture", "Criminal", "Outlaw", "Basket Weaver", "Smith (Armor)", "Smith (Weapons)", "Silversmith", "Jeweller", "Shopkeeper", "Town Guard", "Soldier", "Wine Maker", "Wine Seller", "Basket Weaver", "Cook", "Woodcarver", "Woodcutter", "Woodworker", "Construction Worker", "Cobbler", "Bard", "Clockmaker", "Miner", "Servant", "Barber", "Fighter", "Fighter (Gladiator)", "Gardener", "Unemployed"]
            self.occupation = random.choice(job_list)
        if self.wealth == "Wretched":
            job_list = ["Unemployed", "Farm Hand", "Slave", "Prisoner", "Prisoner (Escaped)"]
            self.occupation = random.choice(job_list)

    def known_languages(self):
        languages = []
        if self.knows_common == True:
            languages = ["Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orcish"]
            if self.knows_obscure_languages == True:
                obscure_languages = ["Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon"]
                for each in obscure_languages:
                    languages = languages.append(each)
            self.languages = random.sample(languages, self.languages_known)
            self.languages.append("Common")
        elif self.knows_common == False:
            self.languages_known = 1 
            languages = ["Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orcish"]
            if self.knows_obscure_languages == True:
                obscure_languages = ["Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon"]
                for each in obscure_languages:
                    languages = languages.append(each)
            self.languages = random.sample(languages, self.languages_known)

    def religion_generation_random(self):
        # Main religion gen accounts for the Gods of Faerun, as well as no religious following, and a few unorthodox systems
        # Religion chosen in this method is truly random, and not accounted for alignment
        religions = ["Auril, Goddess of Winter", "Azuth, God of Wizards", "Bane, God of Tyrany", "Beshaba, Goddess of Misfortune", "Bhaal, God of Murder", "Chauntea, Goddess of Agriculture", "Cyric, God of Lies", "Deneir, God of Writing", "Eldath, Goddess of Peace", "Gond, God of Craft", "Helm, God of Protection", "Ilmater, God of Endurance", "Kelemvor, God of the Dead", "Lathander, Goddess of Illusion", "Lliira, Goddess of Joy", "Loviatar, Goddess of Pain", "Malar, God of the Hunt", "Mask, God of Thieves", "Mielikki, Goddess of Forests", "Milil, God of Poetry and Song", "Myrkul, God of Death", "Mystra, Goddess of Magic", "Oghma, God of Knowledge", "Savras, God of Divination and Fate", "Selûne, Goddess of the Moon", "Shar, Goddess of Darkness and Loss", "Silvanus, God of Wild Nature", "Sune, Goddess of Love and Beauty", "Talona, Goddess of Disease and Poison", "Talos, God of Storms", "Tempus, God of War", "Torm, God of Courage and Self-Sacrifice", "Tymora, Goddess of Good Fortune", "Tyr, God of Justice", "Umberlee, Goddess of the Sea", "Waukeen, Goddess of Trade", "Nonreligious/Athiest"]
        self.religion = random.choice(religions)
    
    def religion_generation_alignment(self):
        # Religion is Generated on an alignment basis, with gods specifically matching the NPC's alignment being most likely, followed by adjacent alignments
        # E.G. NPC is True Neutral, and Gods with the same general alignment will be chosen first, followed by those who may be CN, LN, NG, NE at a lesser percentage
        # Also appends the racial religions to the end of each
        religions = []
        if (self.alignment == "Lawful Good" or self.alignment == "Neutral Good") or "Chaotic Good":
            religions = ["Ilmater, God of Endurance", "Torm, God of Courage and Self-Sacrifice", "Tyr, God of Justice", "Azuth, God of Wizards", "Chauntea, Goddess of Agriculture", "Deneir, God of Writing", "Eldath, Goddess of Peace", "Gond, God of Craft", "Helm, God of Protection", "Kelemvor, God of the Dead", "Lathander, God of Birth and Renewal", "Lliira, Goddess of Joy", "Mielikki, Goddess of Forest", "Milil, God of Poetry and Song", "Mystra, Goddess of Magic", "Silvanus, God of Wild Nature", "Sune, Goddess of Love and Beauty", "Tempus, God of War", "Tymora, Goddess of Good Fortune", "Nonreligious/Athiest"]
            
            if self.race == "Dragonborn":
                religions.append("Bahamut, Dragon God of Good")
                religions.append("Tiamat, Dragon Goddess of Evil")
            
            if self.race == "Elf" or self.race == "Half-Elf":
                religions.append("Corellon Larethian, Elf Deity of Art and Magic")
                religions.append("Deep Sashelas, Elf God of the Sea")
                religions.append("Rillifane Rallathil, Wood Elf God of Nature")
                religions.append("Sehanine Moonbow, Elf Goddess of the Moon")
            
            if self.race == "Gnome":
                religions.append("Garl Glittergold, Gnome God of Trickery and Wiles")
            
            if self.race == "Halfling":
                religions.append("Yondalla, Halfling Goddess of Fertility and Protection")
            
            if self.race == "Giant" or self.race == "Goliath":
                religions.append("Grolantor, Hill Giant God of War")
                religions.append("Skoraeus Stonebones, God of Stone Giants and Art")
                religions.append("Surtur, God of fire Giants and Craft")
                religions.append("Thrym, God of Frost Giants and Strength")
            
            if self.race == "Orc" or self.race == "Half-Orc":
                religions.append("Gruumsh, Orc God of Storms and War")
            
            if self.race == "Kobold":
                religions.append("Kurtulmak, Kobold God of War and Mining")
            
            if self.race == "Drow":
                religions.append("Lolth, Drow Goddess of Spiders")
            
            if self.race == "Goblin":
                religions.append("Maglubiyet, Goblinoid God of War")
            
            if self.race == "Dwarf":
                religions.append("Moradin, Dwarf God of Creation")

        if (self.alignment == "Lawful Neutral" or self.alignment == "True Neutral") or "Chaotic Neutral":
            religions = ["Azuth, God of Wizards", "Chauntea, Goddess of Agriculture", "Deneir, God of Writing", "Eldath, Goddess of Peace", "Gond, God of Craft", "Helm, God of Protection", "Kelemvor, God of the Dead", "Lathander, God of Birth and Renewal", "Leira, Goddess of Illusion", "Mask, God of Thieves", "Mielikki, Goddess of Forests", "Milil God of Poetry and Song", "Mystra, Goddess of Magic", "Oghma, God of Knowledge", "Savras, God of Divination and Fate", "Silvanus, God of Wild Nature", "Tempus, God of War", "Waukeen, Goddess of Trade", "Nonreligious/Athiest"]
            
            if self.race == "Dragonborn":
                religions.append("Bahamut, Dragon God of Good")
                religions.append("Tiamat, Dragon Goddess of Evil")
            
            if self.race == "Elf" or self.race == "Half-Elf":
                religions.append("Corellon Larethian, Elf Deity of Art and Magic")
                religions.append("Deep Sashelas, Elf God of the Sea")
                religions.append("Rillifane Rallathil, Wood Elf God of Nature")
                religions.append("Sehanine Moonbow, Elf Goddess of the Moon")
            
            if self.race == "Gnome":
                religions.append("Garl Glittergold, Gnome God of Trickery and Wiles")
            
            if self.race == "Halfling":
                religions.append("Yondalla, Halfling Goddess of Fertility and Protection")
            
            if self.race == "Giant" or self.race == "Goliath":
                religions.append("Grolantor, Hill Giant God of War")
                religions.append("Skoraeus Stonebones, God of Stone Giants and Art")
                religions.append("Surtur, God of fire Giants and Craft")
                religions.append("Thrym, God of Frost Giants and Strength")
            
            if self.race == "Orc" or self.race == "Half-Orc":
                religions.append("Gruumsh, Orc God of Storms and War")
            
            if self.race == "Kobold":
                religions.append("Kurtulmak, Kobold God of War and Mining")
            
            if self.race == "Drow":
                religions.append("Lolth, Drow Goddess of Spiders")
            
            if self.race == "Goblin":
                religions.append("Maglubiyet, Goblinoid God of War")
            
            if self.race == "Dwarf":
                religions.append("Moradin, Dwarf God of Creation")

        if (self.alignment == "Lawful Evil" or self.alignment == "Neutral Evil") or self.alignment == "Chaotic Evil":
            religions = ["Auril, Goddess of Winter", "Bane, God of Tyranny", "Beshaba, Goddess of Misfortune", "Bhaal, God of Murder", "Cyric, God of Lies", "Leira, Goddess of Illusion", "Loviatar, Goddess of Pain", "Malar, God of the Hunt", "Mask, God of Thieves", "Myrkul, God of Death", "Oghma, God of Knowledge", "Shar, Goddess of Darkness and Loss", "Silvanus, God of Wild Nature", "Talona, Goddess of Disease and Poison", "Talos, God of Storms", "Tempus, God of War", "Umberlee, Goddess of the Sea", "Waukeen, Goddess of Trade", "Nonreligious/Athiest"]
            
            if self.race == "Dragonborn":
                religions.append("Bahamut, Dragon God of Good")
                religions.append("Tiamat, Dragon Goddess of Evil")
            
            if self.race == "Elf" or self.race == "Half-Elf":
                religions.append("Corellon Larethian, Elf Deity of Art and Magic")
                religions.append("Deep Sashelas, Elf God of the Sea")
                religions.append("Rillifane Rallathil, Wood Elf God of Nature")
                religions.append("Sehanine Moonbow, Elf Goddess of the Moon")
            
            if self.race == "Gnome":
                religions.append("Garl Glittergold, Gnome God of Trickery and Wiles")
            
            if self.race == "Halfling":
                religions.append("Yondalla, Halfling Goddess of Fertility and Protection")
            
            if self.race == "Giant" or self.race == "Goliath":
                religions.append("Grolantor, Hill Giant God of War")
                religions.append("Skoraeus Stonebones, God of Stone Giants and Art")
                religions.append("Surtur, God of fire Giants and Craft")
                religions.append("Thrym, God of Frost Giants and Strength")
            
            if self.race == "Orc" or self.race == "Half-Orc":
                religions.append("Gruumsh, Orc God of Storms and War")
            
            if self.race == "Kobold":
                religions.append("Kurtulmak, Kobold God of War and Mining")
            
            if self.race == "Drow":
                religions.append("Lolth, Drow Goddess of Spiders")
            
            if self.race == "Goblin":
                religions.append("Maglubiyet, Goblinoid God of War")
            
            if self.race == "Dwarf":
                religions.append("Moradin, Dwarf God of Creation")
            
        self.religion = random.choice(religions)
    
    def religion_generation_racial(self):
        # Religion generation based SOLELY on race. Main-pantheon gods are excluded from this list and is only used if user selects Racial Only
        if self.race == "Dragonborn":
            religions = ["Bahamut, Dragon God of Good", "Tiamat, Dragon Goddess of Evil"]
            self.religion = random.choice(religions)
        if self.race == "Elf" or "Half-Elf":
            religions = ["Corellon Larethian, Elf Deity of Art and Magic", "Deep Sashelas, Elf God of the Sea", "Rillifane Rallathil, Wood Elf God of Nature", "Sehanine Moonbow, Elf Goddess of the Moon"]
            self.religion = random.choice(religions)
        if self.race == "Gnome":
            religions = ["Garl Glittergold, Gnome God of Trickery and Wiles"]
            self.religion = random.choice(religions)
        if self.race == "Halfling":
            religions = ["Yondalla, Halfling Goddess of Fertility and Protection"]
            self.religion = random.choice(religions)
        if self.race == "Giant" or "Goliath":
            religions =["Grolantor, Hill Giant God of War", "Skoraeus Stonebones, God of Stone Giants and Art", "Surtur, God of fire Giants and Craft", "Thrym, God of Frost Giants and Strength"]
            self.religion = random.choice(religions)
        if self.race == "Orc" or "Half-Orc":
            religions = ["Gruumsh, Orc God of Storms and War"]
            self.religion = random.choice(religions)
        if self.race == "Kobold":
            religions = ["Kurtulmak, Kobold God of War and Mining"]
            self.religion = random.choice(religions)
        if self.race == "Drow":
            religions = ["Lolth, Drow Goddess of Spiders"]
            self.religion = random.choice(religions)
        if self.race == "Goblin":
            religions = ["Maglubiyet, Goblinoid God of War"]
            self.religion = random.choice(religions)
        if self.race == "Dwarf":
            religions = ["Moradin, Dwarf God of Creation"]
            self.religion = random.choice(religions)

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
npc.alignment_gen()
npc.sex_gen()
npc.name_gen()
npc.attributes_gen()


npc.income_determinator()
npc.job_determinator()
npc.religion_generation_alignment()
print(npc.religion)
npc.known_languages()
print(npc.languages)
npc.display()
'''