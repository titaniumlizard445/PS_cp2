#PS 1st Calculator for finances

#functions for each thing

#$ per month thing inputs(goal, months,weeks_or_months)
def MonthsToGoal(goal,monthly_pay):
    #divide goal by months and output $/per month
    def divide():
        months = goal/monthly_pay
        return months
    divide()
    round_months = round(divide())
    if round_months < divide():
        round_months+=1
    return print(f"It will take {round_months} montsh to reach {goal} when paying {monthly_pay} per month.")

#Compound interest inputs(starting_balance, Interest, Time_in_years)
def CompoundInt(start_bal,Int,years):
    #for range(Time_in_years)
    total = start_bal
    for x in range(years):
        #multiply starting balance with interest
        newstuff = total * Int
        total += newstuff
    #return total
    return print(f"when you keep {start_bal} in the bank for {years} years, you will have {total}$")

#Budget Allocationer inputs()
def Allocator():
    #options for allocation
    categories = ["Rent/Mortgage","Transportation","Groceries","Utilities","Savings","Investments"]
    #asks for income and how many categories they would like to allocate to from preset categories
    income = input("Enter your monthly income: ").strip().lower()
    
    print("\n\nCategories:\n1.Rent/Mortgage\n2.Transportation\n3.Groceries\n4.Utilities\n5.Savings\n6.Investments\n\n")
    #asks for percent to each category
    categoriesused = int(input("\nEnter number up to how many of these categories would you like to use: ").strip())
    
    #asks for percent of each category
    for x in categoriesused:
        #asks for each category's percent
        percent = ""
        while not percent.isnumeric():
            percent = input(f"Enter in the percent for the {x} category here: ").strip()
            if not percent.isnumeric():
                print(f"Enter in just a number no % sign")
        print(f"{categories[x]}:{percent}%")
    
#Sales Price Calculator inputs(original_price,discount)
def Saleprice(og_price,discount):
    #subtract original price from original price x discount
    disc_perc = discount/100
    new_price = og_price * disc_perc
    return print(f"After a {discount}% discount applied to {og_price}$, the price becomes {new_price}$")

#Tip Calculator inputs(original_price,tip_percent)
def Tipcalc(og_price,tip_perc):
    #multiply original price with tip percent and add that to original price
    added_price = og_price*tip_perc
    total = added_price+og_price
    return print(f"When you give {tip_perc}% of {og_price}$ then your total price will be{total}$")

#User Interface 
    #runs program and allows user to choose different stuff

