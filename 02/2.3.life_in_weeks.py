# Create a program using maths and f-Strings that tells us how many days, weeks, months 
# we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers. 

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)
years_left = 90 - age_int 

days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

#print(f"{days_left,weeks_left,months_left}")

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

