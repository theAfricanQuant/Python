# list comprehensions
# basic format: new_list = [transform sequence [filter] ]
import random

under_10 = list(range(10))
print(f'under_10: {under_10}')

squares = [x**2 for x in under_10]
print(f'squares: {squares}')

odds =  [x for x in range(10) if x%2 == 1]
print(f'odds: {odds}')

ten_x = [x * 10 for x in range(10)]
print(f'ten_x: {ten_x}')

# get all numbers from a string
s = 'I love 2 go t0 the store 7 times a w3ek.'
nums = [x for x in s if x.isnumeric()]
print('nums: ' + ''.join(nums))

# get index of a list item
names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
idx = [k for k, v in enumerate(names) if v == 'Anu']
print(f'index = {str(idx[0])}')

# delete an item from a list
letters = list('ABCDEF')
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print(letters, letrs)

# if-else condition in a comprehension (must come before iteration)
nums = [5, 3, 10, 18, 6, 7]
new_list = [x if x%2 == 0 else 10*x for x in nums]
print(f'new list: {new_list}')

# nested loop iteration for 2D list
a = [[1,2],[3,4]]
new_list = [x for b in a for x in b]
print(new_list)

