str = input("Enter A Line About Python : ")

str1 = str.lower()
str2 = str1.replace(",", " ")
str3 = str2.split()
str4 = str3.count("python")
print(f"The Word Python Is Used {str4} Times.")