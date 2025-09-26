str1 = input("Enter A Line About Python : ")

str2 = str1.lower()
str3 = str2.split()

words = list(set(str3))
print(words)
