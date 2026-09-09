#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!
print("hello world")
#1. Create a list with 5 strings containing 5 different names in it.
name_list = ["Jacob", "Eli", "Dayson", "Joy", "Wyatt"]
#2. Append a new name onto the Name List.
name_list.append("Landon")
#3. Print out the 4th name on the list.
print(name_list[3])
#4. Create a list with 4 different integers in it.
numb_list = [42, 69, 777, 2763]
#5. Insert a new integer into the 2nd spot and print the new list.
numb_list.insert(1, 670)
print(numb_list)
#6. Sort the list from lowest to highest and print the sorted list.
numb_list.sort()
print(numb_list)
#7. Add the 1st three numbers on the sorted list together and print the sum.
numbList_add = numb_list[0] + numb_list[1] + numb_list[2]
print(numbList_add)
#8. Create a list with two strings, two variables, and two boolean values.
two_of_all_list = ["green", "blue", 42, 90, False, True]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
two_of_all_list.append(input("what do we add to the list?"))
print(two_of_all_list)