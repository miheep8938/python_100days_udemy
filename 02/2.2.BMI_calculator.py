#BMI = weight (kg) / height power of 2 (m) 

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_int = float(height)
weight_int = int(weight)

print(int(weight_int / (height_int**2)))

##solution 
# bmi = int(weight)/float(height)**2
# bmi_as_int = int(bmi)
# print(bmi_as_int)