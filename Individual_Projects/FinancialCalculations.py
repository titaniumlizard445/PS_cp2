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
    print(f"It will take {round_months} months to reach {goal} when paying {monthly_pay} per month.")

#Compound interest inputs(starting_balance, Interest, Time_in_years)
def CompoundInt(start_bal,Int,years):
    #for range(Time_in_years)
    total = start_bal
    Int/=100
    for x in range(years):
        #multiply starting balance with interest
        newstuff = total * Int
        total += newstuff
    #return total
    print(f"when you keep {start_bal} in the bank for {years} years with an interest rate of, you will have {total}$")

#Budget Allocationer inputs()
def Allocator(income):
    #options for allocation
    categories = ["Rent/Mortgage","Transportation","Groceries","Utilities","Savings","Investments"]
    
    print("\n\nCategories:\n1.Rent/Mortgage\n2.Transportation\n3.Groceries\n4.Utilities\n5.Savings\n6.Investments\n\n")
    #asks for percent to each category
    categoriesused = int(input("\nEnter number up to how many of these categories would you like to use: ").strip())
    
    #asks for percent of each category
    for x in range(categoriesused):
        #asks for each category's percent
        percent = ""
        percent = int(input(f"Enter in the percent for the {categories[x]} category here: ").strip())
        percent/=100
        some_money = percent * income
        print(f"{categories[x]}:{some_money}$")
    
#Sales Price Calculator inputs(original_price,discount)
def Saleprice(og_price,discount):
    #subtract original price from original price x discount
    disc_perc = discount/100
    new_price = og_price * disc_perc
    print(f"After a {discount}% discount applied to {og_price}$, the price becomes {new_price}$")

#Tip Calculator inputs(original_price,tip_percent)
def TipCalc(og_price,tip_perc):
    #multiply original price with tip percent and add that to original price
    added_price = og_price*tip_perc
    total = added_price+og_price
    print(f"When you give {tip_perc*100}% of {og_price}$ then your total price will be{total}$")

#User Interface 
def Main():
    #runs program and allows user to choose different stuff
    while True:
        print("Welcome to the Financial Calculator!\nPlease choose one of the following options:\n1)how long to save for a goal via monthly payments \n2)Compound Interest Calculator\n3)Budget Allocator\n4)Discount price Calculator\n5)Tip price Calculator")
        Choice = int(input("Enter the number next to the option you would like here: "))
        if Choice == 1:
            #MonthstoGoal
            #Tell user what they chose for comfirmation
            print("You have chosen: time until goal met calculator")
            goal = float(input("How much money would you like to save up? ").strip())
            pay = float(input("How much money will you pay per month? ").strip())
            MonthsToGoal(goal,pay)
        elif Choice == 2:
            #CompoundInterest
            #Tell user what they chose for comfirmation
            print("You have chosen: Compound Interest Calculator")
            start_balance = float(input("How much money will you start with? ").strip())
            interest_rate = float(input("What is the interest rate for the money? ").strip())
            years = int(input("How long will you keep the money in the bank? ").strip())
            CompoundInt(start_balance,interest_rate,years)
        elif Choice == 3:
            #BudgetAllocator
            #Tell user what they chose for comfirmation
            print("You have chosen: Budget Allocator")
            #asks for income and how many categories they would like to allocate to from preset categories
            income_ = float(input("Enter your monthly income: ").strip().lower())
            Allocator(income_)
        elif Choice == 4:
            #DiscountFinder
            #Tell user what they chose for comfirmation
            print("You have chosen: Discount Finder")
            #inputs
            original_price = float(input("What was the original price of the item? ").strip())
            discount = float(input("What is the discount percent? ").strip())
            Saleprice(original_price,discount)
        elif Choice == 5:
            #TipCalculator
            #Tell user what they chose for comfirmation
            print("You have chosen: Tip Calculator")
            #inputs
            original_price = float(input("What was the original price of the meal? ").strip())
            tip_percent = float(input("What is the percent you want to tip? ").strip())
            tip_percent/=100
            TipCalc(original_price,tip_percent)
        else:
            print("Invalid Choice, please enter the number of the choice you would like to use,")
        done = input("Are you done using the Financial Calculator (y/n)? ")
        if done == "y":
            break
        elif done == "n":
            print("continue calculating")
        else:
            print("Type in y for Yes or n for No")
    
Main()
