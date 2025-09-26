import random
diction = {"sisser": 0, "stone": 1, "paper": 2}
rev_dict = {0 :"sisser", 1 :"stone", 2 :"paper"}
var = input("Enter Your Choice : ")
var1 = var.lower()
var2 = random.choice([1, 0, 2])
var1_num = diction[var1]
print(f"You Choosed {rev_dict[var1_num]} \n Computer Choosed {rev_dict[var2]}")
if(var1_num == var2):
    print("Draw !")
else:
    if(var1_num == 0 and var2 == 2):
        print("You Win !")
    elif(var1_num == 1 and var2 == 0):
        print("You Win !")
    elif(var1_num == 2 and var2 == 1):
        print("You Win !")
    elif(var1_num == 0 and var2 == 1):
        print("You Loose !")
    elif(var1_num == 1 and var2 == 2):
        print("You Loose !")
    elif(var1_num == 2 and var2 == 0):
        print("You Loose !")
    else:
        print("Ivalid")
