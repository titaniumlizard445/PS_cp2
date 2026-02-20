#PS 1st word counter UI

#Useful functions
def stupid_proofed_inputs(message,method,*allowed_inputs):
    while True:
        user_data = ""
        if method == "lower":
            user_data = input(f"\n\n{message}").strip().lower()
        elif method == "title":
            user_data = input(f"\n\n{message}").strip().title()
        elif method == "number":
            while not user_data.isnumeric():
                user_data = input(f"\n\n{message}").strip()
                if not user_data.isnumeric():
                    print("\n\nWrite a number")
        elif method == "none":
            user_data = input(f"\n\n{message}").strip()
        else:
            print("Programmer ERROR: used improper method")
        if user_data in allowed_inputs:
            return user_data
        if "_" in allowed_inputs:
            return user_data
        else:
            print("\n\nYou have inputed something in incorrectly please try again")


#decorator for loops
def decorator(func):
    def looper(*args):
        while True:
            func(*args)
            if func.__name__ == "main":
                done = stupid_proofed_inputs("Are you done using this program? (y/n) ?","lower","y","n")
            else:
                done = stupid_proofed_inputs("Are you done using this tool? (y/n) ?","lower","y","n")
            if done == "y":
                break
            elif done == "n":
                print("continue")
            else:
                print("Please only type y for yes or n for no.")
    return looper


#import file manager and time manager functions
from file_manager import *
from time_manager import *

@decorator
#main UI
def main():
    print("Welcome to the document word count updater\n Would you like to\n1) Update the document\n2) View document\n3)Add content to the end of the document")
    choice = stupid_proofed_inputs("Enter here: ","number","1","2","3")
    match choice:
        case "1":
            print("This is where the document update info goes")
        case "2":
            print("View document stuff goes here")
        case "3":
            print("Add content to the document goes here")
main()