print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
try:
    bill = float(bill)
except:
    print("Entered amount is invalid, please try again!")
    exit()
tip = input("How much tip would you like to give? 10, 12, or 15? ")
try:
    tip = int(tip)
except:
    print("Entered tip percentage should be a number, please try again!")
    exit()
if tip != 10 and tip != 12 and tip != 15:
    print("The tip percentage should be from the standard available options of 10, 12 and 15. Please try again!")
    exit()
people = input("How many people to split the bill?")
try: 
    people = int(people)
except:
    print("People input should be a number. Please try again!")
    exit()
cost_per_person = (bill * (1 + (tip/100))) / people
print(f"Each person should pay: %{round(cost_per_person,2)}") 

