#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: HW12


#1. Print Hello World!
print("Hello World")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = False
admin = False
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
adminLogin = 190
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True and login == True and admin == True:
    print("Welcome, admin!")
    adminLogin += 1
if wifi == False:
    print("you are not connected to the correct wifi network")
if login == False:
    print("your login information is incorrect")
if admin == False:
    print("you are not an admin")