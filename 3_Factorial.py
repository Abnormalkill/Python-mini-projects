n = int(input("Enter 1st Number : "))

def factorial():
    var = 1
    for i in range(1, n+1):
        var = var*i
    print(f"The Factorial Of The Number Is : {var}")
factorial()