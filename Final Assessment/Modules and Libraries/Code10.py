import os
path = input("Enter directory path: ")
files = os.listdir(path)
print("Files in the directory:")
for file in files:
    print(file)
