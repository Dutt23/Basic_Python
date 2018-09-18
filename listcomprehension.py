# Replace all numbers divisible by 3 to fizz
fizzes = [i if i%3 else "fizz" for i in range(1,50)]
# print(fizzes)
# If the number divided by 5 has no remainder then only print
# Replaced every 3 and 5 with fizz and buzz
fizzes_less_five = ["Fizz"*(x % 3 == 0) + "Buzz"*(x % 5 == 0) or str(x)
       for x in range(1, 50)]

# fizzes_buzzes = [i if i%5 else "buzz" for i in fizzes_less_five if isinstance(i, int)]
print(fizzes_less_five)
# Only works if number divided by 5 has no remiander

fizzes_no_5 = [i if i%3 else "Fizz" for i in range(1,50) if i%5]
print(fizzes_no_5)

# Creating a list with all primes
# The limit
# Set is easier to search as time complexity is less
# List has a time complexity of n , which is the size of the list
n = 100
non_prime = [j for i in range(2,8) for j in range(i*2,n,i) ]
print("Non Primes" + non_prime)

prime =[x for x in range(2,n) if x not in non_prime]
print("Primes"+ prime)

