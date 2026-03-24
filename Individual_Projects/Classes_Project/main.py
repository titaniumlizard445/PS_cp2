#PS 1st CP2 UI functions and running file
from files.json_manager import *
from sub_ui import *

#main menu things
@decorator
def main_menu():
    
    print("Welcome to the Geometry shape calculator")
    print(f"Shapes Created: {len(JSON_reader())}")
    
    mode = stupid_proofed_inputs("Would you like to Use 2D mode or 3D mode?","title","2D","3D")
    
    if mode == "2D":
        second_dimension()
    
    elif mode == "3D":
        third_dimension()

main_menu()
