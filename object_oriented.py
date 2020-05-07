# Object oriented python programming has Class and functions. When we create an object the __init__ functions runs (instantiates) first

class Student:
    #Instantiates Object
    def __init__(self, name, age,grades):
        self.name = name
        self.age = age
        self.grades=grades

     #String representation of Object
    def __str__(self):
        return f"{self.name} who is {self.age} years old has {self.grades} grades."

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


# Create a student object
student = Student("Ujwala",23,(45, 56, 67, 30, 94))
# print(student.name)  call a class init method runs and can get the property defined in init method.
# print(student.name)
# print(student.average_grade())
print(student)
