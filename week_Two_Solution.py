#Step 1: Create an empty list called my_list
my_list = []

#Step 2: Append the elements 10, 20, 30 and 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Step 3: Insert the value 15 at the second position in the list (index 1)
my_list.insert(1, 15)

#Step 4: Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

#Step 5: Remove the last element form my_list
my_list.pop()

#Step 6: Sort my_list in scending order
my_list.sort()

print(my_list)