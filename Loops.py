'''
For loops
'''
# my_list = [2, 2, 3, 4, 5, 6, 7]
# for i in range(len(my_list)):
#     # prints element at ith index till the len(my_list) is reached
#     print(my_list[i])

# for element in my_list:
#     print(element)  # prints each element one after another

# for element in my_list:
#     if element == 5:
#         # break # Stops the execution at element 5
#         continue # Skips the execution at element 5 and continue to next element
#     print(element)

'''
while loop
'''
# x = 0
# while x < 10:
#     print(x)  # This will end up in infinte loop as 'x' is not changing.

# while x < 10:
#     print(x)
#     x += 1


'''
Write a program to print the numbers from 1 to 50
But for multiples of 3 print 'Fizz' instead of the number and
for multiples of 5 print 'Buzz'. For multiples of both 3 and 5 print 'FizzBuzz'
'''

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
