#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: HW4

#1. Print "Hello World!"
print("Hello World")
#2. import the 'math' library
import math
#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.
x = float(input("Please enter a decimal number"))
y = int(input("Please enter an integer"))
#4. Create a variable with the value that is x and y added together.
XandY = x + y
#5. Print the variable from #4.
print(XandY)
#6. Create a variable with the value that is x and y added together, then divide the sum by 3.
bleh = XandY / 3
#7. Print the variable from #6.
print(bleh)
#8. Create a variable with the value of the square root of y, then print the result.
RootY = math.sqrt(y)
print(RootY)
#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.
RoundTenth = round(x, 1)
print(RoundTenth)
#10. Use the ceiling function to round x up to the nearest whole number. Print the result.
print(math.ceil(x))
#11. Use the floor function to round x down to the nearest whole number. Print the result.
print(math.floor(x))