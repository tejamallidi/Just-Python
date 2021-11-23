# my_list = []
# try:
#     print(my_list[-1])  # Throws index out of range as empty list
# except IndexError as e:
#     print(e)
# len(my_list)  # Gives the length of list

'''
Slicing lists
'''
# my_list = [6, 7, 8, 9]
# # creates a new list with elements in index 0,1 (excludes upper bound)
# print(my_list[0:2])
# print(my_list[0:])  # prints everything from 0th index
# print(my_list[0:3:2])  # print from 0-3 by incrementing 2 positions

'''
Add, Delete, Sort and Reverse elements in a list
'''
# my_list = [2, 4, 5, 6, 7, 8, 9]
# my_list.append(10)  # Adds at the end of the list
# my_list.insert(1, 3)  # Inserts at index 1
# # Removes the element, if that element doesn't exist - throws ValueError
# my_list.remove(9)
# # Removes last element by default. if we give an index, it will remove the element in that index
# my_list.pop(1)
# my_list.reverse()  # Reverses a list
# my_list.sort()  # Sorts the list
# print(my_list)


'''
Nested lists
'''
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Prints the first element ([4,5,6] - list) of nested_list
print(nested_list[1])
# Prints the second element of first element of nested_list
print(nested_list[1][2])
