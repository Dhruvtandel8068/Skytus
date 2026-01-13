# Code1-Write a program to handle division by zero error.
try :
    a = 10
    b = 2
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by Zero")
# Code2-Write a program to handle invalid integer input.
try:
    num = int("abc")
    print(num)
except ValueError:
    print("Invalid integer input")

# Code3-Write a program to open a file and handle the “file not found” error.
try:
    file = open("data.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
# Code4-Write a program to demonstrate multiple exception blocks.
try:
    a = int("abc")
    b = 10 / 0
except ValueError:
    print("Value Error Occurred")
except ZeroDivisionError:
    print("Division by zero error")

# Code5-Write a program to use finally for resource cleanup.
try:
    file = open("test.txt", "w")
    file.write("Helloo")
except:
    print("Error occurred")
finally:
    file.close()
    print("File closed")

# Code6-Write a program to create a custom exception for invalid age (<18).
class InvalidAgeError(Exception):
    pass
try:
    age = 15
    if(age < 18):
        raise InvalidAgeError("Age must be 18 or above")
except InvalidAgeError as e:
    print(e)

# Code7-Write a program to handle IndexError when accessing a list.
try:
    my_list = [1,2,3]
    print(my_list[5])
except IndexError:
    print("Index out of range")

# Code8-Write a program that takes two numbers and handles all possible errors.
try:
    a = 5
    b = 8
    print(a / b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception:
    print("Some other error occurred")

# Code9-Write a program to log errors to a file instead of printing them.
import logging
logging.basicConfig(filename="error.log", level=logging.ERROR)
try:
    a = 10 / 0
except Exception as e:
    logging.error(e)

# Code10-Write a program that validates an email format and raises an exception for invalid ones.
class InvalidEmailError(Exception):
    pass
try:
    email = "usergmail.com"
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format")
    print("Valid email")
except InvalidEmailError as e:
    print(e)