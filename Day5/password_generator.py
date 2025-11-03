import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', \
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','#','$','%','&','(',')','*','+']


len_letters = int(input("How many letters would you like in your password?\n"))
len_symbols = int(input("How many symbols would you like?\n"))
len_numbers = int(input("How many numbers would you like?\n"))

password = ""
for idx in range(0,len_letters):
    random_idx = random.randint(0,51)
    password += letters[random_idx]

for idx in range(0,len_symbols):
    random_idx = random.randint(0,8)
    password += symbols[random_idx]

for idx in range(0,len_numbers):
    random_idx = random.randint(0,9)
    password += str(numbers[random_idx])

shuffled_password = ''
processed_indices = []
while len(shuffled_password) != len(password):
    index = random.randint(0, len(password) - 1)
    if index not in processed_indices:
        processed_indices.append(index)
        shuffled_password += password[index]


print(f"Here is your password: {shuffled_password}")

