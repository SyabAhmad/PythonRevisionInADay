print("inheritance using python")
class Person:
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age
    def diplayDataOfUser(self):
        print(self.name)
        print(self.age)

class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        # print(self.name)
        # print(self.age)

std = Student("De Developer", 22)

std.diplayDataOfUser()


# print("inheritance using python")
# class Person:
#     def __init__(self, Name, Age):
#         self.name = Name
#         self.age = Age
#     def diplayDataOfUser(self):
#         print(self.name)
#         print(self.age)
#
# class Student(Person):
#     pass
#
# std = Student("De Developer", 22)
#
# std.diplayDataOfUser()

