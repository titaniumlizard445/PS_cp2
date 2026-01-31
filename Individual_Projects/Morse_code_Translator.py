#PS 1st CP2 morse code translator


#Stupid proofinator
def stupid_proofed_inputs(message,*allowed_inputs):
    while True:
        user_data = input(f"\n\n{message}").strip().upper()
        if user_data in allowed_inputs:
            return user_data
        elif "_" in allowed_inputs:
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

@onlininator
#english to morse code
def english_to_morse(english_letters,morse_letters):
    #take a user input for a message
    message = stupid_proofed_inputs("What is the message you would like to encrypt into morse code (No numbers and only periods for punctuation)?: ","_")
    #split message into words
    words = message.split(" ")
    
    new_message = ""
    #for each word
    for x in words:
        #for each character
        new_word = ""
        for y in x:
            #find the index of that letter
            letter = english_letters.index(y)
            #turn it into morse code
            letter = morse_letters[letter]
            #add the translated version of the index to the end of a string
            new_word = new_word + " " + letter
        #concatenate word with previous string and a space between
        new_message = new_message + " ..--.- " + new_word
    #Display message
    print(f"Your encoded message is: {new_message}")

@onlininator
#morse code to english
def morse_to_english(english_letters,morse_letters):
    #take in user input for morse code message
    morse_message = stupid_proofed_inputs("What is the morse code message?(Include spaces between each letter and the morse code underscore for a space):","_")
    #split the message by spaces
    split_message = morse_message.split(" ")
    #for each chunk
    english_message = ""
    letter = ""
    for x in split_message:
        #guard line against double spacing
        if x == "":
            continue
        #find what it means
        index = morse_letters.index(x)
        letter = english_letters[index]
        #if it is a _
        if letter == "_":
            #turn it into a " "
            letter = " "
            #add it to the end of a string
            english_message += letter
        #else
        else:
            #add it to the end of a string
            english_message += letter
    #Display message
    print(f"Your decoded message is: {english_message}")

@onlininator
#main
def main():
    #tuples for english and morse code letters
    english = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",".","_")
    morse_code = (".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.",".-.-.-","..--.-")
    
    #Welcome user
    print("\n\nWelcome to a morse code translator!")
    
    #input for which function user would like to use
    choice = stupid_proofed_inputs("What would you like to do?\n1)Use the English to Morse Code translator\n2)Use the Morse Code to English translator\n\nEnter the number here: ","1","2")
    #match for which one they want
    match choice:
        case "1":
            english_to_morse(english,morse_code)
        case "2":
            morse_to_english(english,morse_code)

main()
