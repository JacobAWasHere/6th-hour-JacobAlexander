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
    num = listA[0]
elif listA[1] > listA[0] and listA[1] > listA[2]:
    print(f"{listA[1]} is the highest number")
    num = listA[1]
elif listA[2] > listA[0] and listA[2] > listA[1]:
    print(f"{listA[2]} is the highest number")
    num = listA[2]
else: print("there is more than one highest number")
#5. Tie the result (the largest number) from #4 to a variable called "num".
#the code for this is in #4
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by 2 and 3")
elif num % 2 != 0 and num % 3 != 0:
    print(f"{num} is not divisible by 2 or 3")
elif num % 2 == 0:
    print(f"{num} is divisible by 2")
elif num % 3 == 0:
    print(f"{num} is divisible by 3")