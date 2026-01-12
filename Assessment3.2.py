# Tuple Codes

# Code1-Create a tuple with 5 numbers
numbers = (10, 20, 30, 40, 50)
print(numbers)

# Code2-Access the third element in a tuple
numbers = (10, 20, 30, 40, 50)
print(numbers[2])

# Code3-Unpack a tuple into separate variables
numbers = (10, 20, 30, 40, 50)
a, b, c, d, e = numbers
print(a, b, c, d, e)


# Set Codes

# Code4-Create a set of 5 fruits
fruits = {"apple", "banana", "mango", "orange", "grapes"}
print(fruits)


# Code5-Add a new fruit to the set
fruits = {"apple", "banana", "mango", "orange", "grapes"}
fruits.add("pineapple")
print(fruits)

# Code6-Remove an element from a set
fruits = {"apple", "banana", "mango", "orange", "grapes"}
fruits.remove("banana")
print(fruits)

# Code7-Find union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)

# Code8-Find intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)

# Code9-Check if one set is subset of another
small_set = {1, 2}
big_set = {1, 2, 3, 4}
print(small_set.issubset(big_set))

# Code10-Convert a list with duplicate values into a set to remove duplicates
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print(unique_numbers)


# Dictionary Code

# Code1-Create a dictionary storing student names and marks
students = {
    "Dhruv": 70,
    "Ritik": 50,
    "Avani": 40
}
print(students)

# Code2-Add a new key-value pair to an existing dictionary
students = {
    "Dhruv": 70,
    "Ritik": 50,
    "Avani": 40
}
students["Ravi"] = 45
print(students)

# Code3-Delete a key-value pair from a dictionary
students = {
    "Dhruv": 70,
    "Ritik": 50,
    "Avani": 40
}
del students["Dhruv"]
print(students)

# Code4-Merge two dictionaries into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)

# Code5-Check if a key exists in a dictionary
students = {
    "Dhruv": 70,
    "Ritik": 50,
    "Avani": 40
}
if "Dhruv" in students:
    print("Key exists")
else:
    print("Key does not exist")

# Code6-Count word frequency in a given string using a dictionary
text = "python is easy and python is powerful"
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)


# Code7-Find the key with the maximum value in a dictionary
marks = {"A": 75, "B": 88, "C": 92}
max_key = max(marks, key=marks.get)
print("Highest marks scored by:", max_key)

# Code8-Reverse keys and values in a dictionary
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)

# Code9-Update the value for a specific key
students = {
    "Dhruv": 70,
    "Ritik": 50,
    "Avani": 40
}
students["Rahul"] = 55
print(students)

# Code10-Convert a list of tuples into a dictionary
data = [("name", "Dhruv"), ("age", 21), ("city", "Valsad")]
result = dict(data)
print(result)
