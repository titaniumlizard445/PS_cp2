#PS 1st this file finds the timestamp of when the document was last edited 

import time as clock

#timestamper
def timestamp(file_name,word_count):
    stamp = clock.ctime()
    with open(file_name, "a") as file:
        file.write(f"\nWord count: {word_count}, Last updated: {stamp}\n")
