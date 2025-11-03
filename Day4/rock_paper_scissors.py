import random
#rock - 0
#paper - 1
#scissor - 2

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
def get_art(choice:int):
    if choice == 0:
        return rock
    elif choice == 1:
        return paper
    else: 
        return scissors
selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

if selection < 0 or selection > 2:
    print("Invalid choice, please try again!")
    exit()

computer_selection = random.choice([0,1,2])

print(get_art(selection))

print(f"Computer chose:\n{get_art(computer_selection)}")

if selection == computer_selection:
    print("Draw, please try again!")
    exit()

if selection == 0 and computer_selection == 1:
    print("You lose!")
elif selection == 0 and computer_selection == 2:
    print("You win!")
elif selection == 1 and computer_selection == 0:
    print("You win!")
elif selection == 1 and computer_selection == 2:
    print("You lose!")
elif selection == 2 and computer_selection == 0:
    print("You lose!")
elif selection == 2 and computer_selection == 1:
    print("You win!")






