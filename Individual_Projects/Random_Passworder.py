#PS 1st random password generator
#requirements length, upper/lower letters, numbers, and spec. characters

#import random
import random
# uppercaseletters (password)

def upperletters(password): 
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper_letter =random.choice(letters).upper()
    password += upper_letter
    return password

#lowercase letters (password)

def lowerletters(password):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lower_letter = random.choice(letters)
    password += lower_letter
    return password

#Special Characters (password)

def specials(password):
    special = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]",":",";","'",'"',"<",">",",",".","?","/","\\","|","`","~"]
    special_char = random.choice(special)
    password += special_char
    return password

#numbers (password)
def numbers(password):
    number = str(random.randrange(0,10))
    password += number
    return password

#main
def main():
    #loop
    while True:
        #list for types of things
        accepted_requirements =[]
        rand_password = ""
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
        length = int(input("how long would you like your password to be? (whole number): ").strip())
        #for characters in password
        for x in range(length):
            choice = ""
            #choose a type of character 
            choice = random.choice(accepted_requirements)
            #run associated helper function
            match choice:
                case "":
                    print("No requirements specified")
                case "uppers":
                    rand_password = upperletters(rand_password)
                case "lowers":
                    rand_password = lowerletters(rand_password)
                case "specials":
                    rand_password = specials(rand_password)
                case "numbers":
                    rand_password = numbers(rand_password)
        #display password
        print(f"Your password is {rand_password}")
        #ask if user is done with program
        done = input("Would you like to generate another password? (y/n)").strip().lower()
        #if done
        if done == "n":
            #leave
            print("goodbye")
            break

main()
