# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

###concat two names and make them lower case
concat = name1 + name2
com_names = concat.lower()


#print(com_names)

# t = com_names.count('t')
# r = com_names.count('r')
# u = com_names.count('u')
# e = com_names.count('e')

# true = t + r + u + e 

# l = com_names.count('l')
# o = com_names.count('o')
# v = com_names.count('v')
# e = com_names.count('e') 

# love = l + o + v + e 

# score = (print(f"{true}{love}"))


### Add numbers for each letter ### 
true = com_names.count('t') + com_names.count('r') + com_names.count('u') + com_names.count('e')

love = com_names.count('l') + com_names.count('o') + com_names.count('v') + com_names.count('e')

### change them into integer ### 
score = int('{}{}'.format(true, love))

### calculate love score ### 
if score < 10 or score > 90: 
    print (f"Your score is {score}, you go together like coke and mentos.")

elif score >= 40 and score <=50:
     print (f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

# if com_names == 't' :
#     t= com_names.count('t')
# print(t)


############solution########### 
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()

# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")

# true = t + r + u + e

# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")

# love = l + o + v + e 

# love_score = int(str(true) + str(love))#######

# if (love_score < 10) or (love_score > 90): 
#     print(f"Your love score is {love_score}, you go together like coke and menthos.")

# if (love_score >= 40) and (love_score <=50):
    # print(f"Your love score is {love_score}, you are alright together.")




