################################################random in python#################################################
# Random Practice #1
# Implement the randint() function from the random library that allows you to obtain an integer from 1 to 10, and store that value in a variable called random_number.

import random

random_number = random.randint(1, 10)
print(random_number)

# Random Practice #2
# Implement the random() function from the random library to obtain a real number between 0 and 1, and store that value in a variable called random_number.

import random

random_number = random.random()
print(random_number)

# Random Practice #3
# Use the random library's choice() method to get a random item from the list of names below, and store the chosen name in a variable called raffle.

import random

names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]
raffle = random.choice(names)
print(raffle)