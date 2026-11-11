#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: HW16


#1. import the "random" library
import random
#2. print "Hello World!"
print("hello world!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter yet another number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
d = a + b
e = d / c
print(e)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
round(e)
if e % 2 == 0:
    print(f"{e} is Even")
else:
    print(f"{e} is Odd")
#6. Create a list of five different random integers between 1 and 10.
list = [random.randint(1, 10) for i in range(0, 5)]
#print(list)
#7. Print the 4th number in the list.
print(list[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
list.append(random.randint(1, 10))
#print(list)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
list.sort()
#print(list)
print(list[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i < 100 :
    print(i)
    i += i
print(i)
#11. Create a list containing the names of five other students in the classroom.
name_list = ["Cody", "Eden", "Huxley", "Brody", "Owyn"]
#12. Create a for loop that individually prints out the names of each student in the list.
for i in name_list:
    print(i)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for y in range (1, 100):
    if y % 10 != 0:
        print(y)
    else:
        break

#14. Free space. Do something creative. :)
loop = 0
while loop == 0:
    number = int(input("Pick a number, any number, remember it: "))
    answer = random.randint(1, 2)
    if answer == 1:
        print(number)
        correct = input("is this your number?")
        if correct == "yes":
            print("yayy :D")
            loop = 1
        elif correct == "no":
            print("aww :( lets try again")
            continue
    else:
        print(random.randint(1, 1000))
        correct = input("is this your number?")
        if correct == "yes":
            print("yayy :D")
            loop = 1
        elif correct == "no":
            print("aww :( lets try again")
            continue