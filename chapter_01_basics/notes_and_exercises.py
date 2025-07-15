"""pretty greeting (doc string)"""
print(__doc__)

spam = 42
print(spam)

eggs = 2

print(spam + eggs)

# string replication
print('Alice' * 5)

"""variables cant begin with a number"""
"""also can't be a python keyword (if, for)"""
"""variable names are case sensitive - spam sPaM and SPAM are 3 different variables"""

"""camelCase"""
"""snake_case"""
"""A Foolish Consistency Is the Hobgoblin of Little Minds"""

# program says hello and asks for your name
print('Hello,world')
print('what is your name?')
my_name = input('>')
print('hello, ' + my_name)
print('the length of your name is: ')
print(len(my_name))
print('what is your age?')
my_age = input('>')
print('you will be ' + str(int(my_age)+1) + ' in a year.')


