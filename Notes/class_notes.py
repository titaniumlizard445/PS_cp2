#PS 1st Classes Notes

#screwin' around #1
class DefaultClass:
    #!IMPORTANT!
    def __init__(self,name,age,is_cat):
        self.name = name
        self.age = age
        self.is_cat = is_cat
    
    def __str__(self):
        return f"Name: {self.name}\n Age: {self.age}\n Is Cat?: {self.is_cat}"
    
    def happy_birthday(self):
        self.age += 1


fred = DefaultClass("Fred",34,False)
silvia = DefaultClass("Silvia",5,True)
print(fred)
print(silvia)
silvia.happy_birthday()
print(silvia)
print()
class Shapes:
    def __init__(self,width,height,area,name):
        self.width = width
        self.height = height
        self.name = name
        self.area = area
    
    def __str__(self):
        return f"Name: {self.name}\nWidth:{self.width}px\nHeight:{self.height}px\nArea:{self.area}px"
    
Shape1 = Shapes(200,200,20000,"Equilateral Triangle")
Shape2 = Shapes(400,400,160000,"Large Square")
Shape3 = Shapes(100,100,10000,"Small Square")
Shape4 = Shapes(200,400,800,"Rectangle")

print(Shape1)
print(Shape2)
print(Shape3)
print(Shape4)