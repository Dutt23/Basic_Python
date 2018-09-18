# A list
a_list = []
# A dictionary
# Key and value mapping , basically a hash table
a_dict = {}
# A set
a_set = set()


for letter in "Hello World":
    a_list.append(letter)
    a_set.add(letter)
    # Maps each letter to it's last position in the string
    a_dict[letter] = len(a_list)

print("List:",a_list)
print("Set:",a_set)
print("Dictionary:",a_dict)

# 2-D list ecample
a_list2 = []
for letter in "Hello":
    for letter2 in "World":
        a_list2.append((letter,letter2))

print("2-D List:",a_list2)

input = "Hello World"
# List comprehension
list2 = [letter for letter in input]
set2 = {letter for letter in "Hello World"}
# Key : Value
# Gives it a position to map
dict2 = {letter:i for i , letter in enumerate("Hello World",1)}

print(a_list == list2,a_set ==set2,a_dict==dict2,sep="\n")

# Multidimensional list

data = [[1,2],[4,5],[8,9],[2,9]]
# This will return a flattened one dimensional list
flattened = [value for row in data for value in row]
# This will return a 2-D list
# Evaluates the outer loop first then the inner loop
multidim = [[value for value in row] for row in data]

print("Flatted:",flattened,"Multi",multidim,sep="\n")

new_list = [[word.upper(),word.lower(),len(word)]for word in "the quick brown fox jumped over the lazy sheep".split()]
print(new_list)