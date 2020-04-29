# #Different ways of defining a Dict object
from typing import Dict, Union

a_dict = {}

b_dict = {"name": 'Jack', "Age": "14", "Grade": "8"}
# print(b_dict)

c_dict = dict(zip(["salary", "country", "ph_no"], [5000, "USA", "576-905-4958"]))
# print(c_dict["salary"])

d_dict = dict([("school", "XYZ"), ("Fam_members", 3), ("wanna_be", 'Engineer')])
# print(d_dict["school"])

e_dict = dict({'Age': 10, 'name': "Katie", 'Grade': 5})
print(e_dict["name"])

# Adding more key value pairs to exisitng Dictionary
e_dict["fav_color"] = "Blue"
print(e_dict)

# deleting an item from dictionary
del e_dict["name"]
print(f'Deleting a key "{e_dict}')

# List all keys of dictionary
print(f'List of keys :{list(e_dict)}')


# a = dict(one=1, two=2, three=3)
# >>> b = {'one': 1, 'two': 2, 'three': 3}
# >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
# >>> e = dict({'three': 3, 'one': 1, 'two': 2})
#
#
#
# #Create a students Dict Object
#
# students=[{'name':'Sam', 'school':'Lindenwood','age':25, 'grades':(34,68,79)},
# {'name':'Shreya', 'school':'Washu','age':22, 'grades':(45,68,96)},
# {'name':'Cloe', 'school':'SLU','age':24, 'grades':(76,76,79)}]
#
# student={'name':'Sam', 'school':'Lindenwood','age':25, 'grades':(34,68,79)}
# #write a function to get avarage
# def average_grade(data):
#     grades = data['grades']
#     return sum(grades) / len(grades)
#
#
# def average_grade_all_students(student_list):
#     total = 0
#     count = 0
#     for student in student_list:
#         # Implement here
#         total+=sum(student['grades'])
#         count+=len(student['grades'])
#     return total / count
#
# print(average_grade(student))
# print(average_grade_all_students(students))
