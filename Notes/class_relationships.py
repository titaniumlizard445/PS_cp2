# Class Relationships Notes

#Inheritance "is a"
#Parent Class
class Vehicle:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

    
    def move(self):
        print("MOOOOOOOOOOOOOOVE!")
    

#Child Class
class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("SAIL")


class Plane(Vehicle):
    def move(self):
        print("FLY!!!!")

car = Car("Ford", "Mustang")
boat = Boat("Visa","journey 6000")
plane = Plane("Lockheed Martin", "A-12")

car.move()
boat.move()
plane.move()



#Aggregation  "has a"
class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog
    

    def add_book(self,book):
        self.catalog.append(book)
    

    def remove_book(self,book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("Book not in library")
    
    def view_catalog(self):
        for book in self.catalog:
            print(book)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    
    def __str__(self):
        return f"{self.title} by {self.author}"
    

librar = Library("Provo Library")

librar.add_book(Book("Return of the King", "J.R.R. Tolkien"))
librar.add_book(Book("Fellowship of the Ring", "J.R.R. Tolkien"))
librar.add_book(Book("SteelHeart", "Brandon Sanderson"))
librar.view_catalog()
