# password generator

import random
import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password_list = []

# rand_letters = random.sample(letters, nr_letters)
# password_list.append(rand_letters)

# rand_symbols = random.sample(symbols, nr_symbols)
# password_list.append(rand_symbols)

# rand_numbers = random.sample(numbers, nr_numbers)
# password_list.append(rand_numbers)

# print(password_list)

# password = ''
# for char in password_list:
#     for lists in char:
#         password += lists
# print(f"Your password is: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Hard Level
password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

# farai mutukumira
