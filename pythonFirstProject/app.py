print("Hello World")

# execute code line by line

# separate with underscore when creating a variable
character_name = "John"
character_age = "50"
# use capital letter
is_male = True
print("Hi my name is " + character_name + " and I am " + character_age + " years old.")

# variables can be re-assigned
character_name = "Mike"
print("Hi my name is " + character_name + " and I am " + character_age + " years old.")

# change sentence
print("Hello\nWorld")
# add " inside the sentence
print("Hello\"World")

# make sentence upper case and check is it is upper case
text = "Hello World"
print(text.upper().isupper())

# count characters
print(len(text))

# return the index of the character
print(text.index("H"))

# replace words
print(text.replace("Hello", "Hey"))

# convert number to string. make sure number and string can not be combined
my_num = -5
print(str(my_num))

# return absolute number
print(abs(my_num))

# return exponentiation number
print(pow(4, 2))

# return bigger number
print(max(4, 2))

# return smaller number
print(min(4, 2))

# return rounded number
print(round(3.7))

# import math function. allows us a lot of things related math by importing this
from math import *
print(floor(3.7))
print(ceil(3.7))
print(sqrt(37))

# create input and save it to name variable
name = input("Enter your name: ")
print("Hello " + name + "!")


