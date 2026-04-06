from files.file_management import *
import pandas as panda
import matplotlib as plotting
import matplotlib.pyplot as piechart


def data_ui():
    print("Put explanation of what program does here")


#Charts: Pie for Class Distribution, Radar for Stats, Bar for Damage per ability

#Statistical Analyzer Chops up data into bites for DataVis
class StatisticalAnalyzer:
    def __init__(self,character_name):
        self.char_name = character_name
        self.char_info = JSON_reader()

    def class_distribution(self):        
        classes_created = []
        for x in self.char_info.keys():
            classes_created.append(self.char_info[x]["Class"])
        
        number_of_c = []
        number_of_c.append(classes_created.count("Well Rounded"))
        number_of_c.append(classes_created.count("Archer"))
        number_of_c.append(classes_created.count("Warrior"))
        number_of_c.append(classes_created.count("Mage"))
        number_of_c.append(classes_created.count("Engineer"))

        return number_of_c


    def stats(self):
        char_stats = self.char_info[self.char_name]["Stats"]
        info = panda.DataFrame(char_stats)
        return info


    def power_of_ability(self):
        abilities = self.char_info[self.char_name]["Abilities"]
        abil_names = abilities.keys()
        abil_damages = []
        
        for x in abil_names:
            abil_damages.append(abilities[x]["Damage"])
        
        info = {
            "Damages":abil_damages,
            "Names":abil_names
        }

        frame = panda.DataFrame(info)

        return frame




class DataVis(StatisticalAnalyzer):
    def __init__(self):
        pass

    def pie(self):
        piechart.pie(self.class_distribution(),labels=["Well Rounded","Archer","Warrior","Mage","Engineer"])
        piechart.title("Distribution of Classes")
        piechart.show()
        

    def radar(self):
        pass

    def bar(self):
        pass
