#PS 1st Movie recommender


import csv


#get the onlinator and stupid proofed inputs from morse code translator

#Stupid proofinator
def stupid_proofed_inputs(message,*allowed_inputs):
    while True:
        user_data = input(f"\n\n{message}").strip().title()
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


#filter boy func

#parser function (mode)
    #open the file
    #use function for what the user wants to do




#main()