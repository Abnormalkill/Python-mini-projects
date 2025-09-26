var1 = int(input("Enter 1st Number : "))
var2 = int(input("Enter 2nd Number : "))
var3 = input("Enter The Operator : ")

def sum():
    print(f"The Sum of The numbers is : {var1+var2}")

def subtract():
    print(f"The Subtraction of The numbers is : {var1-var2}")

def multiply():
    print(f"The Multiplication of The numbers is : {var1*var2}")

def divide():
    print(f"The Division of The numbers is : {var1/var2}")

def modulus():
    print(f"The Modulus of The numbers is : {var1%var2}")

if(var3 == "+"):
    sum()
elif(var3 == "-"):
    subtract()
elif(var3 == "*"):
    multiply()
elif(var3 == "/"):
    divide()
elif(var3 == "%"):
    modulus()
else:
    print("Invalid Operator! ")