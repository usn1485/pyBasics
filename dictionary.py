#Create a students Dict Object

students=[{'name':'Sam', 'school':'Lindenwood','age':25, 'grades':(34,68,79)},
{'name':'Shreya', 'school':'Washu','age':22, 'grades':(45,68,96)},
{'name':'Cloe', 'school':'SLU','age':24, 'grades':(76,76,79)}]

student={'name':'Sam', 'school':'Lindenwood','age':25, 'grades':(34,68,79)}
#write a function to get avarage 
def average_grade(data):
    grades = data['grades']  
    return sum(grades) / len(grades)


def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        # Implement here
        total+=sum(student['grades'])
        count+=len(student['grades'])
    return total / count

print(average_grade(student))
print(average_grade_all_students(students))