import PySimpleGUI as sg
import webbrowser
import npc_generator
import random
import os.path
from pydub import AudioSegment
from pydub.playback import play
import ffmpeg


menu_def = [["NPC Generator"], ["Audio"], ["Maps/Images"], ["About"]]

sg.theme("DarkGrey11")

core_options_column = [
    [sg.Frame("NPC Generation Options:", title_location="n", element_justification="left", expand_x=True, expand_y=True, layout=[
    [sg.Text("Race Selection:"), sg.Combo(values=["Random", "Human", "Elf", "Half-Elf", "Tiefling", "Drow", "Dragonborn"], readonly=True, key="-RACE-", default_value="Random")],
    [sg.Text("Sex Selection:"), sg.Combo(values=["Random", "Male", "Female"], readonly=True, key="-SEX-", default_value="Random")],
    [sg.Text("Name Selection:"), sg.Combo(values=["Random", "Custom"], readonly=True, key="-NAME-", default_value = "Random", enable_events=True), sg.Input(disabled=True, key="-NAME SELECTION-", size =(20,40))],
    [sg.Text("Alignment Selection:"), sg.Combo(values=["Random", "Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"], readonly=True, key="-ALIGNMENT-", default_value="Random")]
])]
]

attributes_column_1 = [
    [sg.Text("Strength Score:"), sg.Slider(range = (1,30), size = (10,20), orientation = "h", key = "-STRENGTH-", default_value=10, expand_x = True)],
    [sg.Text("Constitution Score:"), sg.Slider(range = (1,30), size = (10,20), orientation = "h", key = "-CONSTITUTION-", default_value=10, expand_x = True)],
    [sg.Text("Wisdom Score:"), sg.Slider(range = (1,30), size = (10,20), orientation = "h", key = "-WISDOM-", default_value=10, expand_x = True)]
]

attributes_column_2 = [
    [sg.Text("Dexterity Score:"), sg.Slider(range = (1,30), size = (10,20), orientation = "h", key = "-DEXTERITY-", default_value=10, expand_x = True)],
    [sg.Text("Intelligence Score:"), sg.Slider(range = (1,30), size = (10,20), orientation = "h", key = "-INTELLIGENCE-", default_value=10, expand_x = True)],
    [sg.Text("Charisma Score:"), sg.Slider(range = (1,30), size = (10,20), orientation = "h", key = "-CHARISMA-", default_value=10, expand_x = True)]
]

attribute_generation_column = [
    [sg.Frame("Attribute Options:", title_location="n", element_justification="center", expand_x=True, expand_y=True, layout=[
    [sg.Radio("Randomize Attributes", "ATTRIBUTES", default=True, key="-RANDOMIZE ATTRIBUTES-"), sg.Radio("Customize Attributes", "ATTRIBUTES", key="-CUSTOMIZE ATTRIBUTES-")],
    [sg.Column(attributes_column_1, element_justification="center"), sg.Column(attributes_column_2, element_justification="center")]
])]
]

personality_options_column = [
    [sg.Frame("Personality Options:", title_location="n", element_justification="left", expand_x=True, expand_y=True, layout=[
    [sg.Checkbox("Generate Personality Trait", enable_events=True, default=True, key="-PERSONALITY-"), sg.Checkbox("Generate Flaw", default=True, enable_events=True, key="-FLAW-")],
    [sg.Checkbox("Generate Bond", default=True, enable_events=True, key="-BOND-"), sg.Checkbox("Generate Ideal", enable_events=True, default=True, key="-IDEAL-")],
    [sg.Checkbox("Generate Quirk", default=True, enable_events=True, key="-QUIRK-"), sg.Checkbox("Generate Physical Trait", default=True, enable_events=True, key="-PHYSICAL-")]
])]
]

extra_options_column_random = [
    [sg.Frame("Extra Generation Options", title_location="n", element_justification="left", expand_x=True, expand_y=True, layout=[
    [sg.Checkbox("Enable Extras?", default=False, enable_events=True, key="-EXTRA OPTIONS-")],
    [sg.Checkbox("Generate Religion", default=True, enable_events=True, key="-GEN RELIGION-"), sg.Checkbox("Generate Wealth Status", default=True, enable_events=True, key="-GEN WEALTH-"), sg.Checkbox("Generate Profession", default=True, key="-GEN PROFESSION-")],
    [sg.Checkbox("Generate Languages", default=True, enable_events=True, key="-GEN LANGUAGE-"), sg.VSeparator(), sg.Text("Number of Languages known:"), sg.Combo(values=["Random (1-3)", "1","2","3","4","5","6","7"], readonly=True, default_value="1", key="-KNOWN LANGUAGES-")],
    [sg.Radio("Speaks Common","COMMON", default=True, key="-COMMON TRUE-"), sg.Radio("Does Not Speak Common", "COMMON", key="-COMMON FALSE-")],
    [sg.Checkbox("Enable Obscure Languages?", default=True, key="-OBSCURE LANGUAGE-")]
])]
]

list_column = [
    [sg.Text("Please Select Folder to Store NPCs:")],
    [sg.Input(size=(30,40), expand_x=True, expand_y=False, key="-FOLDER-", enable_events=True), sg.FolderBrowse()],
    [sg.Listbox(values=[], enable_events=True, key="-NPCs-", expand_x=True, expand_y=True)],
    [sg.Button("Open Folder", disabled=True, key="-OPEN FOLDER-")]
]

viewer_column = [
    [sg.Frame("NPC Viewer", title_location="n", element_justification="center", expand_x=True, expand_y=True, layout=[
    [sg.Text("Once you have generated and selected an NPC, its information will appear here!", size=(40,0), grab=True, key="-NPC INFO-", justification="c", auto_size_text=True)]
])]
]

generation_column = [
    [sg.Column(core_options_column, element_justification="left")],
    [sg.Column(attribute_generation_column, element_justification="left")],
    [sg.Column(personality_options_column, element_justification="left")],
    [sg.Column(extra_options_column_random, element_justification="left")],
    [sg.Button("Generate"), sg.Button("Exit")]
]

amb_column1 = [
    [sg.Button("City Streets (day)", key="-CS DAY-")],
    [sg.Button("City Streets (night)", key="-CS NIGHT-")],
    [sg.Button("City Streets (panic)", key="-CS PANIC-")],
    [sg.Button("City Streets (festival)", key="-CS FEST-")],
    [sg.Button("City Streets (trade)", key="-CS TRADE")],
    [sg.Button("City Streets (travel)", key="-CS TRAVEL")]
]

amb_column2 = [
    [sg.Button("Market District", key="-MARKET DIST-")],
    [sg.Button("Sewers", key="-SEWER-")],
    [sg.Button("Mines", key="-MINES-")],
    [sg.Button("Tavern w/ Hearth", key="-TAV HEARTH-")],
    [sg.Button("Busy Tavern", key="-TAV BUSY-")],
    [sg.Button("Nature", key="-NATURE-")]
]

file_list_column = [
    [sg.Frame("Image Selection", expand_x=True, expand_y=True, element_justification="Center", title_location="n", layout =[
    [sg.Text("Image Folder"), sg.In(size=(25, 1), enable_events=True, key ="-IMAGE FOLDER-"), sg.FolderBrowse()],
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
])]
]

image_viewer_column = [
    [sg.Frame("Choose an image from the list to the left", expand_x=True, expand_y=True, element_justification="Center", title_location="n", layout =[
    [sg.Text(size=(40,1), key="-TOUT-", expand_x=True)],
    [sg.Image(key="-IMAGE-", size = (200,200))]
])]
]

ambiance_column = [
    [sg.Frame("Ambient sounds to fill the world", title_location="n", element_justification="center", expand_x=True, expand_y=True, layout=[
    [sg.Column(amb_column1, element_justification="left"), sg.VSeparator(), sg.Column(amb_column2, element_justification="left")],
    [sg.Button("Stop Ambience", key="-END AMB-")]
])]
]

main_layout = [
    [sg.Button("NPC Generator", disabled=True, size=(15,1)), sg.Button("Audio", size=(15,1), key = "-AUDIO-"), sg.Button("Maps/Images", size=(15,1), key="-IMAGE VIEWER-"), sg.Button("About", size=(15,1))],
    [sg.Frame("Chest of Many Faces - DM Dashboard", title_location = "n", expand_x=True, expand_y=True, element_justification="Center", layout=[
    [sg.Column(list_column, expand_y=True), sg.VSeparator(), sg.Column(generation_column, element_justification="Center"), sg.VSeparator(), sg.Column(viewer_column, expand_y=True, expand_x=True)],
    ])]
]

audio_layout = [
    [sg.Frame("Audio and Music - DM Dashboard", title_location="n", element_justification="center", expand_x=True, expand_y=True, layout=[
    [sg.Column(ambiance_column, expand_y=True), sg.VSeparator()],
    [sg.Button("Exit")]
    ])]
]

image_layout = [
    [sg.Column(file_list_column), sg.VSeperator(), sg.Column(image_viewer_column)]
]

window = sg.Window("DM Dashboard - Chest of Many Faces", main_layout, resizable=True, element_justification="Center", icon="icon.ico")
audio_window = sg.Window("DM Dashboard - Chest of Many Songs", audio_layout, resizable=True, element_justification="Center", icon="icon.ico")
image_window = sg.Window("Image Viewer", image_layout)

def audio():
    while True:
        event, values = audio_window.read()
        ambience = ""
        track = ""
        if event == "-SEWER-":
            ambience = AudioSegment.from_file("music/ambience/sewers.mp4", ".mp4")
            play(ambience)
        
        if event == "-END AMB-":
            ambience.stop()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    audio_window.close()

def image_viewer():
    while True:
        event, values = image_window.read()

        if event == "-IMAGE FOLDER-":
            folder = values["-IMAGE FOLDER-"]
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []
            
            fnames = [f for f in file_list if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith((".png", ".gif"))]
            image_window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":
            try:
                filename = os.path.join(values["-IMAGE FOLDER-"], values["-FILE LIST-"][0])
                image_window["-TOUT-"].update(filename)
                image_window["-IMAGE-"].update(filename=filename)
            except:
                pass
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-OPEN FOLDER-":
        webbrowser.open(os.path.realpath(folder))
    
    if event == "-AUDIO-":
        audio()

    if event == "-IMAGE VIEWER-":
        image_viewer()

    if event == "-ABOUT-":
        #open_about()
        pass

    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        print("Filepath selected: " + folder)
        try:
            file_list = os.listdir(folder)
        except:
            file_list =[]
        generated_npcs =[f for f in file_list if os.path.isfile(os.path.join(folder, f))] # iterate through files, add to list, display in window
        generated_npcs.sort()
        window["-NPCs-"].update(generated_npcs)
        window["-OPEN FOLDER-"].update(disabled=False)

    if event == "-NPCs-":
        try:
            print(values["-NPCs-"])
            selection = values["-NPCs-"]
            selection = str(selection)
            selection = selection.replace("['", "")
            selection = selection.replace("']", "")  # string is created with [' and '], in order to search for file, must be removed

            if selection in file_list:
                print("File selection found in file list")
                print(selection)
            else:
                print("File not found.")

            with open(folder + "/{}".format(selection), "r") as readable:
                print("File opened, reading to window.")
                window["-NPC INFO-"].update(readable.read())
                readable.close()
        except:
            print("Failed to Load NPC information to window '-NPC INFO-'")
            pass
    
    if values["-NAME-"] == "Custom":
        window["-NAME SELECTION-"].update(disabled=False)

    if event == "Generate":
        npc = npc_generator.NpcGenerator()
        print("NPC OBJECT CREATED")

        if values["-RACE-"] == "Random":
            try:
                npc.race_gen()
                print("Race Successfully Generated!")
            except:
                print("ERR: Unable to Generate Race")
        else:
            try:
                npc.race = str(values["-RACE-"])
                print(npc.race)
                print("Race Selection Successfully retrieved.")
            except:
                print("ERR: Unable to retrieve custom race selection.")

        if values["-SEX-"] == "Random":
            try:
                npc.sex_gen()
                print("Sex successfully Generated!")
            except:
                print("ERR: Unable to generate sex")
        else:
            try:
                npc.sex = str(values["-SEX-"])
                print("Sex Selection Successfully Retrieved.")
            except:
                print("ERR: Unable to retrieve custom sex selection.")

        if values["-NAME-"] == "Random":
            try:
                npc.name_gen()
                print("Name Successfully Generated!")
            except:
                print("ERR: Unable to Generate Name")
        elif values["-NAME-"] == "Custom":
            try:
                npc.name = str(values["-NAME SELECTION-"])
                print("Custom Name Selection Successfully Retrieved.")
            except:
                print("ERR: Unable to Retrieve custom Name selection.")

        if values["-ALIGNMENT-"] == "Random":
            try:
                npc.alignment_gen()
                print("Alignment Successfully Generated!")
            except:
                print("ERR: Unable to generate Alignment")
        else:
            try:
                npc.alignment = str(values["-ALIGNMENT-"])
                print("Custom Alignment Successfully Retrieved.")
            except:
                print("ERR: Unable to Retrieve custom Alignment selection.")

        if values["-RANDOMIZE ATTRIBUTES-"] == True:
            try:
                npc.attributes_gen()
                print("Attribute Score Array Successfully Generated!")
            except:
                print("ERR: Unable to generate Attribute Score Array")
        elif values["-CUSTOMIZE ATTRIBUTES-"] == True:
            try:
                npc.custom_attribute_selection()
                npc.strength = str(values["-STRENGTH-"])
                npc.dexterity = str(values["-DEXTERITY-"])
                npc.constitution = str(values["-CONSTITUTION-"])
                npc.intelligence = str(values["-INTELLIGENCE-"])
                npc.wisdom = str(values["-WISDOM-"])
                npc.charisma = str(values["-CHARISMA-"])
                print("Sucessfully assigned attribute scores.")
            except:
                print("Unable to write custom values to NPC object.")

        if values["-PERSONALITY-"] == True:
            try:
                npc.personality_gen()
                print("Personality Trait Successfully Generated!")
            except:
                print("ERR: Unable to generate Personality Trait")

        if values["-IDEAL-"] == True:
            try:
                npc.ideal_gen()
                print("Ideal Successfully Generated!")
            except:
                print("ERR: Unable to generate Ideal")

        if values["-BOND-"] == True:
            try:
                npc.bond_gen()
                print("Bond Successfully Generated!")
            except:
                print("ERR: Unable to generate Bond")

        if values["-FLAW-"] == True:
            try:
                npc.flaw_gen()
                print("Flaw Successfully Generated!")
            except:
                print("ERR: Unable to generate Flaw")

        if values["-QUIRK-"] == True:
            try:
                npc.quirk_gen()
                print("Personality Quirk Successfully Generated!")
            except:
                print("ERR: Unable to generate Personality Quirk")

        if values["-PHYSICAL-"] == True:
            try:
                npc.physical_gen()
                print("Physical Trait Successfully Generated!")
            except:
                print("ERR: Unable to generate Physical Trait")

        if values["-EXTRA OPTIONS-"] == True:
            if values["-GEN RELIGION-"] == True:
                try:
                    npc.religion_generation_alignment()
                    print("Religion Generated successfully.")
                except:
                    print("ERR: Failed to generate religion")
            if values["-GEN WEALTH-"] == True:
                try:
                    npc.income_determinator()
                    npc.current_gold()
                    print("Income status & held gold determined!")
                except:
                    print("ERR: Failed to determine income status.")
            if values["-GEN PROFESSION-"] == True:
                try:
                    npc.job_determinator()
                    print("NPC Profession successfully generated!")
                except:
                    print("ERR: Could not generate NPC profession.")
            if values["-GEN LANGUAGE-"] == True:
                try:
                    if values["-OBSCURE LANGUAGE-"] == True:
                        if values["-COMMON TRUE-"] == True:
                            npc.knows_common == True
                            if values["-KNOWN LANGUAGES-"] == "Random (1-3)":
                                npc.languages_known = random.randint(1,3)
                            else:
                                npc.languages_known = int(values["-KNOWN LANGUAGES-"])
                            npc.known_languages()
                        else:
                            npc.knows_common == False
                            if values["-KNOWN LANGUAGES-"] == "Random (1-3)":
                                npc.languages_known = random.randint(1,3)
                            else:
                                npc.languages_known = int(values["-KNOWN LANGUAGES-"])
                            npc.known_languages()
                    if ["-OBSCURE LANGUAGE-"] == False:
                        if values["-COMMON TRUE-"] == True:
                            npc.knows_common == True
                            if values["-KNOWN LANGUAGES-"] == "Random (1-3)":
                                npc.languages_known = random.randint(1,3)
                            else:
                                npc.languages_known = int(values["-KNOWN LANGUAGES-"])
                            npc.known_languages()
                        else:
                            npc.knows_common == False
                            if values["-KNOWN LANGUAGES-"] == "Random (1-3)":
                                npc.languages_known = random.randint(1,3)
                            else:
                                npc.languages_known = int(values["-KNOWN LANGUAGES-"])
                            npc.known_languages()
                    print("Languages Generated")
                    print(npc.languages)
                except:
                    print("Failed to generate languages")

        # Output to txt file in designated folder
        npc_filename = "{}.txt".format(npc.name)
        npc_file = open(npc_filename, "w")
        npc_file.write("Name: {}\n".format(npc.name))
        npc_file.write("Race: {} {}\n".format(str(npc.sex), str(npc.race)))
        npc_file.write("Alignment: {}\n\n".format(npc.alignment))

        npc_file.write("-------ATTRIBUTE SCORE ARRAY-------\n")
        if npc.custom_attributes_enabled == True:
            npc_file.write("Strength: " + str(npc.strength) + "\n")
            npc_file.write("Dexterity: " + str(npc.dexterity) + "\n")
            npc_file.write("Constitution: " + str(npc.constitution) + "\n")
            npc_file.write("Intelligence: " + str(npc.intelligence) + "\n")
            npc_file.write("Wisdom: " + str(npc.wisdom) + "\n")
            npc_file.write("Charisma: " + str(npc.charisma) + "\n")
        elif npc.custom_attributes_enabled == False:
            for each in npc.attribute_scores:
                npc_file.write(each + "\n")
        npc_file.write("\n\n")

        npc_file.write("-------TRAITS AND FLAWS-------\n")
        npc_file.write("Personality trait: " + npc.pt + "\n")
        npc_file.write("Ideal: " + npc.ideal + "\n")
        npc_file.write("Bond: " + npc.bond + "\n")
        npc_file.write("Flaw: " + npc.flaw + "\n")
        npc_file.write("Quirk: " + npc.quirk + "\n")
        npc_file.write("Physical Characteristic: " + str(npc.physical) + "\n\n")

        npc_file.write("-------RELIGION, WEALTH, PROFESSION, AND LANGUAGES-------\n")
        npc_file.write("Religion: " + npc.religion + "\n")
        npc_file.write("Wealth Status: " + str(npc.wealth) + "\n")
        npc_file.write("Currently has: " + str(npc.current_gold_pieces) + "gp, " + str(npc.current_silver_pieces) + "sp, " + str(npc.current_copper_pieces) + "cp\n")
        npc_file.write("Profession: " + npc.occupation + "\n")
        npc_file.write("Languages known: ")
        for each in npc.languages:
            npc_file.write(str(each) + ", ")
        
        npc_file.close()

        os.rename(npc_filename, "{}/{}".format(folder, npc_filename))
        os.path.join(str(folder), str(npc_file))
        print("File successfully created.")
        npc.display()
        path = os.path.abspath(npc_filename)
        print("\nNPC file saved to location: ", path)
    try:
        file_list = os.listdir(folder)
    except:
        file_list =[]
    generated_npcs =[f for f in file_list if os.path.isfile(os.path.join(folder, f))]
    generated_npcs.sort()
    window["-NPCs-"].update(generated_npcs)

window.close()