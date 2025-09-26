num = []
num1 = int(input("Enter 1st no. : "))
num.append(num1)
num2 = int(input("Enter 2nd no. : "))
num.append(num2)
num3 = int(input("Enter 3rd no. : "))
num.append(num3)
num4 = int(input("Enter 4th no. : "))
num.append(num4)

num_1 = min(num)
num_2 = max(num)

print(f"The Minimum Number in the list is : {num_1}")
print(f"The Maximum Number in the list is : {num_2}")