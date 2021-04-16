##The below is a finance caluclator. It will help the user calculate
##their investment or their bond
import math ##This imports the necessary math functions that will be needed in this program

calculator_choice = input("What would you like to calculate today? Investment or Bond?: ")
calculator_choice =  str.casefold(calculator_choice) ##casefold allows the for the input to be read no matter the case of the word that was entered.

##The below detirmines through if function what type of investment will be made.
##Gathers the necessary information from the user for that calculation.
if calculator_choice == "investment":
    investment_amount = input("How much money are you going to be depositing? ")
    investment_amount = int(investment_amount)
    investment_interest = input("How much interest are your planning on earning? ")
    investment_interest = int(investment_interest)/100
    investment_years = input("How many years are you planning on investing for? ")
    investment_years = int(investment_years)
    interest_type = input("What type of interest would you like to earn? Simple or compound? ")
    interest_type = str.casefold(interest_type)
    if interest_type == "simple":
        interest_earned = investment_amount* (1 + investment_interest * investment_years)
        print(interest_earned)
    elif interest_type == "compound":
        interest_earned = investment_amount * math.pow((1 + investment_interest), investment_years)
        print(f"The mount of interest that your will earn based on what you invested and the period will be R{interest_earned}")

##The below calculates that monthly cost if it was a bond investment and what the montly repayment
##would be.
if calculator_choice == "bond":
    investment_amount = input("How much money are you going to be depositing? ")
    investment_amount = int(investment_amount)
    investment_interest = input("How much is the interest? ")
    investment_interest = int(investment_interest)/100
    monthly_interest = investment_interest/12
    bond_length = input("How many months are you planning to take to repay the bond? ")
    bond_length = int(bond_length)
    monthly_repayment = (monthly_interest * investment_amount) / (1 - (1 + monthly_interest ** (- bond_length)))
    print(f"Your monthly repayment will be R{monthly_repayment} based on your investment amount, interest and length of the bond.")
    
##\\https://docs.python.org/3/library/stdtypes.html#str.casefold
##\\https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators#:~:text=0.0%20is%20returned.-,Power,multiplied%20by%20itself%203%20times