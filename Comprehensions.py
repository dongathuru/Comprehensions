# List Comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#
my_list = [n for n in nums]
print(my_list)

#
my_list = [n * n for n in nums]
print(my_list)

# Using maps and lambda to do above
my_list = list(map(lambda n: n * n, nums))
print(my_list)

# List comprehensions do away with functions because they are easier
# to read especially if don't know about the actual functions.

#
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# Using filter and lambda to do above
my_list = list(filter(lambda n: n % 2 == 0, nums))
print(my_list)

#
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

print(list(zip(names, heroes)))  # Produces list of tuples

my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

# Its easy to add restrictions at the end of these Comprehensions e.g. :
# the comprehension above (If name is not equal to Peter)
my_dict = {name: hero for name, hero in zip(names, heroes)
           if name != 'Peter'}
print(my_dict)

# Set Comprehensions
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = {n for n in nums}
print(my_set)

# Generator expressions
# A generator expression is so similar to a list comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def gen_func(nums):
    for n in nums:
        yield n * n

my_gen = gen_func(nums)

for n in my_gen:
    print(n)

# Now for the actual generator expression
my_gen = (n * n for n in nums)

for i in my_gen:
    print(i)