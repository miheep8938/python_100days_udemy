# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#number of names in the list 

length_names= len(names)


random_num = random.randint (0, length_names - 1)
# print(random_num) 

person_chosen = names[random_num]
print(f"{person_chosen} is going to buy the meal today!")


#### use random.choice () 

# person_chosen = random.choice (names)
# print(names[0]) 

# random_num = random.randint(0,4)

# if random_num == 0: 
#     print(name[0])
# elif random_num == 1:
#     print(name[1])
# elif random_num == 2:
#     print(name[2])
# elif random_num == 3:
#     print(name[3])
# else:
#     print(name[4])


#f"{names[0]} is going to buy the meal today!"