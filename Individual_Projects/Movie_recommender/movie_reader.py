#PS 1st Movie recommender

import csv

#get the onlinator and stupid proofed inputs from morse code translator

#Stupid proofinator
def stupid_proofed_inputs(message,*allowed_inputs):
    while True:
        user_data = input(f"\n\n{message}").strip().lower()
        if user_data in allowed_inputs:
            return user_data
        if "_" in allowed_inputs:
            return user_data
        else:
            print("\n\nYou have inputed something in incorrectly please try again")


#continous function
def onlininator(func):
    def wrapper(*args):
        while True:
            func(*args)
            done = stupid_proofed_inputs("Are you done using this? y/n:","y","n")
            if done == "y":
                break
            else:
                print("\n\nContinue")
    return wrapper


#pretty-ifier func
def pretty(csv_info,headers):
    #create rows for each item
    rows = []
    #assign them to dictionaries
    for x in csv_info:
        rows.append({headers[0]:x[0],headers[1]:x[1],headers[2]:x[2],headers[3]:x[3],headers[4]:x[4],headers[5]:x[5]})
    return rows

#filter boy func
def searcher(content,headers):
    #asks for what type of search they would like (genre, director, actor(s), and length)
    #asks for first search criteria
    cryteria1 = stupid_proofed_inputs("What is the first search criteria that you would like to use? (Title,Genre,Director,Actors or length)\nEnter here: ","genre","director","actors","actor","length","title")
    #asks for second search criteria
    cryteria2 = stupid_proofed_inputs("What is the second search criteria that you would like to use? (Title,Genre,Director,Actors or length)\nEnter here: ","genre","director","actors","actor","length","title")


    specific1 = ""
    mode1 = ""
    #finds which index to search
    match cryteria1:
        case "title":
            specific1 = stupid_proofed_inputs("\nEnter the title of the movie here (exact spelling): ","_")
        case "genre":
            specific1 = stupid_proofed_inputs("\nEnter the genre of the movie here (exact spelling): ","_")
        case "director":
            specific1 = stupid_proofed_inputs("\nEnter the director of the movie here (exact spelling): ","_")
        case "actor":
            specific1 = stupid_proofed_inputs("\nEnter the actor of the movie here (exact spelling): ","_")
        case "actors":
            specific1 = stupid_proofed_inputs("\nEnter the actors (separated by commas) of the movie here (exact spelling): ","_")
        case "length":
            length1 = stupid_proofed_inputs("\nEnter the minimum length in minutes of the movie here: ","_")
            length2 = stupid_proofed_inputs("\nEnter the maximum length in minutes of the movie here: ","_")
            mode1 = "length"

    mode2 = ""
    match cryteria2:
        case "title":
            specific2 = stupid_proofed_inputs("\nEnter the title of the movie here (exact spelling): ","_")
        case "genre":
            specific2 = stupid_proofed_inputs("\nEnter the title of the movie here (exact spelling): ","_")
        case "director":
            specific2 = stupid_proofed_inputs("\nEnter the title of the movie here (exact spelling): ","_")
        case "actor":
            specific2 = stupid_proofed_inputs("\nEnter the title of the movie here (exact spelling): ","_")
        case "actors":
            specific2 = stupid_proofed_inputs("\nEnter the title of the movie here (exact spelling): ","_")
        case "length":
            length3 = stupid_proofed_inputs("\nEnter the minimum length in minutes of the movie here: ","_")
            length4 = stupid_proofed_inputs("\nEnter the maximum length in minutes of the movie here: ","_")
            mode2 = "length"

    searched_content = []
    if mode1 != "length":
        #for each item
        for x in content:
            #if the category searched in matches item
            if specific1 in x[cryteria1.title()].split():
                #add whole item to acceptable content
                searched_content.append(x)
    else:
        for x in content:
            #length comparison
            if int(x["Length (min)"]) >= int(length1) and int(x["Length (min)"]) <= int(length2):
                searched_content.append(x)
    
    if mode2 != "length":
        #for each item
        for x in searched_content:
            #if the category searched in does not match item
            if specific2 not in x[cryteria1.title()].split():
                #add whole item to acceptable content
                searched_content.append(x)
    else:
        for x in searched_content:
            #length comparison
            if int(x["Length (min)"]) >= int(length3) and int(x["Length (min)"]) <= int(length4):
                continue
            else:
                searched_content.remove(x)
    
    #cool_data = pretty(searched_content,headers)
    for x in searched_content:
        print(f"Title: {x["Title"]}, Director: {x["Director"]}, Genre: {x["Genre"]}, Rating: {x["Rating"]}, Length: {x["Length (min)"]}, Notable actors: {x["Notable Actors"]}")
    
#parser function
def parser(mode):
    try:
        #open the file
        with open("Individual_Projects/Movie_recommender/Movies list.csv",mode="r") as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            cool_data = pretty(content,headers)
            #use function for what the user wants to do
            if mode == "search":
                searcher(cool_data,headers)
            if mode == "see all":
                for x in cool_data:
                    print(f"Title: {x["Title"]}, Director: {x["Director"]}, Genre: {x["Genre"]}, Rating: {x["Rating"]}, Length: {x["Length (min)"]}, Notable actors: {x["Notable Actors"]}")
    except:
        print("An Error Occured Loading The File")


#use the onlininator on this
@onlininator
#main
def main():
    #intro
    print("Welcome to the Movie Recommender 5000! you can either see all the movies or search for a set few.")
    #ask for what the user wants to do
    mode = stupid_proofed_inputs("Which mode would you like to use? ('search' or 'see all')\nEnter here:","search","see all")
    #use parser function
    parser(mode)

main()