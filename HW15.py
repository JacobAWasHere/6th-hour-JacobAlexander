#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: HW15
import time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.

for i in range(5, 0, -1):
    print(i)
    time.sleep(0.5)
print("hello world")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for a in range(1, 31):
    if a % 2 == 0:
        time.sleep(0.5)
        print(a)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for b in range(1, 31):
    if b % 3 == 0:
        continue
    time.sleep(0.5)
    print(b)
#4. Create a for loop that prints 5 different animals from a list.
for c in ["bird", "cat", "dog", "bee", "fox"]:
    time.sleep(0.5)
    print(c)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for d in input("give me a word")[::-1]:
    time.sleep(0.5)
    print(d)
#6. Create a list containing 10 integers of your choice and print the list.
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(list)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for e in list:
    if e % 2 == 0:
        evenNumbers = evenNumbers + 1
    else:
        oddNumbers = oddNumbers + 1
print(f"there are {evenNumbers} even numbers")
print(f"there are {oddNumbers} odd numbers")

#9. Create a variable that asks the user for an integer and an empty integer variable.r
g = int(input("give me a integer"))
h = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for i in range(1, g + 1):
    h *= i
print(h)