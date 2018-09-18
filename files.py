# With conext managers.
# The "wb" is write in binary.
# Context managers make sure the file is clo
filename = "Test.dat"
with open(filename,"wb") as f:
    f.write(b"This is a string")

my_file = open(filename,"wb")
user_input = input("Enter your name")
try:
    # Files can only read and write in bytes
    # Hence the encoding is done to convert to bytes
    my_file.write(user_input.encode("utf8"))
except Exception as e:
    import traceback
    # Prints the traceback
    # Without actually breaking the flow
    traceback.print_exc()
    # Raises the actual error
    # Causes the actual error to trigger
    raise
    print("Not shown")
finally:
    my_file.close()
    print("Printing in the finally loop , all done")


with open(filename,"rb") as f_in:
    # If the files is encoded then you have to decode to read it back
    print(f_in.read().decode("utf8"))

