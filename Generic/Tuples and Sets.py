'''
Tuples - Collection which is ordered and unchangeable.
'''
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[2])

# # Cannot remove or add elements

# for x in my_tuple:
#     print(x)

# print(len(my_tuple))


'''
Sets - collection similar to lists BUT UNORDERED

Lists are faster than Sets to iterate over the values

Sets are faster than Lists to search for an item - contains only unique values

Used mostly to remove and duplicates and check if an item exists
'''
my_set = {'apples', 'bananas', 'oranges', 'melons'}
new_set = {'grapes', 'plums', 'apples'}
# print(my_set)  # can print it any random order

# print('melonS' in my_set)  # case sensitive


# # Loop thorugh
# for x in my_set:
#     print(x)


# # Remove
# my_set.remove('grapes')  # throws KeyError if key doesn't exist
# my_set.discard('grapes')  # no response returned if key doesn't exist
# my_set.clear()

# # Return the difference of two or more sets as a new set. (i.e. all elements that are in this set but not the others.)
# print(new_set.difference(my_set)) # returns {'grapes', 'plums'} and excludes 'apples'

# # Remove all elements of another set from this set.
# my_set.difference_update(new_set) # 'apples' got removed from my_set
# print(my_set)
# print(new_set)

# # Union
# set_one = {1, 3, 5, 7, 9}
# set_two = {2, 4, 6, 8, 10}
# all_set = set_one.union(set_two)  # returns a combined set in asc order
# print(all_set)

# # Add
# my_set.add('pears')
# my_set.update(['mango', 'pumpkin'])
# print(my_set)
# print(len(my_set))
