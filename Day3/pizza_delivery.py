#prices
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_medidum_large = 3
extra_cheese = 1

print("Welcome to Python pizza Deliveries!")
pizza_size = input("What size pizza do you want? S, M or L: ")
option_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
option_extra_cheese = input("Do you want extra cheese? Y or N: ")

#basic input validation
if pizza_size != "S" and pizza_size!= "M" and pizza_size != "L":
    print("Entered pizza size is not valid, please try again!")
    exit()
if option_pepperoni != "Y" and option_pepperoni != "N":
    print("Entered option for pepperoni is not valid, please try again!")
    exit()
if option_extra_cheese != "Y" and option_extra_cheese != "N":
    print("Entered option for extra cheese is not valid, please try again!")
    exit()

toppings = 0
if option_pepperoni == "Y":
    if pizza_size == "S":
        toppings += pepperoni_small
    else:
        toppings += pepperoni_medidum_large

if option_extra_cheese == "Y":
    toppings += extra_cheese

pizza_price = 0
if pizza_size == "S":
    pizza_price = small_pizza
elif pizza_size == "M":
    pizza_price = medium_pizza
else:
    pizza_price = large_pizza

print(f"Your final bill is: ${pizza_price + toppings}")

