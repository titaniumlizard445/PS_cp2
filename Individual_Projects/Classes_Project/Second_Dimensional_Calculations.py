#Calculating class functions go here
from Stupid_proofing import *
import math

class Quadrilaterals:
    def __init__(self,width,height,shape):
        self.width = float(width)
        self.height = float(height)
        self.shape = shape
        self.area = None
        self.perimeter = None
    #handle shape type in UI ex. square, trapezoid, kite


    #Object Info
    def __str__(self):
        return f"Shape: {self.shape}\nArea: {self.area}units^2\nPerimeter: {self.perimeter}units\nWidth:{self.width}units\nHeight: {self.height}units"


    #As All quadrilaterals behave almost the same way in the case of perimeter, I can do almost all perimeters in one function and have Areas as separate functions. Also height will act as a side length for 
    def find_perimeter(self):
        #for parrallelograms and rhombuses because height is not the same as the sides as well as trapezoid and kites
        is_normal = stupid_proofed_inputs("Is your shape a parallelogram, a rhombus,a kite, or a trapezoid?(Enter No or one of the shape names)\nEnter here: ","lower","no","parallelogram","rhombus","trapezoid","kite")
        
        if is_normal == "no":
            self.perimeter = (self.width*2)+(self.height*2)
        
        elif is_normal == "parallelogram" or is_normal == "rhombus":
            slant = positivity(stupid_proofed_inputs(f"How long is the slant of the {is_normal}?(Enter a positive number)\nEnter here: ","number","_"))
            self.perimeter = (self.width*2)+(slant*2)
        
        elif is_normal == "trapezoid":
            slant1 = float(positivity(stupid_proofed_inputs("What is the first slant length?(Enter a positive number)\nEnter here: ","number","_")))
            slant2 = float(positivity(stupid_proofed_inputs("What is the second slant length?(Enter a positive number)\nEnter here: ","number","_")))
            top_base = float(positivity(stupid_proofed_inputs("What is the top side length?(Enter a positive number)\nEnter here: ","number","_")))
            self.perimeter = slant1 + self.width + slant2 + top_base
        
        elif is_normal == "kite":
            side1 = float(positivity(stupid_proofed_inputs("What is the long side length?(Enter a positive number)\nEnter here: ","number","_")))
            side2 = float(positivity(stupid_proofed_inputs("What is the long side length?(Enter a positive number)\nEnter here: ","number","_")))
            self.perimeter = (side1*2)+(side2*2)


    #Normal includes squares rectangles parallelograms and rhombi areas
    def normal_area(self):
        self.area = self.width * self.height

    
    #sides 1 and 2 are bases for the 1/2h(b1*b2)
    def trapezoid(self):
        base2 = positivity(stupid_proofed_inputs("What is the length of the smallest base of the trapezoid?\nEnter here: ","number","_"))
        self.area = 0.5*(self.width+base2)*self.height

    
    def kite(self):
        self.area = 0.5*self.width*self.height

    
    #for file saving
    def packager(self):
        dict_format = {
            "Dimension":"2D",
            "Shape":self.shape,
            "Width":self.width,
            "Height":self.height,
            "Area":self.area,
            "Perimeter":self.perimeter
        }
        return dict_format
    


class Triangles:
    def __init__(self,base,height,shape):
        self.base = float(base)
        self.height = float(height)
        self.shape = shape
        self.area = None
        self.perimeter = None
        self.hypotenuse = None
    

    #Object Info
    def __str__(self):
        return f"Shape: {self.shape}\nArea: {self.area}units^2\nPerimeter: {self.perimeter}units\nBase:{self.base}units\nHeight: {self.height}units\nHypotenuse: {self.hypotenuse}units"

    #As the formula for areas for all triangles is 1/2b*h there is only going to be one function for area but the perimeters are going to be separate
    def find_area(self):
        self.area = 0.5*self.base*self.height

    #useful for modularity
    def find_hypotenuse(self):
        c_squared = (self.base**2)+(self.height**2)
        self.hypotenuse = math.sqrt(c_squared)


    def right(self):  
        self.perimeter =  self.base + self.height + self.hypotenuse
    

    def equilateral(self):
        self.perimeter = self.base*3
    

    def irregular(self):
        second = positivity(stupid_proofed_inputs("What is the second side length of the triangle?(not base)","number","_"))
        third = positivity(stupid_proofed_inputs("What is the third side length of the triangle?(not base)","number","_"))
        self.perimeter = third+self.base+second
    

    #for file saving
    def packager(self):
        dict_format = {
            "Dimension":"2D",
            "Shape":self.shape,
            "Width":self.base,
            "Height":self.height,
            "Area":self.area,
            "Perimeter":self.perimeter
        }
        return dict_format


#all regular polygons area's and perimeters can be calculated the same way so there is only need for one for each
class RegularPolygon:
    def __init__(self,apothem,sidelength,shape,sides):
        self.shape = shape
        self.apothem = float(apothem)
        self.sidelength = float(sidelength)
        self.sides = int(round(float(sides),0))
        self.area = None
        self.perimeter = None


    def __str__(self):
        return f"Shape: {self.shape}\nSides: {self.sides}\nArea: {self.area}units^2\nPerimeter: {self.perimeter}units\nApothem:{self.apothem}units\nSide Length: {self.sidelength}units"
    

    def find_perimeter(self):
        self.perimeter = self.sidelength*self.sides


    #!IMPORTANT! MAKE SURE THAT PERIMETER FUNCTION IS CALLED ON THE OBJECT BEFORE AREA
    def find_area(self):
        self.area = 0.5*self.apothem*self.perimeter
    

    #for file saving
    def packager(self):
        dict_format = {
            "Dimension":"2D",
            "Shape":self.shape,
            "Apothem":self.apothem,
            "Height":self.sidelength,
            "sides":self.sides,
            "Area":self.area,
            "Perimeter":self.perimeter
        }
        return dict_format


class Circles:
    def __init__(self,radius,shape):
        self.shape = shape
        self.radius = float(radius)
        self.area = None
        self.circumference = None
        self.diameter = float(radius)*2

    
    def __str__(self):
        return f"Shape: Circle\nRadius: {self.radius}\nDiameter: {self.diameter}\nArea: {self.area}\nCircumference: {self.circumference}"
    

    def find_circumference(self):
        self.circumference = self.diameter*math.pi
    

    def find_area(self):
        self.area = math.pi*(self.radius**2)

    
    #for file saving
    def packager(self):
        dict_format = {
            "Dimension":"2D",
            "Shape":self.shape,
            "Radius":self.radius,
            "Diameter":self.diameter,
            "Area":self.area,
            "Circumference":self.circumference
        }
        return dict_format
