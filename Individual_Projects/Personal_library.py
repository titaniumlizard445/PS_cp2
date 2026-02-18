#PS 1st personal library

#categorize video games
#parts of an item: Title, Company/Studio , Year, Is it part of a series or franchise?

#Note to future development: *NEW* means that it was implemented for the file writing update

#Import CSV *NEW*
import csv

#Stupid proofinator *NEW* :::: inserted in input spots
def stupid_proofed_inputs(message,method,*allowed_inputs):
    while True:
        if method == "lower":
            user_data = input(f"\n\n{message}").strip().lower()
        elif method == "title":
            user_data = input(f"\n\n{message}").strip().title()
        else:
            print("Programmer ERROR: used improper method")
        if user_data in allowed_inputs:
            return user_data
        if "_" in allowed_inputs:
            return user_data
        else:
            print("\n\nYou have inputed something in incorrectly please try again")


#Parser to load data into the library
def parser():
    with open("Individual_Projects/Personal_library_data.csv",mode="r") as library:
        content = csv.reader(library)
        headers = next(content)
        rows = []
        for x in content:
            rows.append({headers[0]: x[0],headers[1]: x[1],headers[2]:x[2],headers[3]:x[3]})
    return rows


#decorator for loops
def decorator(func):
    def looper(*args):
        while True:
            func(*args)
            done = stupid_proofed_inputs("Are you done using this tool (y/n) ?","lower","y","n")
            if done == "y":
                break
            elif done == "n":
                print("continue")
            else:
                print("Please only type y for yes or n for no.")
    return looper


#view library
def view(lib,cryteria):
    #ask for display mode (simple/detailed) *NEW*
    #loop through set and print each item on an individual line
    print(cryteria)
    for x in lib:
        print(x)

#decor
@decorator
#Add to library
def AddToLibrary(lib,cryteria):
    #ask for and store all the criteria as listed above
    game = []
    for x in cryteria:
        if x == "Is it part of a series?":
            while criteria_part != "yes" or criteria_part != "no":
                criteria_part = stupid_proofed_inputs("Is this game a part of a series (yes/no)?","title","Yes","No")
        else:
            criteria_part = stupid_proofed_inputs(f"What is the {x}?","title","_")
        #combine it all into a packet to add to library
        game.append(criteria_part)
    lib.append(game)
    return lib

#decor
@decorator
#search library
def search(lib):
    #counter to see how many items match search
    counter = 0

    #ask user what they would like to search by
    search_type = stupid_proofed_inputs("What criteria  would you like to search by (title,company/studio,year,part of series or franchise)?: ","lower","title","company","franchise","series","studio","year")

    if "title" in search_type:
        #ask user for item
        title = stupid_proofed_inputs("What is the title of the game?","title","_")

        #display to user if the item is in the library and display item
        for x in lib:
            if title in x["Title"]:
                print(x)
                counter += 1
        if counter <= 0:
            print(f"No games match search {title}")
        else:
            print(f"All games that match {title} are found")

    elif "company" in search_type or "studio" in search_type:
        #ask user for item
        company_studio = stupid_proofed_inputs("What is the Company/studio who made the game? ","title","_")

        #display to user if the item is in the library and display item
        for x in lib:
            if company_studio in x["Company/Studio"]:
                print(x)
                counter+=1
        if counter <= 0:
            print(f"No games match search {company_studio}")
        else:
            print(f"All games that match {company_studio} are found")

    elif "year" in search_type:
        #ask user for item
        year = ""

        while not year.isnumeric():
            year = input("What year was the game released (number)? ").strip()
        #display to user if the item is in the library and display item

        for x in lib:
            if year in x["Year"]:
                print(x)
                counter+=1
        if counter <= 0:
            print(f"No games match search {year}")
        else:
            print(f"All games that match {year} are found")        

    elif "series" in search_type or "franchise" in search_type:
        #ask user for item
        series = stupid_proofed_inputs("Is the game part of a series or franchise? ","lower","yes","no")

        #display to user if the item is in the library and display item
        for x in lib:
            if series in x["Is the game part of a series or franchise?"]:
                print(x)
                counter+=1
        if counter <= 0:
            print(f"No games match search {series}")
        else:
            print(f"All games that match {series} are found") 
    
    else:
        print("Not a valid search category, please try again")


#decor
@decorator
#remove from library
def remove(lib,cryteria):
    #counter for seeing if anything was found
    counter = 0

    #Display library
    view(lib,cryteria)

    #ask for which item to remove
    title_of_game_to_remove = stupid_proofed_inputs("Enter the Title of the Game you would like to remove: ","title","_")
    for x in lib:
        if title_of_game_to_remove in x[0]:
            lib.remove(x)
            counter+=1
    if counter == 1:
        print("One Game removed sucessfully")
    elif counter > 1:
        print("More than one Game was deleted (if you did not want that to happen then you should have been more specific about your Game title)")
    elif counter == 0:
        print("Game Not found")

#decor
@decorator
#edit existing item
def Edit(lib,cryteria):
    #counter for seeing how many items match search]
    counter = 0
    #Display library
    view(lib,cryteria)

    #ask User for which Item they want to access
    game_to_access = stupid_proofed_inputs("What is the title of the game you want to access?","title","_")
    
    #checks if item exists
    for x in lib:
        if game_to_access in x:
            counter+=1
            game = x
    print(f"games found {counter}")

    #if the item exists
    if counter == 1:
        #ask which part of the item they want to change
        part = stupid_proofed_inputs(f"What part of {game} do you want to change (title,company/studio,year,part of series or franchise)?: ","lower","title","company","studio","year","series","franchise")
        change = stupid_proofed_inputs("What would you like to change it to?: ","title","_")

        #Save new item
        if "title" in part:
            game[0] = change
        elif "company" in part or "studio" in part:
            game[1] = change
        elif "year" in part:
            game[2] = change
        elif "series" in part or "franchise" in part:
            game[3] = change
    
        #else display that item does not exist
    elif counter > 1:
        print("Please narrow down your search so 1 game matches your search.")
    else:
        print(f"{game_to_access} does not exist within this library")

#writer for the csv *NEW*
def writer_code(library1):
    with open("Individual_Projects/Personal_library_data.csv", "w", newline="") as library2:
        fieldnames = ["Title","Company/Studio","Year","Is it part of a series or franchise?"]
        writer = csv.DictWriter(library2,fieldnames=fieldnames)
        writer.writeheader()
        if library1:
            for y in library1:
                for x in y:
                    writer.writerow({"Title": x[0] , "Company/Studio" : x[1], "Year": x[2] ,"Is it part of a series or franchise?":x[3]})
        



#decor
@decorator
#main
def main():
    #moved info to main *NEW*
    library = parser()
    criteria = ("Title","Company/Studio","Year","Is it part of a series or franchise?")
    #UI for choosing function
    print("Library Options:\n1.View Library\n2.Add a Game\n3.Search Library\n4.Remove a game\n5.Edit an Existing item\n")
    choice = stupid_proofed_inputs("\nPlease Enter The Number Of An Option Here: ","lower","1","2","3","4","5")
    if choice == "1": 
        view(library,criteria)
    elif choice == "2":
        AddToLibrary(library,criteria)
    elif choice == "3":
        search(library)
    elif choice == "4":
        remove(library,criteria)
    elif choice == "5":
        Edit(library,criteria)
    else:
        print("Invalid Choice, please enter the number only")
    print("Finished using library tool")
    writer_code(library)
main()
