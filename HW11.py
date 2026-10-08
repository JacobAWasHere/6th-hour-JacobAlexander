#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("hello world")
#2. Create a list with three variables that each randomly generate a number between 1 and 100

listA = [random.randint(1, 100),random.randint(1, 100),random.randint(1, 100)]
#3. Print the list.
print(listA)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if listA[0] > listA[1] and listA[0] > listA[2]:
    print(f"{listA[0]} is the highest number")
elif listA[1] > listA[0] and listA[1] > listA[2]:
    print(f"{listA[1]} is the highest number")
elif listA[2] > listA[0] and listA[2] > listA[1]:
    print(f"{listA[2]} is the highest number")
else: print("there is more than one highest number")
#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.