# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum_height = 0
num_students = 0 

for heights in (student_heights):
    sum_height += heights
    num_students += 1 

# print(sum_height)
# print(num_students) 

avg = round(sum_height / num_students)
print(avg)


# sum_height += student_heights[n]

    

#print(student_heights[0]+student_heights[1])
#print(student_heights)

###Another Solution###

# total_heights = 0 

# for height in student_heights: 
#     total_height += height

# count_students = 0 
# for student in student_heights:
#     count_students += 1





