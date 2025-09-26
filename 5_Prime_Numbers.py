import math

def prime(number):
    if number <= 1:
        return False    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
var = int(input("Enter a number to check: "))
if prime(var):
    print(f"{var} is a prime number.")
else:
    print(f"{var} is not a prime number.")