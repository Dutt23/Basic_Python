# Normal checking
# 255 is to make sure it stays within one byte of data
checksum = 0
a_string= "12 34 56 23"
for letter in a_string:
    checksum = (checksum + (32*ord(letter)+12)) %255

print(checksum)
import hashlib
with open(__file__,"rb") as f:
    print(hashlib.md5(f.read()).hexdigest())

# Encoding passwords
# sha1 is one method for encoding passwords
# hexdigest consumes the hexadecimal object
# Before comparing anything in hashing it must be converted to bytes


password = "test"
hashed_pwd = hashlib.sha1(password.encode('utf8')).hexdigest()
password="Password nullified"
print(hashed_pwd)
# The b before the test converts it into bytes
print(hashlib.sha1(b"test").hexdigest() == hashed_pwd)