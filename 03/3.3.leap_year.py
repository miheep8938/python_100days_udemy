# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4 

# **except** every year that is evenly divisible by 100 

# **unless** the year is also evenly divisible by 400

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if (year % 4 == 0 and year % 100 != 0): 
    print ("Leap year.")

elif (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print ("Leap year.")

elif (year % 4 == 0 and year % 100 != 0 and year % 400 == 0):
    print ("Leap year.")

else: 
    print ("Not leap year.")

# ##First Attempt 
# if (year % 4 == 0): 
#     #print("Leap Year")

#     if (year % 100 == 0):
#         print("Leap Year")

#     elif (year % 100 != 0 ):
        
#         if (year % 400 == 0):
#             print("Leap year.")

        
#     else:
#         print("Not leap year.")
          
# else: 
#     print("Not leap year.")


# print(2020/4)
# print(2020/100)
# print(2020/400)

#refer to https://www.wikihow.com/Calculate-Leap-Years

#given solution
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0: 
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

##another solution## 
if year % 4 > 0:
  print("Not leap year.")
elif year % 400 == 0:
    print("Leap year.")
elif year % 100 == 0:
  print("Not leap year.")
else:
  print("Leap year.")

##Use Boolean##
year = int(input("Which year do you want to check? "))
 
isLeapYear = False
 
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
  isLeapYear = True
 
if isLeapYear:
  print("Leap year.")
else:
  print("Not leap year.")

