""" 3 classes, they have 32,45, and 51 students. You want to divide the students
into groups with the same number of student in each group. Assume you would like
there to be 5 groups in the first class, 7 groups in second, and 6 groups in
third. Write program to calculate the number of students in each group. Print
this number for each class and also print the number of students leftover"""

classes = {
           'Class 1:': 32 ,
           'Class 2:': 45 ,
           'Class 3:': 51 
           }
leftover = {
           'Class 1:': classes['Class 1:']%5,
           'Class 2:': classes['Class 2:']%7,
           'Class 3:': classes['Class 3:']%6
           }
groups = {
          'Class 1:': classes['Class 1:']//5,
          'Class 2:': classes['Class 2:']//7,
          'Class 3:': classes['Class 3:']//6
         }

print("Number of students in each group:")

for x, y in groups.items():
    print(x,y)
    
print("Number of students leftover:")

for x, y in leftover.items():
    print(x,y)
