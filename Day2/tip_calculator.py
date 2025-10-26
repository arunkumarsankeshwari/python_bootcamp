print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

if tip != 10 and tip != 12 and tip != 15:
    print("The tip percentage should be from the standard available options of 10, 12 and 15. Please try again!")
    exit()
people = int(input("How many people to split the bill?"))

cost_per_person = (bill * (1 + (tip/100))) / people
print(f"Each person should pay: %{round(cost_per_person,2)}") 

