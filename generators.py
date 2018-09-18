

import itertools
import random

for k in itertools.count():
    # Rolling 3 dice
    # If all means all conditions have to be true
    # If all the conditions are true then only it will break
    if all(random.randint(1, 6) == 2 for x in range(3)):
        break

print(f"It took {k} tries to get 3 2's in a row")

# Order doesn't matter
# With permutations order does matter
print(list(itertools.combinations(['a','b','c','d'],2)))
# Combines every element in one string with the other string
# Spaces will also be combined
print(list(itertools.product("abc","123")))
# Method to generate binary digits upto 4 places
print(list(itertools.product([0,1],repeat=4)))

# Itertools function
# How to generate infinite numbers
# def my_counter():
#     my_number =1
#     while True:
#         yield my_number
#         my_number +=1
#
# for i in my_counter():
#     print(i)

