#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: HW8


#1. Import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three different variables that each randomly generate an integer between 1 and 10
roll1 = random.randint(1,10)
roll2 = random.randint(1,10)
roll3 = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(roll1, roll2, roll3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
roll1_plus2 = roll1 + 2
roll2_minus4 = roll2 - 4
roll3_times1andhalf = roll3 * 1.5
#6. Print each result from #5 on the same line.
print(roll1_plus2, roll2_minus4, roll3_times1andhalf)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
random_list = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#8. Sort the list in #7 and print it.
random_list.sort(reverse=True)
print(random_list)
#9. Add together the highest three numbers in the list from #7 and print the result.
randListAdded = random_list[0] + random_list[1] + random_list[2]
print(randListAdded)
#10. Create a list with 5 names of other students in this class and print the list.
nameList = ["Jacob", "Cody", "Eden", "Brody", "Owyn"]
print(nameList)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(nameList)
print(nameList)
#12. Print a random choice from the list of names from #10.
print(random.choice(nameList))