
class student:
    def __init__(self, name):
        self.name = name
    def displayUsername(self):
        print(self.name)

 # self  keyword is used for accessing variables of the same class
std = student("de Developer")
std.displayUsername()
#to modify class properties we can do that like this ...
std.name = "DE Developer"
std.displayUsername()
# to delete class properties we can do that like this ...
del std.name
std.displayUsername()
# we can also delete the object of the class
del std
std.displayUsername()
#now it will show error....
