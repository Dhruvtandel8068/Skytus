# #Task-1 To Do List 
# tasks = []
# while True:
#     print("\n TO DO LIST ")
#     print("1. Add Task") 
#     print("2. View Tasks")
#     print("3. Remove Task")
#     print("4. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         task = input("Enter task: ")
#         tasks.append(task)
#         print("Task added successfully")
#     elif choice == "2":
#         if len(tasks) == 0:
#             print("No tasks available")
#         else:
#             print("Your Tasks:")
#             for i in range(len(tasks)):
#                 print(i + 1, tasks[i])
#     elif choice == "3":
#         num = int(input("Enter task number to remove: "))
#         tasks.pop(num - 1)
#         print("Task removed")
#     elif choice == "4":
#         print("Exiting To-Do List")
#         break
#     else:
#         print("Invalid choice")

# Task-2 Quiz Game
score = 0
print("Quiz Started")
answer = input("1)Who is God of Cricket? ")
if answer.lower() == "Sachin Tendulkar":
    score += 1
answer = input("2)Who is the Prime minister of India?")
if answer == "Narendra Modi":
    score += 1
answer = input("3)what is the Full form of HTML ?")
if answer.lower() == "Hypertext markup Language":
    score += 1
print("Your Score:", score)
