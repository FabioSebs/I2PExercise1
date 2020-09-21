"""Write a program that calculates average score on an exam. Assume we have a small
class of only three students. Assign each students score to variables called student1
student 2, and student 3 and then use these to find the avg score. Assign the avg to var
called avg. Print student scores and avg scores"""

import random

student1, student2, student3 = random.uniform(0,100), random.uniform(0,100),random.uniform(0,100)
total = 0
average =0 
scorelist = [student1, student2, student3]

print("Student Scores:")
for x in scorelist:
    total += x
    print(x)

average = total/len(scorelist)

print("Average: ",average)


