#PS 1st CP2 Insert Game and Character classes here

import random
from stupid_proofable import *
from Individual_Projects.Class_Relationships_Project.files.file_management import *

#Use agregation for Game to Characters
class Game:
    def __init__(self,characters = []):
        self.characters = characters
    
    def add_character(self,character):
        self.characters.append()
    
    def __str__(self):
        print(self.characters)
    
    def battle(self):
        print("Choose First Fighter\n\n")
        
        character_info = JSON_reader()
        characters = character_info.keys()
        
        for x in characters:
            print(x)
    
        for x in characters:
            print(f"{x}")

        #chooser
        first = stupid_proofed_inputs("\n\nEnter here: ","None","_")
        while first not in characters:
            print("Not Valid Character, Please Try Again")
            first = stupid_proofed_inputs("\n\nEnter here: ","None","_")
        
        print("Choose Second Fighter\n\n")
        
        second = stupid_proofed_inputs("\n\nEnter here: ","None","_")
        while second not in characters:
            print("Not Valid Character, Please Try Again")
            second = stupid_proofed_inputs("\n\nEnter here: ","None","_")
        
        first_info = character_info[first]
        second_info = character_info[second]
        first_health = first_info["Stats"]["Health"]
        second_health = second_info["Stats"]["Health"]
        
        print("========== THE BATTLE COMENCETH ===========")
        while first_health != 0 or second_health != 0:
            #P1 Turn
            if first_health != 0 or second_health != 0:
                
                print(f"{first}'s Turn")
                print("\n\nChoose an Ability:")
                
                first_abilities = first_info["Abilities"].keys()
                for x in first_abilities:
                    print(x)
                
                ability_chosen = stupid_proofed_inputs("Enter here: ","None","_")
                while ability_chosen not in first_abilities:
                    print("Not Valid Ability, Please Try Again")
                    ability_chosen = stupid_proofed_inputs("Enter here: ","None","_")
                
                damage = first_abilities[ability_chosen]["Damage"]*random.randint(1,25)
                second_health -= damage
                
                if second_health < 0:
                    second_health = 0
                
                print(f"{first} did {damage} damage! {second} Health: {second_health}")
            
            #P2 Turn
            if first_health != 0 or second_health != 0:
                
                print(f"{second}'s Turn")
                print("\n\nChoose an Ability:")
                
                second_abilities = second_info["Abilities"].keys()
                for x in second_abilities:
                    print(x)
                
                ability_chosen = stupid_proofed_inputs("Enter here: ","None","_")
                while ability_chosen not in second_abilities:
                    print("Not Valid Ability, Please Try Again")
                    ability_chosen = stupid_proofed_inputs("Enter here: ","None","_")
                
                damage = second_abilities[ability_chosen]["Damage"]*random.randint(1,25)
                first_health -= damage
                
                if first_health < 0:
                    first_health = 0
                
                print(f"{second} did {damage} damage! {first} Health: {first_health}")
        
        print("\n\n========= THE BATTLE ENDETH ==========\n\n")

        if first_health == 0:
            print(f"{second} won!")
        
        elif second_health == 0:
            print(f"{first} won!")

#Methods to be in the Game class: Battle, Display All Characters, Level Up system

#Use Inheritance for characters being a class classes needed: Well rounded (Has all base stats), Archer, Warrior, Mage, Engineer

class DefaultCharacter:
    def __init__(self):
        pass

    #send info to JSON
    def packager():
        pass

class WellRounded:
    def __init__(self):
        pass

class Archer:
    def __init__(self):
        pass

class Warrior:
    def __init__(self):
        pass

class Mage:
    def __init__(self):
        pass

class Engineer:
    def __init__(self):
        pass