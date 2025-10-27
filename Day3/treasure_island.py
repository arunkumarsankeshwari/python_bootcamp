#The game is boring, I am going to keep it so for the reason that there's not much to learn langauge wise
#Skipping the ASCII ART as well
print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
left_right = input("Do you want to left or right?\n")
if left_right.lower() != "left":
    print("Game over!")
    exit()
swim_weight = input("Do you want swim or wait?\n")
if swim_weight.lower() != "wait":
    print("Game over!")
    exit()
door_color = input("There are 3 doors - Red, Yellow and Blue, Choose one..\n")
if door_color.lower() != "yellow":
    print("Game over!")
    exit()

print("You found the treasure, you win!!!")
