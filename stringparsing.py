s = 'hello'
print(list(s))

name = "Shatyaki Dutt"

first, last = name.split()

print(first)
print(last)

print("This is joining the string {first} + {last}".format(first=first, last=last))

# We can split using anything
print("to/a/path/done".split("/"))
# Controlling the number of spilts
print("Apples,Bananaes,Something,Again more, And more".split(",", 2))

# Splitting from the right hand side
file_path = 'path/home/this/file.ext'
print("path/home/this/file.ext".rsplit(".", 1)[-1])

# Getting file base name

print("path/home/this/file.ext".split("/")[-1])
# Getting only the extension of the file
print(file_path.split('/', 1)[-1].split('.', 1)[-1])

# Splitting and joinning strings
parts = "Apples and Bananas".split("and")
print("or".join(parts))

" ".join([str(1), str(2), str(3)])

if isinstance(name, str):
    name.isprintable()
    name.isalnum()
    print(
    name[0].islower(),
    name[0].isupper()
    )
