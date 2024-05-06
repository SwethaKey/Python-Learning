# write a program that calculates the sum of all elements in a given tuple.

def sum_tuple(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_tuple(1,2,3,4,5))

# Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.

def given_tuple(tuple):
    new_even_tuple = []
    for item in tuple:
        if (item%2 == 0):
            new_even_tuple += (item,)
    return new_even_tuple

tuple = (1,8,3,4,10,20)
new_even_tuple = given_tuple(tuple)
print(new_even_tuple)


# Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
# example(2^3)

def power(base,exponent):
    result = 1
    for item in range(exponent):
        result = result*base
    return result

base = int(input("enter a base: "))
exponent = int(input("enter a exponent: "))
total_value = power(base,exponent)
print(total_value)



# Write a program that merges two dictionaries into a single dictionary. If a key is
# common to both dictionaries, the value from the second dictionary should be used.


def merge_dicts(dict1,dict2):
    merged_dict = dict1.copy()

    for key,value in dict2.items():
        merged_dict[key] = value

    return merged_dict
    
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'd': 5, 'e': 6}

merge_dict = merge_dicts(dict1,dict2)
print(merge_dict)

# Write a program that takes a string as input and prints its revers

def string(user_input):
    rev = " "
    for item in user_input:
        rev = item+rev
    return rev 


user_input = input("enter a string : ")
rev_string = string(user_input)
print(rev_string)

# Write a program that takes a list of integers as input and uses 
# list comprehension to create a new list 
# containing only the even numbers from the original list.

def extract_even_number(input_list):
    even_number = [num for num in input_list if num%2 == 0]
    return even_number
    
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_list = extract_even_number(original_list)
print(result_list)