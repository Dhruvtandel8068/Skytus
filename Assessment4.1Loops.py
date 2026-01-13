# Code1-Print numbers from 1 to 10.
for i in range(1,11):
    print(i)

# Code2-Display multiplication table for a given number.
num = 2
for i in range(1,11):
    print(num*i)

# Code3-Find factorial of a number.
num = 5
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(fact)


# Code4-Generate the first N Fibonacci numbers.
n = 5
a, b = 0, 1
for i in range(n):
    print(a)
    a,b = b,a + b

# Code5-Check if a number is prime.
num=17
is_prime=True
if(num<=1):
    is_prime=False
else:
    for i in range(2,num):
        if(num%i==0):
            is_prime=False
            break
if(is_prime):
    print("Prime Number")
else:
    print("Not a prime Number")

# Code6-Reverse a number (e.g., 123 → 321).
num=12345
reverse=0
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print(reverse)

# Code7-Count digits in a number.
num=8866108068
count=0
while(num>0):
    count +=1
    num=num//10
print(count)

# Code8-Find sum of even numbers between 1–100.
total=0
for i in range(2,101,2):
    total +=i
print(total)

# Code9-Print a pyramid pattern.
rows=5
for i in range(1,rows+1):
    print("*"*i)

# Code10-Find all divisors of a number.
num=100
for i in range(1,num+1):
    if(num%i==0):
        print(i)

