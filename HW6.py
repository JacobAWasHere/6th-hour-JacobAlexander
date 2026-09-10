#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: HW6

print("hello world")
#1. Create a list with 9 different numbers inside.
big_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
#2. Sort the list from highest to lowest.
big_list.sort()
#3. Create an empty list.
nothing_burger_list = []
#4. Remove the median number from the first list and add it to the second list.
var1 = big_list.pop(4)
nothing_burger_list.append(var1)

#5. Remove the first number from the first list and add it to the second list.
var2 = big_list.pop(0)
nothing_burger_list.append(var2)
#6. Print both lists.
print(big_list)
print(nothing_burger_list)
#7. Add the two numbers in the second list together and print the result.
something_burger = nothing_burger_list[0] + nothing_burger_list[1]
print(something_burger)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
big_list.append(something_burger)
#9. Sort the first list from lowest to highest and print it.
big_list.sort()
print(big_list)