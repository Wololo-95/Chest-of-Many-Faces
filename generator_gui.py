import PySimpleGUI as sg
import textwrap
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
    about_window = sg.Window("About CoMF", about_screen, resizable=True, icon="icon.ico", modal=True)
    while True:
        event, values = about_window.read()
        if event == "-EXIT_ABOUT-" or event == sg.WIN_CLOSED:
            break
        if event == "-GITHUB-":
            try:
                webbrowser.open("https://github.com/Wololo-95/Chest-of-Many-Faces")
                print("Opened link successfully")
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

attributes_column = [
    [sg.Frame("Attributes for Custom Selection:", layout=[
    [sg.Text("Strength Score:"), sg.Slider(range=(1,30), size=(10,20), orientation="h", key = "-STRENGTH-"), sg.VSeperator(), sg.Text("Dexterity Score:"), sg.Slider(range=(1,30), size=(10,20), orientation="h", key = "-DEXTERITY-")],
    [sg.Text("Constitution Score:"), sg.Slider(range=(1,30), size=(10,20), orientation="h", key = "-CONSTITUTION"), sg.VSeperator(), sg.Text("Intelligence Score:"), sg.Slider(range=(1,30), size=(10,20), orientation="h", key = "-INTELLIGENCE-")],
    [sg.Text("Wisdom Score:"), sg.Slider(range=(1,30), size=(10,20), orientation="h", key = "-WISDOM-"), sg.VSeperator(), sg.Text("Charisma:"), sg.Slider(range=(1,30), size=(10,20), orientation="h", key = "-CHARISMA-")]
    ])]
]

npc_generation_column = [
    [sg.Frame("NPC Generation Options:", layout=[
    [sg.Text("Please select from the following options:", size=(40,1),key="-GENERATION TEXT-")],
    [sg.Radio("Randomize Name", "NAME", True, key="-RANDOM NAME-", enable_events=True), sg.Text(" -Or- "), sg.Radio("Enter a name: ", "NAME", key="-CUSTOM NAME-", enable_events=True), sg.InputText(size=(20,20), key="-NAME SELECTION-", enable_events=True)],
    [sg.Radio("Randomize Alignment", "ALIGNMENT", True, key="-RANDOM ALIGNMENT-", enable_events=True), sg.Text(" -Or- "), sg.Radio("Choose an alignment", "ALIGNMENT", key="-CUSTOM ALIGNMENT-", enable_events=True), sg.Combo(alignment_menu, readonly=True, key="-ALIGNMENT SELECTION-", enable_events=True)],
    [sg.Radio("Randomize Sex", "SEX", True, key ="-RANDOM SEX-", enable_events=True), sg.Text(" -Or- "), sg.Radio("Choose a sex", "SEX", key="-CUSTOM SEX-", enable_events=True), sg.Combo(values=["Male","Female"], readonly=True, key="-CUSTOM SEX VALUE-", enable_events=True)],
    [sg.Radio("Randomize Race", "RACE",True, key="-RANDOM RACE-", enable_events=True), sg.Text(" -Or- "), sg.Radio("Choose a race", "RACE", key="-CUSTOM RACE-", enable_events=True), sg.Combo(values=["Human","Elf","Tiefling","Dwarf","Halfling","Half-Orc", "Dragonborn","Half-Elf", "Gnome","Goblin", "Drow"], readonly=True, key="-CUSTOM RACE VALUE-", enable_events=True)],
    [sg.Radio("Generate Attribute Array","ATTRIBUTES", default = True, key= "-ATTRIBUTE ARRAY-", enable_events=True), sg.Text(" -Or- "), sg.Radio("Customize Attribute Array", "ATTRIBUTES", default=False, key="-CUSTOMIZE ATTRIBUTES")],
    [sg.Checkbox("Generate Personality Trait", default = True, key="-PERSONALITY TRAIT-", enable_events=True), sg.VSeperator(), sg.Checkbox("Generate Ideal", default = True, key="-IDEAL-", enable_events=True), sg.VSeperator()],
    [sg.Checkbox("Generate Flaw", default = True, key="-FLAW-", enable_events=True), sg.VSeperator(), sg.Checkbox("Generate Bond", default = True, key="-BOND-", enable_events=True)],
    [sg.Checkbox("Generate Personality Quirk", default = True, key="-PERSONALITY QUIRK-", enable_events=True), sg.VSeperator(), sg.Checkbox("Generate Physical Quirk", default = True, key="-PHYSICAL TRAIT-", enable_events=True)],
    [sg.Column(attributes_column)]
    ]
    )
    ],
    [sg.Text("Please note the following:\nCheckbox Elements such as for generating the Attribute Array for an NPC are OPTIONAL,\nand can be disabled. Elements that have fillable forms or menus\nmust have a selection if being used, or the application will crash.\nPlease also note that duplicate names WILL override existing files of the same name.\n\n Lastly, the application is still in early development, it may crash without notice.\n Thanks for using Chest of Many Faces, and I hope it proves useful for you!", justification="c")]
]

npc_viewer_column =[
    [sg.Frame("NPC VIEWER:", expand_x=True, size=(350,500), layout=[
    [sg.Text("When you select or generate an NPC,\n its information will appear here!", key="-NPC INFO-", size=(40,40), justification="c", expand_x=True)],
    [sg.Button("Show in Folder", key="-SHOW FOLDER-", disabled=True)]])]
]

layout = [
    [
        sg.Frame("Chest of Many Faces; modular TTRPG NPC Generator - Version 1.0 (Initial Release)", layout=[
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

# Create window variable, sg.Window() allows you to define the name and the layout among others, it takes many arguments
window = sg.Window("Chest of Many Faces", layout, resizable=True, icon="icon.ico")
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
                print("Found in file list")
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
        print("NPC OBJECT CREATED\n")

        if values["-RANDOM RACE-"] == True:
            try:
                npc.race_gen()
                print("Race Successfully Generated!\n")
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
                print("Sex successfully Generated!\n")
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
                print("Name Successfully Generated!\n")
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
                print("Alignment Successfully Generated!\n")
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
                print("Attribute Score Array Successfully Generated!\n")
            except:
                print("ERR: Unable to generate Attribute Score Array")

        if values["-PERSONALITY TRAIT-"] == True:
            try:
                npc.personality_gen()
                print("Personality Trait Successfully Generated!\n")
            except:
                print("ERR: Unable to generate Personality Trait")

        if values["-IDEAL-"] == True:
            try:
                npc.ideal_gen()
                print("Ideal Successfully Generated!\n")
            except:
                print("ERR: Unable to generate Ideal")

        if values["-BOND-"] == True:
            try:
                npc.bond_gen()
                print("Bond Successfully Generated!\n")
            except:
                print("ERR: Unable to generate Bond")

        if values["-FLAW-"] == True:
            try:
                npc.flaw_gen()
                print("Flaw Successfully Generated!\n")
            except:
                print("ERR: Unable to generate Flaw")

        if values["-PERSONALITY QUIRK-"] == True:
            try:
                npc.quirk_gen()
                print("Personality Quirk Successfully Generated!\n")
            except:
                print("ERR: Unable to generate Personality Quirk")

        if values["-PHYSICAL TRAIT-"] == True:
            try:
                npc.physical_gen()
                print("Physical Trait Successfully Generated!\n")
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
        print("File successfully created.\n")
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