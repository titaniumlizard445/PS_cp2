#PS 1st notes for writing to files


import csv


try:
    with open("Notes/readable_file.txt", "r+") as file_txt:
        content = file_txt
        content += "\nMore stuff on the file"
        file_txt.write(content)
except:
    print("File not found")
else:
    print("file written successfully")

try:
    with open("Notes/readable_file.txt", "a") as yay_txt:
        yay_txt.write("\nMORE STUFF")
except:
    print("File Not found")
else:
    print("2nd file written")



try:
    with open("Notes\Coolthing.csv", "r+", newline="") as csv_file:
        fieldnames = ["username", "Message"]
        reader = csv.reader(csv_file)
        for line in reader:
            print(f"{fieldnames[0]}:{line[0]} Message: {line[1]}")
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({"username": "THE USER" , "Message" : "Woah Woah Woah Wow"})
        writer.writerow({"username": "Bob the USER" , "Message" : "I can bulid it"})
        writer.writerow({"username": "Bob the programmer" , "Message" : "I CAN'T FIX IT"})
        writer.writerow({"username": "Bretts dog" , "Message" : "Ruff"})
        writer.writerow({"username": "Bretts dad" , "Message" : "Brett, go clean your room"})
except:
    print("File not found")
else:
    print("csv file written")