#Calculating class functions go here

class Quadrilaterals:
    def __init__(self,side1_length,side2_length):
        self.side1_length = side1_length
        self.side2_length = side2_length
    #handle shape type in UI ex. square, trapezoid, kite


    #Help Screen
    def __str__(self):
        return print("In the Quadrilateral Calculator You can calculate the Area and Perimeter of the following:\n1.Square/Rectangle\n2.Kite\n3.Trapezoid,\n4.Parallelogram\n5.Rhombus")


    def Normal(self,side1_length,side2_length):
        Area = side1_length * side2_length
        Perimeter = (side1_length*2)+(side2_length*2)
    
    def Trapezoid(self,side1_length,side2_length):
        print("POOTIS CODE HERE")