#3D shape stuff goes here

import math

#shapes wanted: cube, sphere, cone, rectangular prism

class Cube:
    
    def __init__(self,side_length,shape):
        self.side_length = float(side_length)
        self.shape = shape
        self.volume = None
        self.surface_area = None
    

    def find_volume(self):
        self.volume = self.side_length**3
    

    def find_surface(self):
        self.surface_area = (self.side_length**2)*6


    def packager(self):
        dict_format = {
            "Dimension":"3D",
            "Shape":self.shape,
            "Side Length":self.side_length,
            "Volume":self.volume,
            "Surface area":self.surface_area
        }
        return dict_format



class Sphere:

    def __init__(self,radius,shape):
        self.radius = float(radius)
        self.shape = shape
        self.volume = None
        self.surface_area = None
    

    def find_volume(self):
        self.volume = (4/3)*math.pi*(self.radius**3)


    def find_surface(self):
        self.surface_area = 4*math.pi*(self.radius**2)


    def packager(self):
        dict_format = {
            "Dimension":"3D",
            "Shape":self.shape,
            "Radius":self.radius,
            "Volume":self.volume,
            "Surface area":self.surface_area
        }
        return dict_format
    


class Cone:

    def __init__(self,radius,height,shape):
        self.radius = float(radius)
        self.height = float(height)
        self.shape = shape
        self.volume = None
        self.surface_area = None
        self.slant = None
    

    def find_volume(self):
        self.volume = (1/3)*math.pi*(self.radius**2)*self.height
    

    def find_slant(self):
        self.slant = math.sqrt((self.radius**2)+(self.height**2))


    #!IMPORTANT! FIND SLANT HEIGHT FIRST
    def find_surface(self):
        self.surface_area = math.pi*self.radius*(self.slant+self.radius)


    def packager(self):
        dict_format = {
            "Dimension":"3D",
            "Shape":self.shape,
            "Radius":self.radius,
            "Height":self.height,
            "Slant Height":self.slant,
            "Volume":self.volume,
            "Surface area":self.surface_area
        }
        return dict_format



class RectangularPrism:
    
    #d stands for Dimension
    def __init__(self,shape,first_d,second_d,third_d):
        self.shape = shape
        self.first = float(first_d)
        self.second = float(second_d)
        self.third = float(third_d)
        self.surface_area = None
        self.volume = None


    def find_volume(self):
        self.volume = self.first*self.second*self.third
    

    def find_surface(self):
        self.surface_area = ((self.first*self.second)*2)+((self.first*self.third)*2)+((self.second*self.third)*2)
    

    def packager(self):
        dict_format = {
            "Dimension":"3D",
            "Shape":self.shape,
            "First Side":self.first,
            "Second Side":self.second,
            "Third Side":self.third,
            "Volume":self.volume,
            "Surface area":self.surface_area
        }
        return dict_format
