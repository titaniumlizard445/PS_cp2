#PS 1st main code

#Import code
from sub_ui import *


@decorator
def main():
    print("Welcome to the Character Creator\nChoose an Option:\n1. Create New Character\n2. View One Character's Information\n3. Level up Character\n4. Battle Characters\n5.View All Created Characters\n6.Equip/Remove Armor or Weapons from a character\n7.Assign New Abilities\n8.Exit")
    main_choice = stupid_proofed_inputs("Enter here: ","number","1","2","3","4","5","6","7")

    match main_choice:
        case "1":
            character_creator()
        case "2":
            view_single()
        case "3":
            level_up()
        case "4":
            Game.battle()
        case "5":
            view_all()
        case "6":
            print("EQUIP/REMOVE HERE")
        case "7":
            print("ABILITY MAKER HERE")
        case "8":
            print("Type No in Exit Prompt")

main()