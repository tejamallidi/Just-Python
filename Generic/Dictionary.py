'''
Dictionary
'''

user_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'year_of_birth': 1990
}

# # Throws a KeyError if the key doesn't exist
# print(user_dict['first_name'])
# print(user_dict.get('last_name'))

# # Add a key value
# user_dict['major'] = 'math' or user_dict.update({'major': 'math'})
# print(user_dict)

# # Length
# print(len(user_dict))

# Remove
# user_dict.pop('major')
# user_dict.popitem() # Deletes the last item
# del user_dict['year_of_birth']  # Deletes the key - year_of_birth
# del user_dict  # Deletes the dictionary
# user_dict.clear() # Clears the contents of the dictionary and makes it empty
# print(user_dict)


# Loops
# for k in user_dict:
#     print(k)  # prints all keys of the dictionary

# for k, v in user_dict.items():
#     print(k, v)  # prints all keys and values of the dictionary

# # To check if a key exists in a dict
# if 'year_of_birth' in user_dict:
#     print('yob exists')

# # To check if a value exists in a dict
# if 'Doe' in user_dict.values():
#     print('Doe exists')


# # Copy
# dict2 = user_dict.copy() dict(user_dict)


# Nested Dictionary
family = {
    'child1': {
        'first_name': 'John',
        'last_name': 'Doe',
        'year_of_birth': 1990
    },
    'child2': {
        'first_name': 'Peter',
        'last_name': 'Parker',
        'year_of_birth': 1993
    }
}
print(family)
