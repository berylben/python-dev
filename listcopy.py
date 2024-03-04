import copy
spam = ['A', 'B', 'C', 'D']


cheese = spam.copy()

# Keep the data type consistent
cheese[1] = '42'
print(spam)
print(cheese)