
#Comparison operators
# Logical operators
# Decision making
# loops(for loops, while loops, range, enumerator)
# min/max practice
# Random in python
# List comprehension


# review practice
# Append the value of current to the end of the list seconds Please use the list.append() method to do that.


seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)

print(seconds)

# Remove item 1.45 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)
print(seconds)

# Remove items 1.45, 1.02, and 1.11 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)
seconds.remove(1.02)
seconds.remove(1.11)
print(seconds)


################################comparison operators#########################
#remember....
# > greater
# < less
# >= greater or equal
# <= less or equal
# == equal
# != different or not equal to




# Comparison Operators Practice  1:
# Create two variables (num1 and num2) with the following values: 36 and 17. Check if num1 is greater than or equal to num2 and store the result of that comparison in a variable called my_bool
num1 = [36, 17]
num2 = [36, 17]
my_bool_1 = num1 >= num2
print(my_bool_1)


# Comparison Operators Practice  2:
# Create two variables (num1 and num2):
# Inside num1, store the result of the square root of 25
# Inside num2, store the number 5.
# Check if num1 is equal to num2 and store the result of that comparison in a variable called my_bool.
import math

num1 = math.sqrt(5)
num2 = [5]
my_bool_2 = num1 == num2
print(my_bool_2)

# Comparison Operators Practice #3:
# Create two variables (num1 and num2):

# Inside num1, store the result of 64 x 3
num1 = [64*3]
# Inside num2, store the result of 24 x 8
num2 = [24*8]
# Check if num1 is different from num2 and store the result of that comparison in a variable called my_bool.
my_bool_3 = num1 != num2
print(my_bool_3)


#######################comparison operators challenge#####################
# Challenge: Compare two numbers entered by the user and check if they are equal or not.
# If they are not equal, print which one is greater.

# Prompt the user for two numbers
numK = int(input('Enter a number: '))
numD = int(input('Enter a number: '))
# Check for equality and greater number

if numK == numD:
    print('Equal')
elif numK > numD:
    print('numK is Greater')
elif numD > numK:
    print('numD is Greater')
else:
    print('Lesser')