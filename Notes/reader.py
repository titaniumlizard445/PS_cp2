#PS 1st file reading notes

import csv

while True:
    try:
        with open("Notes/readable_file.txt","r") as file:
            content = file.read()
            print(content.upper())
    except:
        print("file not found")

    else:
        print("code is workable")
        break


try:
    with open("Notes\Coolthing.csv",mode="r") as not_file:
        content = csv.reader(not_file)
        headers = next(content)
        rows = []
        for x in content:
            rows.append({headers[0]: x[0],headers[1]: x[1]})
            print(x[0])
            print(x[1])
        print(rows)
except:
    print("Ya can't find tha file")
else:
    for y in rows:
        print(y)