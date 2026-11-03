#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: SC3

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
num = 1
import time
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        time.sleep(0.25)
        print("FizzBuzz")
        num = num + 1
    else :
        if num % 3 == 0 :
            time.sleep(0.25)
            print("Fizz")
            num = num + 1
        elif num % 5 == 0 :
            time.sleep(0.25)
            print("Buzz")
            num = num + 1
    if not num % 3 == 0 and not num % 5 == 0:
        time.sleep(0.25)
        print(num)
        num = num + 1
