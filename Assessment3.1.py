#String Codes

# Code1-Take a string input and print its length
text = "Dhruv"
length = len(text)
print("Length of the string:", length)

# Code2-Convert a sentence to lowercase
sentence = "DHRUV"
lower_sentence = sentence.lower()
print("Lowercase sentence:", lower_sentence)


# Code3-Replace spaces with underscores in a string
text = "Dhruv"
modified_text = text.replace(" ", "_")
print("Modified string:", modified_text)

# Code4-Extract the first and last character of a string
text = "Dhruv"
first_char = text[0]
last_char = text[-1]
print("First character:", first_char)
print("Last character:", last_char)

# Code5-Reverse a string using slicing
text = "Dhruv"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)


# Code6-Count how many times a letter appears in a string
text = "Tandel"
letter ="a" 
count = text.count(letter)
print("The letter appears", count, "times")


# Code7-Check if a word is present in a sentence
sentence = "I am Dhruv"
word = "am"
if word in sentence:
    print("Word is present in the sentence")
else:
    print("Word is not present in the sentence")


# Code8-Take name & age and print using f-string formatting
name = "Dhruv"
age = 20
print(f"My name is {name} and I am {age} years old.")


# Code9-Remove extra spaces from the start and end of a string
text = " Dhruv "
clean_text = text.strip()
print("After removing spaces:", clean_text)


# Code10-Join a list of words into a single string with - between them
words = ["Python", "is", "very", "easy"]
result = "-".join(words)
print(result)


# List Codes

# Code1-Create a list of your 5 favorite movies
movies = ["Ms Dhoni-The Untold Story", "KGF", "Pushpa", "Titanic", "12th Fail"]
print(movies)

# Code2-Add a new movie to the list
movies = ["Ms Dhoni-The Untold Story", "KGF", "Pushpa", "Titanic", "12th Fail"]
movies.append("Chhava")
print(movies)

# Code3-Remove the first movie from the list
movies = ["Ms Dhoni-The Untold Story", "KGF", "Pushpa", "Titanic", "12th Fail"]
movies.pop(0)
print(movies)

# Code4-Sort a list of numbers in ascending order
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)

# Code5-Reverse a list
numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)

# Code6-Find the largest number in a list
numbers = [5, 2, 9, 1, 7]
largest = max(numbers)
print("Largest number:", largest)

# Code7-Merge two lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)

# Code8-Access the last element of a list without using index number
movies = ["Ms Dhoni-The Untold Story", "KGF", "Pushpa", "Titanic", "12th Fail"]
print(movies[-1])


# Code9-Create a nested list and access a specific inner element
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])

# Code10-Count how many times an element appears in a list
numbers = [1, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)
print("2 appears", count, "times")



