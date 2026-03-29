#PS 1st CP2 UI stuff

#get class stuff
from character_classes import *
#get stoobid proofing funcs
from stupid_proofable import *
#get JSON manipulation funcs
from Individual_Projects.Class_Relationships_Project.files.file_management import *


#character chooser for smaller code size
def char_chooser():
    character_info = JSON_reader()
    characters = character_info.keys()
    
    for x in characters:
        print(f"{x}")

    user_choice = stupid_proofed_inputs("\n\nEnter here: ","None","_")

    while user_choice not in characters:
        user_choice = stupid_proofed_inputs("\n\nEnter here: ","None","_")
    return user_choice

#UI for Character Creator
def character_creator():
    #info from user inputs needed: Name, Class - Class makes a bunch of defaults like abilities, stats and weapons
    print("\n\n========= CHARACTER CREATOR =========\n\n")
    print("Create a new character\n\n")
    
    name = stupid_proofed_inputs("Enter the name of the character here: ","None","_")
    
    print("\n\nClasses\n1. Well Rounded\n2. Archer\n3. Warrior\n4. Mage\n5. Engineer")
    
    chosen_class = stupid_proofed_inputs("Enter Class here: ","number","1","2","3","4","5")
    
    match chosen_class:
        case "1":
            print("Well rounded Chosen")
        case "2":
            print("Archer Chosen")
        case "3":
            print("Warrior Chosen")
        case "4":
            print("Mage Chosen")
        case "5":
            print("Engineer Chosen")

#Level One Character Up
def level_up():
    print("\n\n============= LEVEL UP CHARACTER ================\n\n")
    print("Choose a Character to level up")
    
    character_info = JSON_reader()
    user_choice = char_chooser()

    character_info[user_choice["Level"]] += 1

    print(f"\n\nCharacter Leveled Up Sucessfully, Level:{character_info[user_choice]["Level"]}")

#View Single Character
def view_single():
    print("================ Single Character Stats ===================")
    
    characters = JSON_reader()
    user_choice = char_chooser()
    
    print("================ CHARACTER STATS ================")
    print(f"Name: {user_choice}\nDefense: {characters[user_choice]["Stats"]["Defense"]}\nStrength: {characters[user_choice]["Stats"]["Strength"]}\nHP: {characters[user_choice]["Stats"]["Health"]}\nIntelligence: {characters[user_choice]["Stats"]["Intelligence"]}\nLevel: {characters[user_choice]["Level"]}\nClass: {characters[user_choice]["Class"]}")
    
    print("Weapons:")
    for x in characters[user_choice]["Weapons"]:
        print(x)
    
    print(f"ARMOR:\nHelmet:{characters[user_choice]["Armor"]["Helmet"]}\nChestPlate: {characters[user_choice]["Armor"]["ChestPlate"]}\nLeggings: {characters[user_choice]["Armor"]["Leggings"]}\nBoots: {characters[user_choice]["Armor"]["ChestPlate"]}")
    
    print("Inventory (Non Weapons or Armor)")
    for x in characters[user_choice]["Inventory"]:
        print(x)
    
    print("Abilities")
    for x in characters[user_choice]["Abilities"].keys():
        print(f"{x}:{characters[user_choice]["Abilities"][x]["Description"]}")

#View All Characters
def view_all():
    characters = JSON_reader().keys()
    for x in characters:
        print(x)