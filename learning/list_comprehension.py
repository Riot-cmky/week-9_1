# list comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition] - follow this formula

# Version 1
doubles = []
for x in range(1, 11):
    doubles.append(x*2)

print(doubles)

# Version 2.1
doubles = [x*2 for x in range(1, 11)]

print(doubles)

# Version 2.2
triples = [y*3 for y in range(1, 11)]

print(triples)

# Version 2.3
squares = [z*z for z in range(1, 11)]

print(squares)

# ~~~~~~~~FRUITS EXAMPLE~~~~~~~~~~~~

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)


fruits = ["apple", "orange", "banana", "coconut"]
fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)

# ~~~~~~~~NUMBERS EXAMPLE~~~~~~~~~~~~

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

# ~~~~~~~~NUMBERS EXAMPLE~~~~~~~~~~~~

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)

################################################List comprehension###############################################
# List Comprehensions Practice #1
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create a square_values list consisting of the numbers in the values list, squared.

values = [1, 2, 3, 4, 5, 6, 9.5]
square_values = [x**2 for x in values]
print(square_values)

#OR

values = [1, 2, 3, 4, 5, 6, 9.5]
square_values = []

for x in values:
    square_values.append(x**2)

print(square_values)


# List Comprehensions Practice #2
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

values = [1, 2, 3, 4, 5, 6, 9.5]
even_values = [x for x in values if isinstance(x, int) and x % 2 == 0]
print(even_values)

#OR

values = [1, 2, 3, 4, 5, 6, 9.5]
even_values = []

for x in values:
    if isinstance(x, int) and x % 2 == 0:
        even_values.append(x)

print(even_values)

# List Comprehensions Practice #3
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius. The conversion between type of units is as follows:

# °C = (°F - 32) * (5/9)

# or expressed in another way:

# (degrees_fahrenheit-32)*(5/9)

# The list of temperatures is as follows:

# temperature_fahrenheit = [32, 212, 275]

# Store this new list in a variable called degrees_celsius

temperature_fahrenheit = [32, 212, 275]
degrees_celsius = [(f - 32) * (5/9) for f in temperature_fahrenheit]
print(degrees_celsius)

#OR

temperature_fahrenheit = [32, 212, 275]
degrees_celsius = []

for f in temperature_fahrenheit:
    celsius = (f - 32) * (5/9)
    degrees_celsius.append(celsius)

print(degrees_celsius)