# #Code1-Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.
# class Car:
#     def __init__(self, brand, model, speed):
#         self.brand = brand
#         self.model = model
#         self.speed = speed
#     def accelerate(self):
#         self.speed += 10
#         print("Speed after accelerating:", self.speed)
#     def brake(self):
#         self.speed -= 10
#         print("Speed after braking:", self.speed)
# car = Car("Toyota", "Fortuner", 50)
# car.accelerate()
# car.brake()


# #Code2-Create a BankAccount class with deposit and withdraw methods.
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print("Balance after deposit:", self.balance)
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Balance after withdraw:", self.balance)
#         else:
#             print("Insufficient balance")
# account = BankAccount(5000)
# account.deposit(1000)
# account.withdraw(3000)


# #code3-Create a Student class with a method to calculate average marks.
# class Student:
#     def __init__(self, marks):
#         self.marks = marks
#     def average(self):
#         return sum(self.marks) / len(self.marks)
# student = Student([80, 85, 90])
# print("Average Marks:", student.average())


# # Code4-Create a Rectangle class with methods to find area and perimeter.
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2 * (self.length + self.width)
# rect = Rectangle(10, 5)
# print("Area:", rect.area())
# print("Perimeter:", rect.perimeter())


# #Code5-Create an Employee class that displays salary details. 
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
# emp = Employee("Dhruv", 30000)
# emp.display()

# #Code6-Create a Book class to store title, author, and price, and display details. 
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def show(self):
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.price)
# book = Book("Life", "Tandel", 499)
# book.show()

# #Code7-Create a Circle class to find area and circumference. 
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
#     def circumference(self):
#         return 2 * 3.14 * self.radius
# circle = Circle(7)
# print("Area:", circle.area())
# print("Circumference:", circle.circumference())

# #Code8-Create a Laptop class with a method to apply discounts on price.
# class Laptop:
#     def __init__(self, price):
#         self.price = price
#     def apply_discount(self, percent):
#         discount = self.price * percent / 100
#         self.price -= discount
#         print("Price after discount:", self.price)
# laptop = Laptop(60000)
# laptop.apply_discount(10)

# #Code9-Create a Flight class with seat booking functionality. 
# class Flight:
#     def __init__(self, seats):
#         self.seats = seats
#     def book_seat(self):
#         if self.seats > 0:
#             self.seats -= 1
#             print("Seat booked. Seats left:", self.seats)
#         else:
#             print("No seats available")
# flight = Flight(3)
# flight.book_seat()
# flight.book_seat()

#Code10-Create a Shop class with a method to add and list products.
class Shop:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def list_products(self):
        print("Products in shop:")
        for p in self.products:
            print(p)
shop = Shop()
shop.add_product("Laptop")
shop.add_product("Mobile")
shop.list_products()
