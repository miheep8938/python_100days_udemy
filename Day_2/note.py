###Data Types###

print("Hello"[4])
print("123" + "345")

# #Integer 
print(123+ 345)

#Float
3.14159 

# Boolean 
True 
False 

# Convert Data Type

num_char = len(input("What is your name?"))
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")
print(type(num_char))

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70)+str(100))

# division, print float always. 
print(6/3)

# PEMDAS
# () PARENTHESIS
# ** EXPONENTS
# * MULTIPLICATION
# / DIVISION
# + ADDION
# - SUBTRACTION


# print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 + 3) / 3 - 3)

#Floor Division
print(8 // 3)
print(round(2.6777,2))

#+=, -=, *=, /= 
# result = result /2
# score = score + 1 
result = 4/ 2
result /= 2
print(result)

score = 0 
score +=1 

#f-String for various data types 
score = 0 
height = 1.8 
isWinning = True 

print("your score is "+ str(score))

print(f"your score is {score}, your heigh is {height}, you are winning is {isWinning}")


