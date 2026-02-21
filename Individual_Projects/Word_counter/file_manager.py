#PS 1st file for dealing with txt data


#file checker - checks if the file path the user inputed is correct
def file_is_exist(file_name):
    try:
        with open(file_name,"r") as file:
            print("\n\nFile found")
            return True
    except:
        print("\n\nThe file has not been found")
        return False


#file writer - takes in user data and then appends it to the data in the txt
def text_writer(file_name,new_text):
    with open(file_name, "r") as file:
        row_number = 0
        rows = []
        counter = -1
        #create a list object for each row
        for x in file:
            rows.append(x.strip())
            row_number +=1
        #try to find where there is an empty gap
        for x in rows:
            counter +=1
            if x == "":
                break
    with open(file_name, "w") as file:
    #put the new content where the empty gap is
        rows.insert(counter,new_text)
        for x in range(row_number):
            file.write(f"{rows[x]}\n")


#file reader - opens the file and then outputs what is on the file
def reader(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        return content


#actual word counter function
def word_counter(text):
    words = text.split()
    counter = 0
    for x in words:
        #makes sure there was no double spaces
        if not x == "":
            counter+=1
    return counter
