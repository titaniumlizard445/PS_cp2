#PS 1st this contains the UI for the sub menus
from Stupid_proofing import *
from files.json_manager import *
from Second_Dimensional_Calculations import *
from Third_Dimensional_Calculations import *

#2D Shape Menu
@decorator
def second_dimension():
    
    #inner function for showing user all shapes
    def view_shapes(sorting=None):
        shapes = JSON_reader()
        
        #separating 2D shapes from 3D shapes
        two_D_shapes = []
        for x in shapes.keys():
            if "2D" in shapes[x]["Dimension"]:
                two_D_shapes[x] = shapes[x]
        
        if sorting == None:
            #dictionary cleaner upper
            for name,info in shapes.items():
                print(f"\nShape name: {name}")

                for info_key,info_value in info.items():
                    print(f"{info_key}: {info_value}")
            return shapes
        else:
            for name,info in sorting.items():
                print(f"\nShape name: {name}")

                for info_key,info_value in info.items():
                    print(f"{info_key}: {info_value}")
    

    print("----2D MODE SELECTED----\n (small warning: keep the units the same if you plan to compare shapes)\nActions:\n1.Create New Shape\n2.View Shapes\n3.Compare Shapes\n4.Sort\n5.Leave")
    choice = stupid_proofed_inputs("Enter here: ","number","1","2","3","4","5")
    match choice:
        #Create new shape
        case "1":
            print("\n\n----CREATE NEW SHAPE----\n\n")
            new_shape_choice = stupid_proofed_inputs("What Type of Shape would you like to create?\n1.Quadrialateral (any four sided shape)\n2.Triangle\n3.Regular Polygon (any shape that has equal side lengths and interior angles)\n4.Circle\nEnter here: ","number","1","2","3","4")
            match new_shape_choice:
                case "1":
                    print("\n\nQuadrilateral Mode Selected\n\n")
                    #get info
                    quad_name = stupid_proofed_inputs("What would you like to name your shape? (suggestion example: Billy the Square)\nEnter here: ","title","_")
                    quad_width = positivity(stupid_proofed_inputs(f"How wide is {quad_name}'s base?(Enter a positive number)\nEnter here: ","number","_"))
                    quad_height = positivity(stupid_proofed_inputs(f"How tall is {quad_name}?(Enter a positive number)\nEnter here: ","number","_"))
                    
                    #create object
                    new_quad = Quadrilaterals(quad_width,quad_height,quad_name)
                    
                    #change specifications of certain parts of the object
                    new_quad.find_perimeter()
                    special_area_check = stupid_proofed_inputs("Is your shape a kite or trapezoid?(no, kite or trapezoid)\nEnter here: ","lower","no","kite","trapezoid")
                    
                    if special_area_check == "no":
                        new_quad.normal_area()
                    
                    elif special_area_check == "trapezoid":
                        new_quad.trapezoid()
                    
                    elif special_area_check == "kite":
                        new_quad.kite()
                    
                    #save and display object
                    JSON_writer(new_quad.packager())
                    print(new_quad)

                case "2":
                    print("\n\nTriangle Mode Selected\n\n")
                    #get info
                    tri_name = stupid_proofed_inputs("What would you like to name your shape? (suggestion example: Billy the Square)\nEnter here: ","title","_")
                    tri_base = positivity(stupid_proofed_inputs(f"How wide is {tri_name}?(Enter a positive number)\nEnter here: ","number","_"))
                    tri_height = positivity(stupid_proofed_inputs(f"How tall is {tri_name}?(Enter a positive number)\nEnter here: ","number","_"))
                    triangle_type = stupid_proofed_inputs(f"What type of triangle is {tri_name} ?(Equilateral,Right,Irregular)\nEnter here: ","lower","equilateral","right","irregular")
                    #create object
                    new_tri = Triangles(tri_base,tri_height,tri_name)
                    
                    #change specifications of certain parts of the object
                    if triangle_type == "right":
                        new_tri.find_hypotenuse()
                        new_tri.right()
                    
                    elif triangle_type == "equilateral":
                        new_tri.equilateral()
                    
                    elif triangle_type == "irregular":
                        new_tri.irregular()
                    
                    new_tri.find_area()
                    new_tri.perimeter()
                    
                    #save and display object
                    JSON_writer(new_tri.packager())
                    print(new_tri)

                case "3":
                    print("\n\nRegular Polygon mode selected\n\n")
                    #get info
                    poly_name = stupid_proofed_inputs("What would you like to name your shape? (suggestion example: Billy the Square)\nEnter here: ","title","_")
                    poly_apothem = positivity(stupid_proofed_inputs(f"What is the apothem for {poly_name}?(Enter a positive number)\nEnter here: ","number","_"))
                    poly_side_length = positivity(stupid_proofed_inputs(f"What is the side length for {poly_name}?(Enter a positive number)\nEnter here: ","number","_"))
                    poly_sides = positivity(stupid_proofed_inputs(f"How many sides does {poly_name} have?(Enter a positive number)\nEnter here: ","number","_"))
                    #create object
                    new_poly = RegularPolygon(poly_apothem,poly_side_length,poly_name,poly_sides)
                    
                    #change specifications of certain parts of the object
                    new_poly.find_perimeter()
                    new_poly.find_area()
                    
                    #save and display object
                    JSON_writer(new_poly.packager())
                    print(new_poly)

                case "4":
                    print("\n\nCircle Mode Selected\n\n")
                    #get info
                    circ_name = stupid_proofed_inputs("What would you like to name your shape? (suggestion example: Billy the Square)\nEnter here: ","title","_")
                    circ_radius = positivity(stupid_proofed_inputs(f"What is the radius of {circ_name}?(Enter a positive number)\nEnter here: ","number","_"))
                    
                    #create object
                    new_circ = Circles(circ_radius,circ_name)
                    
                    #change specifications of certain parts of the object
                    new_circ.find_area()
                    new_circ.find_circumference()
                    
                    #save and display object
                    JSON_writer(new_circ.packager())
                    print(new_circ)

        #view all shapes choice
        case "2":
            print("\n\n----VIEW ALL SHAPES----\n\n")
            view_shapes()

        #compare all shapes mode
        case "3":
            print("\n\n----COMPARE SHAPES----\n\n")
            
            #display all shapes
            shape_data = view_shapes()
            
            #making sure that the shape the user chooses exists
            shape1 = None
            while shape1 not in shape_data:
                shape1 = stupid_proofed_inputs("Select the first shape for comparison\nEnter here: ","title","_")

            #making sure that the second shape the user chooses exists
            shape2 = None
            while shape2 not in shape_data:
                shape2 = stupid_proofed_inputs("Select the second shape for comparison\nEnter here: ","title","_")
            print("\n\n")
            
            #checking if the shape is a circle
        
            if "Perimeter" in shape_data[shape1]:
                per_or_circum1 = "Perimeter"
            else:
                per_or_circum1 = "Circumference"
            
            if "Perimeter" in shape_data[shape2]:
                per_or_circum2 = "Perimeter"
            else:
                per_or_circum2 = "Circumference"

            #comparisons for Area
            if shape_data[shape1]["Area"] > shape_data[shape2]["Area"]:
                print(f"{shape1}'s Area is larger than {shape2}'s Area by: {shape_data[shape1]["Area"]-shape_data[shape2]["Area"]}units^2")
            elif shape_data[shape1]["Area"] < shape_data[shape2]["Area"]:
                print(f"{shape2}'s Area is larger than {shape1}'s Area by: {shape_data[shape2]["Area"]-shape_data[shape1]["Area"]}units^2")
            else:
                print(f"Shapes Areas are equal. Area:{shape_data[shape1]["Area"]}")
            
            #comparisons for Perimeter
            if shape_data[shape1][per_or_circum1] > shape_data[shape2][per_or_circum2]:
                print(f"{shape1}'s Perimeter is larger than {shape2}'s Perimeter by: {shape_data[shape1][per_or_circum1]-shape_data[shape2][per_or_circum2]}units^2")
            elif shape_data[shape1][per_or_circum1] < shape_data[shape2][per_or_circum2]:
                print(f"{shape2}'s Perimeter is larger than {shape1}'s Area by: {shape_data[shape2][per_or_circum2]-shape_data[shape1][per_or_circum1]}units^2")
            else:
                print(f"Shapes Perimeters are equal. Perimeter:{shape_data[shape1][per_or_circum1]}")
            print("\n\n")

        case "4":
            print("----Sorting Selected----")
            mode = stupid_proofed_inputs("\n\nWhat criteria would you like to sort by?(perimeter or area)\nEnter here: ","lower","perimeter","area")
            
            shape_data = JSON_reader()
            shape_names = shape_data.keys()
            if mode == "perimeter":
                perimeters = []
                
                for x in shape_names:

                    if "Perimeter" in shape_data[x]:
                        per_or_circum = "Perimeter"
                    else:
                        per_or_circum = "Circumference"
            
                    perimeters.append(shape_data[x][per_or_circum])
                perimeters.sort(reverse=True)
                ordered_dicts = {}
                for shape_per in perimeters:
                    for x in shape_names:
                        if "Perimeter" in shape_data[x]:
                            per_or_circum = "Perimeter"
                        else:
                            per_or_circum = "Circumference"
                        if shape_data[x][per_or_circum] == shape_per:
                            ordered_dicts[x] = shape_data[x]
                            break    
                    
            #simple sorting for areas -similar system for perimeters but making sure that circumferences are included with perimeters
            elif mode == "area":
                areas = []

                #gets all the areas into a separate list
                for x in shape_names:
                    areas.append(shape_data[x]["Area"])
                
                #sorts areas
                areas.sort(reverse=True)
                ordered_dicts = {}
                
                #assigns all the sorted areas back to their original shapes and orders those
                for shape_area in areas:
                    for x in shape_names:
                        if shape_data[x]["Area"] == shape_area:
                            ordered_dicts[x] = shape_data[x]
                            break
                
            else:
                print("Error in sorting selection")
                ordered_dicts = "An Error occured"
            
            print("\n----Sorted Shapes----\n")
            view_shapes(ordered_dicts)

        case "5":
            return



#3D Shape Menu
@decorator
def third_dimension():
    print("\n\n----3D MODE SELECTED----\n")
    print("\nWarning Units are not saved so you have to keep track of them!\nActions:\n1.Create New Shape\n2.View Shapes\n3.Compare Shapes\n4.Leave\n\n")
    choice = stupid_proofed_inputs("Enter here: ","number","1","2","3","4")

    match choice:
        case "1":
            print("\n\n----CREATE NEW SHAPE----\n\n")
            shape_choice = stupid_proofed_inputs("Which shape would you like to create? (Cube, Sphere,Cone or Rectangular Prism(Prism))\nEnter here:","lower","cube","sphere","cone","prism","rectangular prism")
            shape_name = stupid_proofed_inputs("What would you like to name your shape? (suggestion example: Billy the Square)\nEnter here: ","title","_")
            
            match shape_choice:
                case "cube":
                    side_length = positivity(stupid_proofed_inputs(f"What is the length of one of the sides of {shape_name}\nEnter here: ","number","_"))
                    
                    #create object
                    new_shape = Cube(side_length,shape_name)
                    new_shape.find_surface()
                    new_shape.find_volume()

                    #save
                    JSON_writer(new_shape.packager())

                case "cone":
                    radius = positivity(stupid_proofed_inputs(f"What is the Radius of {shape_name}?\nEnter here: ","number","_"))
                    height = positivity(stupid_proofed_inputs(f"What is the Height of {shape_name}?\nEnter here: ","number","_"))
                    
                    #create object
                    new_shape = Cone(radius,height,shape_name)
                    new_shape.find_slant()
                    new_shape.find_surface()
                    new_shape.find_volume()

                    #save
                    JSON_writer(new_shape.packager())

                case "sphere":
                    radius = positivity(stupid_proofed_inputs(f"What is the Radius of {shape_name}?\nEnter here: ","number","_"))

                    #create object
                    new_shape = Sphere(radius,shape_name)
                    new_shape.find_surface()
                    new_shape.find_volume()

                    #save
                    JSON_writer(new_shape.packager())

                case "rectangular prism" | "prism":
                    side1 = positivity(stupid_proofed_inputs(f"What is the length of the first side of {shape_name}?\nEnter here: ","number","_"))
                    side2 = positivity(stupid_proofed_inputs(f"What is the length of the second side of {shape_name}?\nEnter here: ","number","_"))
                    side3 = positivity(stupid_proofed_inputs(f"What is the length of the third side of {shape_name}?\nEnter here: ","number","_"))

                    #create object
                    new_shape = RectangularPrism(shape_name,side1,side2,side3)
                    new_shape.find_surface()
                    new_shape.find_volume()
                    
                    #save
                    JSON_writer(new_shape.packager())

        case "2":
            print("\n\n----VIEW SHAPES----\n\n")
            
            shapes = JSON_reader()
            for x in list(shapes.keys()):
                if shapes[x]["Dimension"] != "3D":
                    shapes.pop(x)
                    
            
            for name,info in shapes.items():
                print(f"\n\nShape Name: {name}")
                for key_info,data_info in info.items():
                    print(f"{key_info}:{data_info}")
            
        case "3":
            print("\n\n----COMPARE SHAPES----\n\n")
            
            shapes = JSON_reader()
            for x in list(shapes.keys()):
                if shapes[x]["Dimension"] != "3D":
                    shapes.pop(x)
                    
            
            for name,info in shapes.items():
                print(f"\n\nShape Name: {name}")
                for key_info,data_info in info.items():
                    print(f"{key_info}:{data_info}")

            shape_data = JSON_reader()
            
            #making sure that the shape the user chooses exists
            shape1 = None
            while shape1 not in shape_data:
                shape1 = stupid_proofed_inputs("Select the first shape for comparison\nEnter here: ","title","_")

            #making sure that the second shape the user chooses exists
            shape2 = None
            while shape2 not in shape_data:
                shape2 = stupid_proofed_inputs("Select the second shape for comparison\nEnter here: ","title","_")
            print("\n\n")

            #comparisons for surface area
            if shape_data[shape1]["Surface area"] > shape_data[shape2]["Surface area"]:
                print(f"{shape1}'s Surface Area is larger than {shape2}'s Area by: {shape_data[shape1]["Surface area"]-shape_data[shape2]["Surface area"]}units^2")
            elif shape_data[shape1]["Surface area"] < shape_data[shape2]["Surface area"]:
                print(f"{shape2}'s Surface Area is larger than {shape1}'s Area by: {shape_data[shape2]["Surface area"]-shape_data[shape1]["Surface area"]}units^2")
            else:
                print(f"Shapes Surface Areas are equal. Area:{shape_data[shape1]["Surface area"]}")
            
            #comparisons for Perimeter
            if shape_data[shape1]["Volume"] > shape_data[shape2]["Volume"]:
                print(f"{shape1}'s Volume is larger than {shape2}'s Volume by: {shape_data[shape1]["Volume"]-shape_data[shape2]["Volume"]}units^3")
            elif shape_data[shape1]["Volume"] < shape_data[shape2]["Volume"]:
                print(f"{shape2}'s Volume is larger than {shape1}'s Volume by: {shape_data[shape2]["Volume"]-shape_data[shape1]["Volume"]}units^3")
            else:
                print(f"Shapes Volumes are equal. Volume:{shape_data[shape1]["Volume"]}units^3")
            print("\n\n")
        case "4":
            return
