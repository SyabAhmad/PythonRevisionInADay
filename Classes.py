
class student:
    def __init__(self, name):
        self.name = name
    def displayUsername(self):
        print(self.name)

 # self  keyword is used for accessing variables of the same class
std = student("de Developer")

std.displayUsername()

