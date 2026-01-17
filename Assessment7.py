# #Code1-Create a base class Animal and subclasses Dog and Cat. 
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# dog = Dog()
# cat = Cat()
# dog.sound()
# cat.sound()

# #Code2-Create a class hierarchy for Vehicle → Car → ElectricCar. 
# class Vehicle:
#     def start(self):
#         print("Vehicle started")
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")
# class ElectricCar(Car):
#     def charge(self):
#         print("Electric car is charging")
# ecar = ElectricCar()
# ecar.start()
# ecar.drive()
# ecar.charge()

# #Code3-Implement method overriding in a base and derived class.
# class Parent:
#     def show(self):
#         print("This is parent class")
# class Child(Parent):
#     def show(self):
#         print("This is child class")
# obj = Child()
# obj.show()
 
# #Code4-Demonstrate multiple inheritance with two parent classes. 
# class Father:
#     def skills(self):
#         print("Father's skills")
# class Mother:
#     def qualities(self):
#         print("Mother's qualities")
# class Child(Father, Mother):
#     pass
# c = Child()
# c.skills()
# c.qualities()

# #Code5-Create a polymorphic function that works with different shapes.
# class Circle:
#     def area(self):
#         print("Area of Circle")
# class Rectangle:
#     def area(self):
#         print("Area of Rectangle")
# def calculate_area(shape):
#     shape.area()
# calculate_area(Circle())
# calculate_area(Rectangle())

# #Code6-Create a Bank system with SavingsAccount and CurrentAccount classes. 
# class BankAccount:
#     def deposit(self, amount):
#         print("Deposited:", amount)
# class SavingsAccount(BankAccount):
#     def interest(self):
#         print("Interest added")
# class CurrentAccount(BankAccount):
#     def overdraft(self):
#         print("Overdraft facility")
# s = SavingsAccount()
# s.deposit(1000)
# s.interest()
# c = CurrentAccount()
# c.deposit(2000)
# c.overdraft()

# #Code7-Create a class with private attributes and getter/setter methods. 
# class Person:
#     def __init__(self):
#         self.__age = 0  
#     def set_age(self, age):
#         self.__age = age
#     def get_age(self):
#         return self.__age
# p = Person()
# p.set_age(25)
# print("Age:", p.get_age())

# #Code8-Create a Teacher and Student class to show inheritance.
# class Teacher:
#     def teach(self):
#         print("Teacher is teaching")
# class Student(Teacher):
#     def study(self):
#         print("Student is studying")
# s = Student()
# s.teach()
# s.study()

#Code9-Create a MusicPlayer class and subclass Spotify to override play method. 
class MusicPlayer:
    def play(self):
        print("Playing music")
class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")
sp = Spotify()
sp.play()

#Code10-Demonstrate the use of super() in inheritance.	
class Animal:
    def __init__(self):
        print("Animal created")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")
d = Dog()
