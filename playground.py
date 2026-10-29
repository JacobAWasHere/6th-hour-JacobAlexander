# name : Jacob Alexander
# I tried to make a very simple calculator

print("hello, this is a calculator. what do you want to calculate?")
calculationOutput = "calculation error"
intInputOne = int(input("enter a number : "))
operation = input("enter an operation : ")
intInputTwo = int(input("enter another number : "))

if operation == "+":
    calculationOutput = f"{intInputOne + intInputTwo}"
if operation == "-":
    calculationOutput = f"{intInputOne - intInputTwo}"
if operation == "*":
    calculationOutput = f"{intInputOne * intInputTwo}"
if operation == "/":
    calculationOutput = f"{intInputOne / intInputTwo}"
if operation == "%":
    calculationOutput = f"{intInputOne % intInputTwo}"
if operation == "^":
    calculationOutput = f"{intInputOne ** intInputTwo}"
if operation == "**":
    calculationOutput = f"{intInputOne ** intInputTwo}"
if operation == ">":
    calculationOutput = f"{intInputOne > intInputTwo}"
if operation == "<":
    calculationOutput = f"{intInputOne < intInputTwo}"
if operation == ">=":
    calculationOutput = f"{intInputOne >= intInputTwo}"
if operation == "<=":
    calculationOutput = f"{intInputOne <= intInputTwo}"
if operation == "==":
    calculationOutput = f"{intInputOne == intInputTwo}"
if operation == "!=":
    calculationOutput = f"{intInputOne != intInputTwo}"
print(calculationOutput)