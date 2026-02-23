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
        lines = file.readlines()
        content_rows = []
        timestamps = []
        
        #separate the rows with content from the rows with timestamps
        for x in lines:
            if x.startswith("Word count:"):
                timestamps.append(x)
            else:
                content_rows.append(x)
        
    with open(file_name, "w") as file:
    #put the new content where the empty gap is
        content_rows.append(new_text)
        file.writelines(content_rows)
        file.write("\n")
        file.writelines(timestamps)


#file reader - opens the file and then outputs what is on the file
def reader(file_name):
    with open(file_name, "r") as file:
        content = file.readlines()
        normal_text = []
        for x in content:
            if not x.startswith("Word count:"):
                normal_text.append(x)
            else:
                break
        return normal_text


#actual word counter function
def word_counter(text):
    counter = 0
    lines = 0
    for x in text:
        lines +=1
        for y in x:
        #makes sure there was no double spaces
            if not y == "":
                counter+=1
            else:
                break
    counter-=lines
    return counter
