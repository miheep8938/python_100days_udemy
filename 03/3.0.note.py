### IF CONDITION ### 

# if condition: 
#  do this 
# else:
#  do this 

##drain water condition using if 
water_level = 90

if water_level > 80: 
  print("Drain water")

##ride - height limit 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: 
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

###comparison operators###
# > Greater than 
# < Less than 
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to
# % Modulo - remainder of the division 

##note: = assignment , == check euqality 

###Nested if and elif statements###
# if conditon:
# if another condtion:
#   do this
# else:
#   do this
# else:
#  do this

##ride - height limit with nested if 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: 
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

##elif## - you can add any many 'elif' condition as you want betwween 'if' and 'else'.
# if condition1: 
#   do A
# elif condition2:
#   do B
# else:
#   do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: 
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

#########Multiple If########### if on the same level, consider all the condition 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: 
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bill = 7 
    print("Please pay $7.")
  else:
    bill = 12
    print("Please pay $12.")

  wants_photo = input ("Do you want a photo taken? Y or N.")
  if wants_photo == "Y":
    #Add 3 to their bill
    # bill = bill + 3 
    bill += 3
    
  print (f"Your final bill is ${bill}")
    
else:
  print("Sorry, you have to grow taller before you can ride.")


####Logical Operators### 
# and, or , not 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: 
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bill = 7 
    print("Please pay $7.")
  elif age >= 45 and age >= 55:
    bill = 0
    print ("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Please pay $12.")

  wants_photo = input ("Do you want a photo taken? Y or N.")
  if wants_photo == "Y":
    #Add 3 to their bill
    # bill = bill + 3 
    bill += 3
    
  print (f"Your final bill is ${bill}")