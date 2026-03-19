#PS 1st CP2 This is where all of the user input error handling functions go

def stupid_proofed_inputs(message,method,*allowed_inputs):
    while True:
        user_data = ""
        if method == "lower":
            user_data = input(f"\n\n{message}").strip().lower()
        elif method == "title":
            user_data = input(f"\n\n{message}").strip().title()
        elif method == "number":
            while not user_data.isnumeric():
                user_data = input(f"\n\n{message}").strip()
                if not user_data.isnumeric():
                    print("\n\nWrite a number")
        elif method == "none":
            user_data = input(f"\n\n{message}").strip()
        else:
            print("Programmer ERROR: used improper method")
        if user_data in allowed_inputs:
            return user_data
        if "_" in allowed_inputs:
            return user_data
        else:
            print("\n\nYou have inputed something in incorrectly please try again")


def positivity(user_input):
    clean_input = user_input.split()
    if "-" in clean_input:
        print("Positive numbers only")
    else:
        return
