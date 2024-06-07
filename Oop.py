#object oriented programming
#class Dog:
#     def __init__(self):
#         pass
#    def add_one(self, x):
#        return x + 1

#    def bark(self):
#        print("bark")
#
#d = Dog()
#d.bark()
#print(d.add_one(5))
#print(type(d))

#class Dog:
#    def __init__(self, name, age, phone):
#        self.name = name
#        self.age = age
#        self.phone = phone
#    def get_name(self):
#        return self.name

#    def get_age(self):
#        return self.age

#    def get_phone(self):
#        return self.phone

#    def add_one(self, x):
#        return x + 1

#    def bark(self):
#        print("bark")

#d = Dog("Tim", 34, "08091551450")
#print(d.get_name())
#print(d.get_age())
#print(d.get_phone())


#class Cat:
#    def __init__(self,name,age):
    #    self.name = name
    #        self.age = age

#    def get_name(self):
#        return self.name

#   def get_age(self):
#        return self.age
#
#    def set_age(self, age):
#        self.age = age

#c = Cat("Kettle", 24)
#c.set_age(15)
#print(c.get_name())
#print(c.get_age())

#================MORE COMPLEX WORK
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade    #0-100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for students in self.students:
            value += students.get_grade()

        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())

#Inheritance
