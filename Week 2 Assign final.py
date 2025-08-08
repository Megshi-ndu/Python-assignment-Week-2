# My_list is the python data structures assignment for week 2
My_list = [10]
My_list.append(20)
My_list.append(30)
My_list.append(40)
print("My_list", My_list)
#Output: My_list [10, 20, 30, 40]
# My_list is now a list with four elements
My_list.insert(1, 15)
print("My list", My_list)
#Output: My list [10, 15, 20, 30, 40]
My_list.append(50)
My_list.append(60)
My_list.append(70)
print("My list", My_list)
#Output: My list [10, 20, 30, 40,50, 60, 70]
# My_list now has seven elements
My_list.pop(7)
print("My list", My_list)
#Output: My list [10, 15, 20, 30, 40, 50, 60]
# The pop method does not take an element value, it takes an index
My_list.sort()
print("My list", My_list)
#Output: My list [10, 15, 20, 30, 40, 50, 60]
# The sort method sorts the list in ascending order
My_list.index(30)
print("Index of 30 in My_list:", My_list.index(30))
#Output: Index of 30 in My_list: 3