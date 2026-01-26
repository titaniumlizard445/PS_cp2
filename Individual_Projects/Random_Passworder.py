#PS 1st random password generator
#requirements length, upper/lower letters, numbers, and spec. characters

#import random
import random
# uppercaseletters (password)

def upperletters(password): 
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    password.append(random.choice(letters).upper())
    return password

#lowercase letters (password)

def lowerletters(password):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    password.append(random.choice(letters))
    return password

#Special Characters (password)

def specials(password):
    special = ["!","@","#","$","%","^","&","*"<"(",")","-","_","+","=","{","}","[","]",":",";","'",'"',"<",">",",",".","?","/","\\","|","`","~"]
    password.append(random.choice(special))
    return password

#numbers (password)
def numbers(password):
    password.append(random.randrange(0,10))
    return password

#main
def main():
    #loop
    while True:
        #list for types of things
        accepted_requirements =[]
        #input for each of the requirements 
        upper_req = input("Would you like upper case letters in your password?  (y/n): ").strip().lower()
        if upper_req == "y":
            accepted_requirements.append("uppers")
        lower_req = input("Would you like lower case letters in your password?  (y/n): ").strip().lower()
        if lower_req == "y":
            accepted_requirements.append("lowers")
        special_req = input("Would you like special characters in your password? (y/n): ").strip().lower()
        if special_req == "y":
            accepted_requirements.append("specials")
        number_req = input("Would you like numbers in your password? (y/n): ").strip().lower()
        if number_req == "y":
            accepted_requirements.append("numbers")
        length = input("how long would you like your password to be? (number): ").strip()
        #for characters in password
        for x in length:
            #choose a type of character 
            #run associated helper function
        #display password
        #ask if user is done with program
        #if yes
            #leave