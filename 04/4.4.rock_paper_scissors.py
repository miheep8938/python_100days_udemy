rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

## your choice

your_choice = int(input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")) 


#print(type(your_choice))


## computer_random 
import random

computer_choice = random.randint(0,2)

print(computer_choice)

## picture in the list ## 
image = [rock, paper, scissors] 

#print(image[0])

your_img =  image[your_choice]
com_img = image[computer_choice]

#print(your_img,com_img)


## integer to rock, paper, scissors ## 

## win_lose ## 
## 0 , 1 => 1 win 
## 1 , 2 => 2 win
## 0 , 2 => 0 win  


# if computer_choice

your_str = "You chose"
com_str = "Computer chose"

if your_choice > 2 or your_choice < 0: 
  print ("Invalid number. Choose again.")

elif your_choice == computer_choice + 1 or your_choice == (computer_choice - 2):
  print(f"{your_str} :\n {your_img}\n {com_str} :\n {com_img}\n You Win")

elif your_choice == computer_choice:
  print(f"{your_str} :\n {your_img}\n {com_str} :\n {com_img}\n It's a draw")

else:
  print(f"{your_str} :\n {your_img}\n {com_str} :\n {com_img}\n You Lose")


###
# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")

##Another Solution## 
# user = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor.\n"))
# computer = random.randint(0,2)
 
# choices = [rock, paper, scissors]
 
# print(choices[user])
# print("The computer threw:")
# print(choices[computer])
 
# if ((user + 1) % 3 == computer):
#   print("You lost!")
# elif(user == computer):
#   print("It's a tie!")
# else:
#   print("You win!")

##Solution 3## 
# import random
# arr = [rock, paper, scissors]
 
# userChoose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
 
# if userChoose>2 or userChoose<0:
#   print('You typed an invalid number, you lose')
# else: 
#   aiChoose = random.randint(0,2)
#   print(arr[userChoose])
 
#   print( f"Computer choose {arr[aiChoose]}")
 
#   results = userChoose, aiChoose
 
#   if results[0] == results[1]:
#     print('There´s no winner')
#   elif results ==(0,2) or results==(1,0) or results==(2,1):
#     print('You win!')
#   else:
#     print('Sorry, you lose')

