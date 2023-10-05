##Defining function## 

def my_function():
  print("Hello")
  print("Bye")

##Once you define a function, make sure you trigger / call the function## 
my_function()

##While loops 

'''
#for loops 

for item in list_of_items: 
 #Do something to each item

for number in range(a,b):
    print(number)
'''

'''
While loops 

while something_is_true:
 #Do something repeatedly 
''' 




###REEBORG ###
##https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json


###Hurdle 1###

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def path ():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


path()
path()
path()
path()
path()
path()

for step in range (6):
   path()

###Hurdle 2 ### 

number_of_hurdles = 6 
while number_of_hurdles > 0:
    path()
    number_of_hurdles -= 1 
    print(number_of_hurdles)
'''


###while loop can be more dangerous than for loop### 

# while at_goal() != True: 
#  path()
    
#while not at_goal():
#    path()

'''
infinite loop
while 5>3: 
 do this and do that 
'''


### Hurdle 3 ### 

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def path ():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#front_is_clear()
#wall_in_front()
#at_goal()

while not at_goal():
    if front_is_clear():
        move()
    elif not front_is_clear():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

'''



### solution ## 
# def path ():
#     #move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# while not at_goal():
#     if wall_in_front():
#         path()
#     else:
#         move()


###Hurdle 4 ### 

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def path ():
    #turn_left()
    #move()
    turn_right()
    move()
    turn_right()
    move()
    #turn_left()

while not at_goal():
    if wall_in_front() and right_is_clear():
        path()
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        move()
    else: 
        path()
'''



##Another Solution##
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def path ():
#     turn_left()
    
#     while wall_on_right():
#         move()
        
#     turn_right()
#     move()
#     turn_right()
    
#     while front_is_clear():
#         move()
        
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         path()
#     else:
#         move()

##Solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
   

# while not at_goal():

#     if front_is_clear():

#         move()

#         if right_is_clear():

#             turn_right()

#     else:

#         turn_left()



###solution###
# while not at_goal():

#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()


###solution###

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
        
# while not at_goal():
#     while not wall_on_right():
#         turn_right()
#         move()        
#     if wall_in_front() == False:
#         move()
#     elif wall_in_front() == True:        
#         if right_is_clear() == True:
#             turn_right()
#             move()
#         elif wall_on_right() == True:
#             turn_left()           
#             if front_is_clear() == True:
#                 move()
#             elif wall_on_right() == True:
#                 turn_left()
#                 move()       