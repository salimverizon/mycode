first_list = ["eggs", "bacon" , "milk", "butter", "bread", "cheddar", 5 , 2.37]
# identify -
print(first_list)
print(first_list[3])
print(first_list[3], first_list[5])
print("I need to get {}, {}, {}, {}, {}, and {} before {}. It  will be more then ${}. ".format(*first_list))

# reorder s list
print(" I need to get {1}, {5}, {3}, {2}, {0}, and {4} before {6}, it will be more then ${7}.".format(*first_list))

new_list = ["cat" , "dog" , "hamster"]
print(new_list[2])

new_list.append("squirrel")
print(new_list)

new_list.insert(1, "marmot")
print(new_list)
new_list.replace(1,"weasel")
print(new_list)

new_list[1] = "weasel"
print(new_list)

new_list.append(first_list)
print(new_list)

print(new_list[5][3])

new_list.extend("sasquatch")


for_realz = ["sasquatch" , "yeti" , "bigfoot"]

new_list.extend(for_realz)
print(new_list)


