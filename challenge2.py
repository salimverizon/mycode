my_list = ["10.10.10.25", "10,10.24.47", "10.20.30.40"]

print("I need to access IP's {0}, {2}, {1} " .format(*my_list))

print(f"I need to access IP's {my_list[0]}, {my_list[2]}, {my_list[1]}")
