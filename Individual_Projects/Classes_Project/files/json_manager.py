#PS 1st CP2 This file manages data so that it can be stored across runs
import json


#JSON reader
def JSON_reader():
    with open("Individual_Projects/Classes_Project/files/shapes.json","r") as Shapes:
        data = json.load(Shapes)
        return data



#JSON file saving func (list of user information)
def JSON_writer(new_shape):
    #open the JSON with the writing and reading mode and make a dictionary with the current user information
    with open("Individual_Projects/Classes_Project/files\shapes.json", "r+") as shapes:
        #create a new user dictionary with all data taken from bg2's user creation screen
        data = json.load(shapes)
        data.update({new_shape["Shape"]:new_shape})
        shapes.truncate(0)
        shapes.seek(0)
        #upload that new dictionary to the JSON
        json.dump(data,shapes,indent=4)
