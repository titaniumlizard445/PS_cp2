#PS 1st Movie recommender

import csv

#get the onlinator and stupid proofed inputs from morse code translator

#Stupid proofinator
def stupid_proofed_inputs(message,*allowed_inputs):
    while True:
        user_data = input(f"\n\n{message}").strip().lower()
        if user_data in allowed_inputs:
            return user_data
        else:
            print("\n\nYou have inputed something in incorrectly please try again")


#continous function
def onlininator(func):
    def wrapper(*args):
        while True:
            func(*args)
            done = stupid_proofed_inputs("Are you done using this? y/n:","Y","N")
            if done == "Y":
                break
            else:
                print("\n\nContinue")
    return wrapper


#pretty-ifier func
def pretty(csv_info):
    #create headers and rows for each item
    headers = next(csv_info)
    rows = []
    #assign them to dictionaries
    for x in csv_info:
        rows.append({headers[0]:x[0],headers[1]:x[1],headers[2]:x[2],headers[3]:x[3],headers[4]:x[4],headers[5]:x[5],headers[6]:x[6]})
    return rows

#filter boy func
    #asks for what type of search they would like (genre, director, actor(s), and length)
    #asks for first search criteria
    #asks for second search criteria
    #for each item
        #if the category searched in matches item
            #add whole item to acceptable content

#parser function
def parser():
    try:
        #open the file
        with open("Individual_Projects\Movie_recommender\Movies list.csv",mode="r") as csv_file:
            content = csv.reader(csv_file)
            #use function for what the user wants to do
    except:
        print("An Error Occured Loading The File")


#use the onlininator on this
@onlininator
#main
def main():
    #ask for what the user wants to do
    mode = stupid_proofed_inputs("Which mode would you like to use?","acceptable option")
    #use parser function