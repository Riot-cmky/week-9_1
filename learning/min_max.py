

#################################################min/max######################################

# Min & Max Practice #1
# Get the maximum value among the values in the following list, and store it in a variable named maximum_value:

# number_list = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

number_list = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
maximum_value = max(number_list)
print(maximum_value)


# Min & Max Practice #2
# Calculate the difference between the maximum and minimum value in the following list of numbers, and store it in a variable called number_range:

# number_list = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

number_list = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665] 
number_range = max(number_list) - min(number_list) 
print(number_range)

# Min & Max Practice #3
# Using max(), min(), and dictionary methods, get the minimum value from the following dictionary:

# dictionary_ages = {"Tony":55, "Paulie":42, "Meadow":78, "Vito":44, "Ralph":24, "Sarah":35, "Evan":19, "Jean":2 ,"Ned":49}

# Store this value in a variable called minimum_age.

# Also, get the name that comes last in alphabetical order, and store it in a variable called last_name.

dictionary_ages = {"Tony":55, "Paulie":42, "Meadow":78, "Vito":44, "Ralph":24, "Sarah":35, "Evan":19, "Jean":2, "Ned":49}

minimum_age = min(dictionary_ages.values())
last_name = max(dictionary_ages.keys())

print(minimum_age)  # Minimum value from the dictionary
print(last_name)    # Last name alphabetically




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