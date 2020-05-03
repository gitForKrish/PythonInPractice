# class Teddy:
#     quantity = 200  # Class attribute

# myTeddy = Teddy()
# print(myTeddy)
# print(myTeddy.quantity)

# class Teddy:
#     quantity = 200

#     def __init__(self, name, color):
#         self.name = name        # instance attribute
#         self.color = color      # instance attribute

#     def changeColor(self, color):
#         self.color = color

# myTeddy1 = Teddy("Ted", "Red")
# print(myTeddy1)
# print(myTeddy1.quantity)
# print(myTeddy1.name)
# print(myTeddy1.color)

# myTeddy2 = Teddy("Rob", "Brown")
# print(myTeddy2)
# print(myTeddy2.quantity)
# print(myTeddy2.name)
# print(myTeddy2.color)
# myTeddy2.changeColor("White")
# print(myTeddy2.color)

# class Student:
#     name = ""
#     age = ""

#     def getData(self, name, age):
#         self.name = name
#         self.age = age
    
#     def showData(self):
#         print(self.name)
#         print(self.age)

# student1 = Student()
# student1.getData(name=input("Enter student name: "), age=input('Enter student age: '))
# student1.showData()

class ScienceStudent():
    def science():
        print('This is a science method')

sciStud1 = ScienceStudent()
sciStud1.science()
# sciStud1.getData()
# sciStud1.showData()