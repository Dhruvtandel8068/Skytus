# # Code1-Write a program to read a file and display its contents.
# file = open("sample.txt", "w")
# file.write("Hello")
# file.close()
# file = open("sample.txt", "r")
# conent = file.read()
# print(conent)
# file.close()

# # Code2-Write a program to count the number of lines in a file.
# file = open("sample.txt","r")
# lines = file.readlines()
# print("Number of lines:",len(lines))
# file.close()

# # Code3-Write a program to count how many times each word appears in a file.
# file = open("sample.txt","r")
# words = file.read().split()
# file.close()
# words_count = {}
# for word in words:
#     words_count[word] = words_count.get(word, 0) + 1
    
#     print(words_count)


# # Code4-Write a program to write 5 user-entered sentences to a file.
# file = open("sentences.txt", "w")
# for i in range (1,6):
#     sentence = input(f"enter sentence {i}:")
#     file.write(sentence + "\n")
# file.close()
# print()

# # Code5-Write a program to append a list of strings to an existing file.
# lines = ["Python\n", "File Handling\n", "Append Mode\n"]
# file = open("sentences.txt", "a")
# for line in lines:
#     file.write(line)
# file.close()
# print("List of strings appended successfully.")

# # Code6-Write a program to read a file and print only lines containing a specific word.
# filename = input("Enter file name: ")
# word = input("Enter word to search: ")
# file = open(filename, "r")
# for line in file:
#     if word in line:
#         print(line.strip())
# file.close()

# # Code7-Write a program to replace a specific word in a file and save changes.
# filename = input("Enter file name: ")
# old_word = input("Enter word to replace: ")
# new_word = input("Enter new word: ")
# file = open(filename, "r")
# content = file.read()
# file.close()
# content = content.replace(old_word, new_word)
# file = open(filename, "w")
# file.write(content)
# file.close()

# print("Word replaced successfully.")


# # Code8-Write a program to merge the contents of two text files into a third file.
# file1_name = input("Enter first file name: ")
# file2_name = input("Enter second file name: ")
# merged_file_name = input("Enter merged file name: ")
# file1 = open(file1_name, "r")
# content1 = file1.read()
# file1.close()
# file2 = open(file2_name, "r")
# content2 = file2.read()
# file2.close()
# merged_file = open(merged_file_name, "w")
# merged_file.write(content1)
# merged_file.write("\n")
# merged_file.write(content2)
# merged_file.close()

# print("Files merged successfully.")

# # Code9-Write a program to read a CSV file and display its content in a formatted way.
# import csv
# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print("{:<5} {:<10} {:<5} {:<10}".format(
#             row[0], row[1], row[2], row[3]
#         ))

# Code10-Write a program to back up a file by copying its contents into another file.
source_file = input("Enter source file name: ")
backup_file = input("Enter backup file name: ")
try:
    file1 = open(source_file, "r")
    content = file1.read()
    file1.close()   
    file2 = open(backup_file, "w")
    file2.write(content)
    file2.close()
    print("Backup created successfully.")
except FileNotFoundError:
    print("Source file not found. Please check the file name.")
