# Conditional Statements

# Code1-Check if a person is eligible to vote (age ≥ 18).
age=20
if(age>=18):
    print("Eligible")
else:
    print("Not Eligible")

# Code2-Grade calculator based on marks: 90+ = A, 80+ = B, else C.
marks = 70
if(marks >= 90):
    print("Grade A")
elif(marks >= 80):
    print("Grade B")
else:
    print("Grade c")

# Code3-Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.
Signal = "yellow"

if(Signal == "Red"):
    print("Stop")
elif(Signal == "Green"):
    print("Go")
elif(Signal == "yellow"):
    print("Wait")
else:
    print("Invalid Signal")

# Code4-ATM withdrawal check: sufficient balance or not.
balance = 50000
withdraw = 60000
if(withdraw <= balance):
    print("Withdraw Successful")
else:
    print("Insufficient balance")

# Code5-Check if a number is positive, negative, or zero.
num = -20
if(num>0):
    print("Positive")
elif(num<0):
    print("Negative")
else:
    print("Zero")

# Code6-Check if a number lies within a given range.
num = 20
if(num >= 10 and num<=20):
    print("Number is within the range")
else:
    print("Number is outside the range")

# Code7-Username & password verification.
Username = "Admin"
password = "12345"

if(Username == "Admin" and password == "12345"):
    print("Login Successful")
else:
    print("Invalid Credentials")

# Code8-Electricity bill calculator based on units consumed.
units = 120
if(units <= 100):
    bill = units * 5
elif(units <= 200):
    bill = units * 7
else:
    bill = units * 10
print(bill)

# Code9-Simple calculator (add, subtract, multiply, divide).
a = 10
b = 20
operation = "*"

if(operation == "+"):
    print(a+b)
elif(operation == "-"):
    print(a-b)
elif(operation == "/"):
    print(a/b)
elif(operation == "*"):
    print(a*b)
else:
    print("Invalid operation")

# Code10-Check type of triangle (equilateral, isosceles, scalene).	
a = 10
b = 7
c = 5
if(a == b and b == c):
    print("Equilateral Triangle")
elif(a == b or b == c or a == c):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")