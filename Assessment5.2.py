# Code1-Function to check if a number is prime. 
def is_prime(num):
    if(num <= 1):
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
num = 20
if(is_prime):
    print("Prime Number")
else:
    print("Not a prime Number")


# Code2-Function to reverse a string.
def reverse_string(text):
    return text[::-1]
string = "Dhruv"
reverse_text = reverse_string(string)
print(reverse_text)


# Code3-Function to find factorial.
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
num = 10
result = factorial(num)
print(result)

# Code4-Function to calculate simple interest. 
def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

principal = 1000
rate = 5
time = 2
interest = simple_interest(principal, rate, time)
print(interest)


# Code5-Function to check if a word is palindrome. 
def is_palindrome(word):
    return word == word[::-1]
text = input("Enter a word: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")

# Code6-Function to count vowels in a string.
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count
string = "Dhruva"
vowel_count = count_vowels(string)
print(vowel_count)

# Code7-Function to merge two lists.
def merge_lists(list1, list2):
    return list1 + list2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_lists(list1, list2)
print(merged_list)

 
# Code8-Function to find GCD of two numbers.
def gcd(a,b):
    while b !=0:
        a,b=b,a%b
    return a
num1 = 24
num2 = 36
result = gcd(num1, num2)
print("GCD of",num1, "and", num2, "is:", result)


# Code9-Function to find area of rectangle. 
def area_rectangle(length, width):
    return length * width
length = 5
width = 3
area = area_rectangle(length, width)
print(area)
# Code10-Function to check Armstrong number.
def is_armstrong(num):
    temp = num
    total = 0
    digits = len(str(num))
    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10
    return total == num
number = 20
if is_armstrong(number):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
