# https://automatetheboringstuff.com/3e/chapter3.html
# while and for

"""you can make a block of code execute over and over again using a while statement.
The code in a while clause will be executed as long as the statement's condition is True.
In code, a while statement always consists of: the while keyword, a condition, a colon, and then followed by an indented block."""

"""At the end of an if clause, the program execution continues after the if statement. At the end of a while clause, 
the program jumps back to the start of the while statement."""

# %%
spam = 0
if spam < 5:
    print('Hello, world')
    spam = spam + 1


# %%
spam = 0
while spam < 5:
    print(spam)
    print('Hello, world')
    spam = spam + 1
    print(spam)

# %%
name = ''
while name != 'Steven':
    print('Please type your name.')
    name = input('>')
print('Thank You!')

# %%
