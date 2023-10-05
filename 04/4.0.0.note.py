# ###Psudorandomization### 

# import random
# # import my_module

# #get any number between a and b (1 and 10 in this case.)
# random_integer = random.randint(1,10)

# print (random_integer)

# # #module
# # print(my_module.pi)

# ##.random : Returns the next random floating point number between [0.0 to 1.0)
# random_float = random.random()
# print(random_float)


# ### expand range - using muliplication : random_float * 5 (random decimal number between 0 and 5)
# randomFloat = random.random() * 5 
# print(randomFloat)


# love_score = random.randint(1,100)
# print(f"your love score is {love_score}")


# ##.uniform : random decimal number betwee 0 and 5 : Returns a random floating point N such that a <= N <= b if a <= b and b <= N <= a if b < a.
# random_decimal = random.uniform(0,5)
# print(random_decimal)

##############################
##Offsets and Appending items to Lists##

#List [] - you have item inside, separated by , 

# state1 = "Delaware"
# state2 = "Pennsylvania"

#list data structure - added the list based on the time when the state join the union. 
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#index starting with 0 
print(states_of_america[0])

variable3 = states_of_america[2] 

#index with negative number - from the last item 
print(states_of_america[-3])

#rename the item 
states_of_america[1] = "Pencilvania"

print(states_of_america) 

#add an item at the end of the list - one item to be added 
states_of_america.append("Angelaland")

print(states_of_america)

#add list of itesms 
states_of_america.extend(["Angelaland", "Jack Bauer"])

## using index 

num_states = len(states_of_america)

print(states_of_america[num_states - 1])

## nested lists 

fruits = ["Strawberries", "Nectarines","Apple", "Grapes", "Peaches","Cherries", "Pears"]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1])