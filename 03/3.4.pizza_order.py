# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# small = 15
# medium = 20
# large = 25 
# pep_small = 2
# pep_large = 3 
# cheese = 1 

bill = 0 

if size == "S": 
    bill = 15

    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1

elif size == "M":
    bill = 20 
    if add_pepperoni == "Y": 
        bill += 3
    if extra_cheese == "Y":
        bill += 1

elif size == "L":
    bill = 25 
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    
print (f'Your final bill is: ${bill}.')

####Solution###

bill = 0 

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else: 
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3

if extra_cheese == "Y":
    bill += 1

print ({bill})









# if add_pepperoni == "Y":
#     if size == "S": 
#         bill = 15 
#         bill += 2

#     elif size == "M":
#         bill = 20
#         bill += 3
#     else:
#         bill = 25 
#         bill += 3 

# if extra_cheese == "Y":
#     bill += 1

# # else:
# #     print(str(bill))

# print(f"Your final bill is: ${bill}.")





# if size == "S" and add_pepperoni =="Y": 
#     bill = 15
#     bill += 2
#     # print (f"pay ${bill}") 

# elif size == "M" and add_pepperoni == "Y":
#     bill = 20
#     bill += 3 
#     # print (f"pay ${bill}")

# elif size == "L" and add_pepperoni == "Y":
#     bill = 25
#     bill += 3 

# # else:
# #     print ("")
# #     # print (f"pay ${bill}")

# if extra_cheese == "Y":
#     bill += 1

     
# print(f"Your final bill is ${bill}")

#Other solution# 
# print("Welcome to Python Pizza Deliveries!")
# small = 15
# medium = 20
# large = 25
# pep_small = 2
# pep_medium_large = 3
# xtra_cheese = 1
# bill = 0
 
# size = input("What size pizza do you want? S, M, or L ")
# if size.lower() ==  "s" :
#       bill = 15
# elif size.lower() == "m" :
#       bill = 20
# else :
#       bill = 25
 
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# if add_pepperoni.lower() == "y":
#       if bill == 15 :
#             bill +=  2
#       else :
#             bill += 3
# extra_cheese = input("Do you want extra cheese? Y or N ")
# if extra_cheese.lower() == "y" :
#       bill += 1
 
# print(f"Your final bill is ${bill}") 

##########
#Write your code below this line 👇
# bill = 0
 
# if size == "S":
#     bill +=15
#     if add_pepperoni == "Y":
#         bill +=2
# elif size == "M":
#     bill +=20
#     if add_pepperoni == "Y":
#         bill +=3
# else:
#     bill +=25
#     if add_pepperoni == "Y":
#         bill +=3
# if extra_cheese == "Y":
#     bill +=1
 