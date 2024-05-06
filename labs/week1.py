# Given String
s = "python"
print(s[0:1])
print(s[0:4])
print(s[1:4])
print(s[::-1])

# output will be [b,c] -1 is not inclue last element
# list = ['a', 'b', 'c', 'd']
#  print(list[1:-1])

# Given the Nested List
i = [3,7,[1,4,"hello"]]
i[2][2] = "goodbye"
print(i)


# using keys and indexing,grab the "hello" from the following dictionaries:

d1 = {'simple_key': 'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':
      [
          {'nest_key':
           ['this is deep',['hello']]
          }
      ]
     }
print(d3['k1'][0]['nest_key'][1][0])

# Use a set of find the unique values of the list below:

mylist = [1,1,1,1,2,2,2,2,3,3,3]
a = set(mylist)
print(a)


#you are giving two variable:
age = 4
name = "sammy"

print(f"Hello my dog name is {name} and he is {age} years old")
print("Hello my dog name is {} and he is {} years old".format(name,age))


student = {"Ram":{"name":"manga", "age":20, "course":"py"},
           "mohan":{"roll_no":20, "age":22, "course":"java"}}
           
print(student["mohan"])
print(student["Ram"]["age"])
student["mohan"]["phone"]=15356353
print(student["mohan"])
del student["mohan"]["phone"]
print(student["mohan"])

