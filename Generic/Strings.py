'''
Strings
'''

# concatination
# my_name = 'Eric'
# print(my_name + ' Roby')

# # Formats
# name = 'Eric'
# number = 8
# # Throws an error to avoid integer concat with string
# # print('I have '+number+' of shoes')

# # to concat integer conver to string
# print('I have '+str(number)+' number of shoes')

# # Instead we can concat with {} and format
# print('I have {} number of shoes'.format(str(number)))

# # using f strings - most commonly used way
# print(f'I have {str(number)} number of shoes')


'''
Useful String Methods
'''
# message = 'Welcome to strings class'

# print(message.upper())  # Converts all letters to upper case
# print(message.lower())  # Converts all letters to lower case
# # Changes the first character of the string to upper case
# print(message.capitalize())
# # Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.
# print(message.count('o'))
# print(message.endswith('s'))  # returns True or False - case sensitive
# print(message.startswith('w'))  # returns True or False - case sensitive
# print(message.isdigit()) # returns True or False - '500' returs True


'''
User Input
'''
# name = input('Enter your name - ')
# age = input('Enter your age - ') # Age will be of type str
# print(f'{name} is {age} years old.')


'''
Advances String Methods
'''
greetings = 'Welcome to python class'

# Indexing
# print(greetings[0]) # prints first character

# Slicing
# # prints characters from 0 to 6 as char at 7 will be excluded - returns a string
# print(greetings[0:7])
# # prints from 0 to 9 by skipping 2 positions (0,2,4,6,8) - returns a list
# print([greetings[0:10:2]])

# Length
# print(len(greetings))  # prints the length of the string

# Split
# print(greetings.split()) # returns list of words seperated by space.

# Find and return index
# print(greetings.find('p'))  # returns -1 if result not found - case sensitive

# Joins
# Concatenate any number of strings. The string whose method is called is inserted in between each given string.
# The result is returned as a new string. Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
# print(greetings, ','.join('abcdefg'))  # prints - Welcome to python class a,b,c,d,e,f,g

# Strip
# print(greetings.strip()) # Trims the string

# Repalce
# new_greetings = greetings.replace('Welcome to', 'Hello there, welcome to')
# print(new_greetings)
