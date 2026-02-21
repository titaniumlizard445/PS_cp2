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

#import file manager and time manager functions
from file_manager import *
from time_manager import *


#main UI
def main():
    valid_file = False
    new_text = ""
    while True:
        while not valid_file:
            file = stupid_proofed_inputs("What is the file path of the file you would like to access? (exact name)(txt files only)\nEnter here: ","none","_")
            #call is_exist function
            valid_file = file_is_exist(file)
        
        print("Welcome to the document word count updater\n Would you like to\n1) Update the document\n2) View document\n3)Add content to the end of the document\n4)Help")
        choice = stupid_proofed_inputs("Enter here: ","number","1","2","3","4")
        text = reader(file)
        match choice:
            case "1":
                text_writer(file,new_text)
                word_count = word_counter(text)
                timestamp(file,word_count)
            case "2":
                print(text)
            case "3":
                new_text = stupid_proofed_inputs("Write text to add to the end of the doc here: ","none","_")
            case "4":
                print("\n\nHelp Guide:\nWhen using the word counter code, there are a few things to remember,\n1) Whenever you are accessing a file the program does not add anything to it. But, once you add content to the document, the program will add the content to that document as well as add a timestamp of when the document was updated.\n2) Whenever you add content to the document, it will not be saved to the file until you select the save feature on the main menu. If you don't, all of your content you wanted to add will vanish.\n3) The program will ask for your file path after every iteration so make sure you keep the relative path on your copy/paste clipboard.")
        done = stupid_proofed_inputs("Are you done using this program? (y/n): ","lower","y","n")
        if done == "y":
            break
        elif done == "n":
            print("continue")
        else:
            print("Please only type y for yes or n for no.")
main()
