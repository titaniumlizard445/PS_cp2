#PS 1st Fractal patterns generator

import turtle
import math

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


#triangle draw-er
def draw_triangle(size,counter=3):
    if counter == 0:
        return
    else:
        draw_triangle(size,counter-1)
        turtle.forward(size)
        turtle.right(120)

#recurser part
def triangles(depth,size=256):
    circumradius = (math.sqrt(3)/3)*size
    if depth == 0:
        turtle.penup()
        turtle.forward(circumradius)
        turtle.pendown()
        turtle.right(30)
        turtle.right(240)
        draw_triangle(size*2)
        turtle.penup()
        turtle.right(30)
        turtle.forward((math.sqrt(3)/3)*size*2)
        turtle.right(60)
        return
    else:
        turtle.forward(size)
        turtle.right(120)
        triangles(depth-1,size/2)
        
        

#snowflake draw-er


#tree draw-er



#save function
def save():
    #get the screen
    turtle_screen= turtle.getscreen()
    #get the canvas
    turtle_screen.getcanvas().postscript(file="Fractal.png")

#then use the on keypress function to detect when the user wants to save a drawing
#use turtle.onkeypress(save function, key="(key)")


#main function
def main():

    #options for UI (recursion depth, turtle color, background color, save?, fractal type)
    print("Hello and welcome to the turtle graphics fractal generator!\nLets get started with some information:\n\n")
    fractal_type = stupid_proofed_inputs("What type of fractal would you like to use? (options: triangle,snowflake,tree)\nEnter here: ","lower","triangle","snowflake","tree")
    depth = int(stupid_proofed_inputs("How many iterations would you like the fractal to go to? (options: numbers 1-7)","number","1","2","3","4","5","6","7"))
    turtle_color = stupid_proofed_inputs("What is the color you would like the turtle to be? (options: (Rainbow colors),black,white,grey,cyan)\nEnter here: ","lower","red","orange","yellow","green","blue","purple","black","white","grey","cyan")
    back_color = stupid_proofed_inputs("What is the color you would like the background to be?(options: black, white, grey, beige, brown)\n","lower","black","white","grey","beige","brown")
    save_ask = stupid_proofed_inputs("Would you like the program to automatically save the fractal for you when it is done drawing it?(options: y (which means yes), n (means no))","lower","y","n")

    #setup the turtle
    
    screen = turtle.Screen()
    screen.bgcolor(back_color)
    turtle.color(turtle_color)

    #get the right fractal type
    match fractal_type:
        case "triangle":
            triangles(depth)
        case "snowflake":
            print("snowflake function goes here")
        case "tree":
            print("tree function goes here")
    
    #hide the turtle
    #turtle.hideturtle()
    turtle.done()
    
    if save_ask == "y":
        save()
    
main()
