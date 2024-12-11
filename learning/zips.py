# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_dates = ["1/1/2021","1/2/2021","1/3/2021"]

#EXAMPLE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# users = zip(usernames,passwords)
users = list(zip(usernames,passwords))

for i in users:
    print(i)


#EXAMPLE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
users = dict(zip(usernames, passwords))

print(type(users))

for key,value in users.items():
    print(key+" : "+value)

#EXAMPLE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
users = zip(usernames, passwords,login_dates)

for i in users:
    print(i)

######################################### zip in python############################################



# Zip Practice #1
# Print to the screen phrases like the following example:

# "The capital of Germany is Berlin"

# Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

nations = dict(zip(capitals,countries))

print(type(nations))

for key,value in nations.items():
    print("The capital of " +value+ " is " +key+ ".")

# Zip Practice #2
# Create a zip object made up of lists, of a set of brands and products that you prefer, inside the my_zip variable.
brands = ["Kodak","McDonald's","Nike","Apple","Cape Cod" ]
products = ["Camera","Fries","Shoes","MacBook","Chips"]

my_zip = list(zip(brands, products))

print(my_zip)

# Zip Practice #3
# Create a zip object with the translations of the numbers from 1 to 5 in Spanish, Portuguese and English (in that same order), and then convert the generated object into a list called numbers:

# one / um / one

# two / two / two

# three / three / three

# four / four / four

# five / five / five

# The result should follow the structure:

# [('one', 'um', 'one'), ('two', 'dois', 'two'), ... ]

# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five

english = ['one','two','three','four','five']
spanish = ['uno','dos','tres','cuatro','cinco']
portuguese = ['um','dois','três','quatro','cinco']

numbers_lang = list(zip(english, spanish, portuguese))

print(numbers_lang)

#######################zip function challenge#####################
# Challenge: Create a list of countries and their capitals, then zip them together and print
# each country with its capital.

# Two lists: countries and capitals


# Use zip to pair countries with their capitals

capitals = ['Cairo', 'Buenos Aires', 'Bangkok', 'Abuja', 'Stockholm']
countries = ['Egypt', 'Argentina', 'Thailand', 'Nigeria', 'Sweden']


nations = dict(zip(capitals,countries))

print(type(nations))

for key,value in nations.items():
    print("The capital of " +value+ " is " +key+ ".")