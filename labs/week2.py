#1] Write a program that calculates the sum of all elements in a given tuple.

my_tuple = (1,2,3,4,5)
sum = 0 
for item in my_tuple:
    sum = sum + item
    
print(sum)

#2] Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.

new_tuple = (2,5,8,10,25,12,13,18)
even_number = ()
for item in new_tuple:
    if (item%2 == 0):
        even_number += (item,)

print(even_number)


#3] Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
# example(2^3)

base = int(input("enter a base: "))
exponent = int(input("enter a exponent: "))
result = 1
for item in range(exponent,0,-1):
    result = result*base
print(result)


for i in range(exponent):
    result *= base
    print(i)

print(result)



#4] Write a program that merges two dictionaries into a single dictionary. If a key is
# common to both dictionaries, the value from the second dictionary should be used.

dict1 = {1: {"name":"sara"}, 2: {"age" : 20}}
dict2 = {1: {"name": "elin"}, 3: {"age" : 30}}

#method1
print(dict1|dict2)
#method2
print({**dict1,**dict2})
#method3
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)


# 5] Write a program that takes a list of integers as input and uses 
# list comprehension to create a new list 
# containing only the even numbers from the original list.


# syntax of list comprehension
# new_list = [new_item for item in list]

user_input = int(input("enter a user input : "))
even_number = [num for num in list if num%2==0]
print(even_number)


#6] Write a program that takes a string as input and prints its reverse.

# option 1: 
print(input("enter a number : ")[::-1])

# option 2:
name = "lexicon"
print(name[-1::-1])
print(name[::-1])

# option 3:
user_input = input("enter a name : ")
rev = ""
for i in user_input:
    rev = i+rev
print(rev)