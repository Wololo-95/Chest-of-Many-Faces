import PySimpleGUI as sg
import webbrowser
import os.path
import npc_generator

alignment_menu = ["None/Unaligned","Lawful Good","Lawful Neutral","Lawful Evil","Neutral Good","True Neutral","Neutral Evil","Chaotic Good","Chaotic Neutral","Chaotic Evil"]

print("Initializing...")
print("Imports successfully loaded, launching application.")

sg.theme("DarkAmber")

def open_about():
    about_screen = [
    [sg.Image("Title.png")],
    [sg.Text("Thanks for using Chest of Many Faces!", justification="center")],
    [sg.Text("CoMF is an ambitious early project geared towards TTRPG players, specifically Dungeons And Dragons 5th edition.\nThis generator was created to accomplish a couple of goals. First and foremost was to hone my fledgling programming skills.\nI started only recently with Python and this is actually one of my first attempts at a solo project.\nIt quickly grewfrom a simple in-terminal name generator, into a full fledged NPC generator.", justification="center")],
    [sg.Text("Soon after, I wanted to increase useability during my games, and desired to make some kind of GUI or webapp for it.\nClearly, I settled on a GUI, and while there was an initial struggle to understand the method to creating one, it eventually started to click.\nSo, that said, it is absolutely uncalculable how much I appreciate the fact that you are reading this, and using my application.\nI am very excited to improve it in the future, as well as use this knowledge to further my own skills!", justification="center")],
    [sg.Button("", size=(165,35), key="-EXIT_ABOUT-", image_filename="thanks.png", image_size=(165,35)), sg.Button("", image_filename="Github.png",size=(165,35), image_size=(165,35), key="-GITHUB-"), sg.Button("", size=(185,35), image_filename="coffeedonate.png", image_size=(185,35))]
    ]
    about_window = sg.Window("About CoMF", about_screen, element_justification="center", resizable=True, icon="icon.ico", modal=True)
    while True:
        event, values = about_window.read()
        if event == "-EXIT_ABOUT-" or event == sg.WIN_CLOSED:
            break
        if event == "-GITHUB-":
            try:
                webbrowser.open("https://github.com/Wololo-95/Chest-of-Many-Faces")
                print("Opened GitHub link successfully")
            except:
                print("Failed to open GitHub Link")
    about_window.close()

npc_log_column = [
    [
        sg.Text("Select Folder For Saving NPCs:"),
    ],
    [
        sg.In(size=(30,40), enable_events = True, key="-FOLDER-"),
        sg.FolderBrowse()
    ],
    [
        sg.Listbox(
            values = [], enable_events = True, size=(35,30), key="-NPCs-"
            )
    ]
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

personality_column_1 = [
    [sg.Checkbox("Generate Personality Trait", default = True, key="-PERSONALITY TRAIT-", enable_events=True)],
    [sg.Checkbox("Generate Ideal", default = True, key="-IDEAL-", enable_events=True)],
    [sg.Checkbox("Generate Flaw", default = True, key="-FLAW-", enable_events=True)]
]

personality_column_2 = [
    [sg.Checkbox("Generate Bond", default = True, key="-BOND-", enable_events=True)],
    [sg.Checkbox("Generate Personality Quirk", default = True, key="-PERSONALITY QUIRK-", enable_events=True)],
    [sg.Checkbox("Generate Physical Quirk", default = True, key="-PHYSICAL TRAIT-", enable_events=True)]
]

core_column_1 = [
    [sg.Radio("Randomize Name", "NAME", True, key="-RANDOM NAME-", enable_events=True)],
    [sg.Radio("Randomize Alignment", "ALIGNMENT", True, key="-RANDOM ALIGNMENT-", enable_events=True)],
    [sg.Radio("Randomize Sex", "SEX", True, key ="-RANDOM SEX-", enable_events=True)],
    [sg.Radio("Randomize Race", "RACE",True, key="-RANDOM RACE-", enable_events=True)],
    [sg.Radio("Generate Attribute Array","ATTRIBUTES", default = True, key= "-ATTRIBUTE ARRAY-", enable_events=True)]
]

core_column_2 = [
    [sg.Radio("Enter a name: ", "NAME", key="-CUSTOM NAME-", enable_events=True), sg.InputText(size=(20,20), key="-NAME SELECTION-", enable_events=True)],
    [sg.Radio("Choose an alignment", "ALIGNMENT", key="-CUSTOM ALIGNMENT-", enable_events=True), sg.Combo(alignment_menu, readonly=True, key="-ALIGNMENT SELECTION-", enable_events=True, size=(15,20))],
    [sg.Radio("Choose a sex", "SEX", key="-CUSTOM SEX-", enable_events=True), sg.Combo(values=["Male","Female"], readonly=True, key="-CUSTOM SEX VALUE-", enable_events=True)],
    [sg.Radio("Choose a race", "RACE", key="-CUSTOM RACE-", enable_events=True), sg.Combo(values=["Human","Elf","Tiefling","Dwarf","Halfling","Half-Orc", "Dragonborn","Half-Elf", "Gnome","Goblin", "Drow"], readonly=True, key="-CUSTOM RACE VALUE-", enable_events=True)],
    [sg.Radio("Customize Attribute Array", "ATTRIBUTES", default=False, key="-CUSTOMIZE ATTRIBUTES-")]
]

npc_generation_column = [
    [sg.Frame("NPC Generation Options:", title_location = "n", expand_x=True, expand_y = True, element_justification="c", layout=[
    [sg.Frame("Please select from the following options:",expand_x=True, expand_y=True, title_location="n", element_justification="c", layout=[
    [sg.Column(core_column_1), sg.VSeperator(), sg.Text(" -Or- "), sg.VSeperator(), sg.Column(core_column_2)]])],
    [sg.Frame("Personality Options (Optional):", title_location="n", element_justification ="c", expand_x=True, expand_y=True, layout=[[sg.Column(personality_column_1), sg.VSeperator(), sg.Column(personality_column_2)]])],
    [sg.Frame("Custom Attribute Array Sliders:", element_justification="c", title_location="n", layout = [[sg.Column(attributes_column_1), sg.VSeperator(), sg.Column(attributes_column_2)]])]
    ])],
    [sg.Text("NOTE: Custom Attribute Array Sliders are ONLY for if you select the Custom Attribute radio option.\nThe options under 'personality options' are fully optional. Any checkboxes can be disabled without issue.\nRadio icons MUST have their inputs filled if using custom options. Application will crash otherwise.\nFolder must be selected, or you will be unable to generate.", justification="c")]
]

npc_viewer_column = [
    [sg.Frame("NPC VIEWER:", element_justification="c", title_location="n", expand_x=True, expand_y=True, size=(350,500), layout=[
    [sg.Text("When you select or generate an NPC,\n its information will appear here!", key="-NPC INFO-", size=(40,40), justification="c", expand_x=True)],
    [sg.Button("Show in Folder", key="-SHOW FOLDER-", disabled=True)]])]
]

layout = [
    [
        sg.Frame("Chest of Many Faces; modular TTRPG NPC Generator - Version 1.0 (Initial Release)", title_location="n", expand_x=True, expand_y=True, layout=[
    [
        sg.Column(npc_log_column),
        sg.VSeperator(),
        sg.Column(npc_generation_column),
        sg.VSeperator(),
        sg.Column(npc_viewer_column)
    ],
    [
        sg.Button("", disabled=True, image_filename="Generate.png", image_size=(83,49), key="-GENERATE-"),
        sg.Button("", image_filename="exit.png", image_size=(75,53), key="-EXIT-"),
        sg.Button("About", key="-ABOUT-")
    ]
        ],
        element_justification="Center", relief="groove"),
    ]
]

# Create window object, elements should be justified center by default
window = sg.Window("Chest of Many Faces", layout, resizable=True, element_justification="center", icon="icon.ico")
npc_box = window["-NPCs-"]

# Create Event Loop - Required for GUI to run; loop ends - application ends
while True:
    event, values = window.read()

    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        print("Filepath selected: " + folder)
        window["-GENERATE-"].update(disabled=False)
        try:
            file_list = os.listdir(folder)
        except:
            file_list =[]
        generated_npcs =[f for f in file_list if os.path.isfile(os.path.join(folder, f))] # iterate through files, add to list, display in window
        window["-NPCs-"].update(generated_npcs)
    
    if event == "-ABOUT-":
        open_about()

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

            window["-SHOW FOLDER-"].update(disabled=False)
        except:
            print("Failed to Load NPC information to window '-NPC INFO-'")
            pass

    if event == "-EXIT-" or event == sg.WIN_CLOSED:
        print("Terminating Application.")
        break

    if event == "-GENERATE-":
        npc = npc_generator.NpcGenerator()
        print("NPC OBJECT CREATED")

        if values["-RANDOM RACE-"] == True:
            try:
                npc.race_gen()
                print("Race Successfully Generated!")
            except:
                print("ERR: Unable to Generate Race")
        elif values["-CUSTOM RACE-"] == True:
            try:
                npc.race = str(values["-CUSTOM RACE VALUE-"])
                print(npc.race)
                print("Race Selection Successfully retrieved.")
            except:
                print("ERR: Unable to retrieve custom race selection.")

        if values["-RANDOM SEX-"] == True:
            try:
                npc.sex_gen()
                print("Sex successfully Generated!")
            except:
                print("ERR: Unable to generate sex")
        elif values["-CUSTOM SEX-"] == True:
            try:
                npc.sex = str(values["-CUSTOM SEX VALUE-"])
                print("Sex Selection Successfully Retrieved.")
            except:
                print("ERR: Unable to retrieve custom sex selection.")

        if values["-RANDOM NAME-"] == True:
            try:
                npc.name_gen()
                print("Name Successfully Generated!")
            except:
                print("ERR: Unable to Generate Name")
        elif values["-CUSTOM NAME-"] == True:
            try:
                npc.name = str(values["-NAME SELECTION-"])
                print("Custom Name Selection Successfully Retrieved.")
            except:
                print("ERR: Unable to Retrieve custom Name selection.")

        if values["-RANDOM ALIGNMENT-"] == True:
            try:
                npc.alignment_gen()
                print("Alignment Successfully Generated!")
            except:
                print("ERR: Unable to generate Alignment")
        elif values["-CUSTOM ALIGNMENT-"] == True:
            try:
                npc.alignment = str(values["-ALIGNMENT SELECTION-"])
                print("Custom Alignment Successfully Retrieved.")
            except:
                print("ERR: Unable to Retrieve custom Alignment selection.")

        if values["-ATTRIBUTE ARRAY-"] == True:
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

        if values["-PERSONALITY TRAIT-"] == True:
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

        if values["-PERSONALITY QUIRK-"] == True:
            try:
                npc.quirk_gen()
                print("Personality Quirk Successfully Generated!")
            except:
                print("ERR: Unable to generate Personality Quirk")

        if values["-PHYSICAL TRAIT-"] == True:
            try:
                npc.physical_gen()
                print("Physical Trait Successfully Generated!")
            except:
                print("ERR: Unable to generate Physical Trait")

        print("NPC Was successfully generated!\nAttempting to save to file.")

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
        npc_file.write("Physical Characteristic: " + str(npc.physical) + "\n")
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
    window["-NPCs-"].update(generated_npcs)

window.close()