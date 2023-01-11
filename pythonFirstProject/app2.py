"""
List
"""

# grab last list elements
friends = ["kevin", "karen", "Jim", "Cupcake", "Cupcake"]
print(friends[-1])

# grab all list elements after 1
print(friends[2:])

# grab selected items
print(friends[1:3])

# extend -> append list
fav_food = ["donut", "bread", "icecream"]
friends.extend(fav_food)
print(friends)

# append -> append an individual list
friends.append("Jane")
print(friends)

# insert -> insert value to the list of specific index
friends.insert(1, "Yumi")
print(friends)

# remove -> remove value
friends.remove("Yumi")
print(friends)

# remove the last element of the list
friends.pop()
print(friends)

# find the index of the element
print(friends.index("Cupcake"))

# count how many times the element appeared
print(friends.count("Cupcake"))

# clear -> clear all values in the list
friends.clear()
print(friends)

# sort elements
friends.sort()

# reverse elements
friends.reverse()

# create a copy of the list
friends2 = friends.copy()

"""
Tuple
"""
# Tuple is a type of data structure. It works like list and be able to store multiple values
# The difference between tuple and list is: tuple is immutable(cannot be changed or modified)

coordinates = (4, 5)
# cannot re-assign to tuple
# coordinates[1] = 10

# you can access tuple each element by using index number
print(coordinates[1])

"""
Function
"""
# def indicates the start of function. if the indent below say_hi is same as say_hi,
# it is considered inside of the say_hi function.


def say_hi():
    print("Hello User")


say_hi()


def cube(num):
    return num*num*num


print(cube(3))

"""
if else statement
"""
is_male = True
is_tall = False

if is_male or is_tall:
    print("You are either male or tall")
elif is_male and not is_tall:
    print("You are male but not tall")
elif not is_male and is_tall:
    print("you are not male but tall")
else:
    print("You are either not male or not tall or both")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 4, 5))


# != -> is not equal, == -> is equal

# with float, you can convert input to the float number from string
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

"""
dictionaries
"""

