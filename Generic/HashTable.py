'''
Jan 1	27
Jan 2	31
Jan 3	23
Jan 4	34
Jan 5	37
Jan 6	38
Jan 7	29
Jan 8	30
Jan 9	35
Jan 10	30

What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
'''
temps = {'Jan 1': 27,
         'Jan 2': 31,
         'Jan 3': 23,
         'Jan 4': 34,
         'Jan 5': 37,
         'Jan 6': 38,
         'Jan 7': 29,
         'Jan 8': 30,
         'Jan 9': 35,
         'Jan 10': 30
         }
temps_total = 0
max_temp = 0
for i in range(len(temps)):
    if temps.get('Jan {}'.format(str(i+1))) > max_temp:
        max_temp = temps.get('Jan {}'.format(str(i+1)))
    if i+1 <= 7:
        temps_total += temps.get('Jan {}'.format(str(i+1)))


print(temps_total / 7)
print(max_temp)

'''
Best approach is to choose list
'''
arr = [27, 31, 23, 34, 37, 38, 29, 30, 35, 30]

print(sum(arr[0:7])/len(arr[0:7]))
print(max(arr[0:10]))


'''
poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
You have to read this file in python and print every word and its count as show below.
Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
'''
poem_list = []
poem_map = {}
with open('C:/Users/tejam/Documents/Just Python/poem.txt', 'r') as txtfile:
    poem_list = txtfile.readlines()
poem = ''.join(poem_list)
poem_split = poem.replace(',', '').replace(
    '\n', '').replace('.', ' ').split(' ')
for p in poem_split:
    p_pro = p.strip()
    if len(p_pro) > 0:
        if poem_map.get(p_pro) is None:
            poem_map[p_pro] = 1
        else:
            poem_map[p_pro] = poem_map.get(p_pro)+1
print(poem_map)

# or
word_count = {}
with open('C:/Users/tejam/Documents/Just Python/poem.txt', 'r') as txtfile:
    for line in txtfile:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n', '')
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1
print(word_count)
