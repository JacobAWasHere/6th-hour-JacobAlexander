#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
dictionary = {"name":"Jacob",
              "age":14,
              "something":[2763, 777, 67]}
#3. Print the keys of the dictionary from #2.
print(dictionary.keys)
#4. Print the values of the dictionary from #2
print(dictionary.values)
#5. Print one of the three numbers from the list by itself
print(dictionary["something"][0])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
dictionary.update({"grade":9})
#7. Print the entire dictionary from #2 with the updated key and value.
print(dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
friends = {
    "eli":
        {"lastName": "laney",
         "grade":9},
    "wyatt": {"lastName": "toler",
              "grade": 8},
    "cody": {"lastName": "obama?",
             "grade": 9}}
#9. Print the names of all three classmates on the same line.
print(friends.keys())
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
friends.pop("cody")
print(friends)