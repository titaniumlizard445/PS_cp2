#PS 1st personal library

#categorize video games
#parts of an item: title, company/studio , year, part of a series?

library = {}

#decorator for loops
def decorator(func):
    def looper():
        while True:
            func
            done = input("Are you done using this tool (y/n) ?").strip().lower()
            if done == "y":
                break
            elif done == "n":
                print("continue")
            else:
                print("Please only type y for yes or n for no.")
    return looper



#view library
def view(lib):
    #loop through set and print each item on an individual line
    for x in lib:
        print(x)

#decor
@decorator
#Add to library
def AddToLibrary(lib):
    #ask for and store all the criteria as listed above
    #combine it all into a packet to add to library
    print("h")

#decor
#search library
    #ask user what they would like to search by
    #ask user for the search criteria
    #display to user if the item is in the library and display item

#decor
#remove from library
    #Display library
    #ask for which item to remove

#decor
#edit existing item
    #Display library
    #ask User for which Item they want to access
    #ask which part of the item they want to change
    #Save new item

#decor  
#main
    #UI for choosing function
        

