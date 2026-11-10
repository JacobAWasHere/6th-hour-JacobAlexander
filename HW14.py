#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: HW14
import random as r
import time

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i > 0:
    time.sleep(0.1)
    print(i)
    i = i - 1
else:
    print("hello world")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
e = 1
while e < 30:
    if e % 2 == 0:
        time.sleep(0.1)
        print(e)
        e = e + 1
    else:
        e = e + 1

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
x = 1
while x < 30:
    if x % 3 == 0:
        x = x + 1
        continue
    else:
        time.sleep(0.1)
        print(x)
        x = x + 1

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
y = r.randint(1, 10000)
while not y == 1:
     time.sleep(0.1)
     print(y)
     y = r.randint(1, 10000)

#5. Create a while loop that asks for a number input until the user inputs the number 0.
answer = int(input("pick a number. DONT pick zero"))
while not answer == 0 :
    answer = int(input("pick a number. DONT pick zero"))
print("aw man :(")