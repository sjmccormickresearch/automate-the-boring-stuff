# flow control statements can decide which instructions to execute under which conditions

# %%
print(42 == 42)
print(42 == 99)
print(2 != 3)


# %%
print('dog' == 'dog')
print('dog' == 'cat')

# %%
print(True and True)
print(True and False)

# %%
print(False or True)
print(False or False)
print(True or True)

# %%
print(not True)
print(not False)

# %%
print((4 < 5) and (5 < 6))
print((4 < 5) and (9 < 6))

# be careful with e.g.
print(4 < 5) and (9 < 6)
# need to wrap the whole boolean operator

# conditions followed by clauses
# same thing as expressions - conditions just more specific for flow control
# conditions always evaluate to a boolean value (true/false)
# a flow control statement decides what to do based on whether its true or false
# if this condition is true, do this thing, or else do this other thing
# or; keep repeating these instructions as long as this condition continues to be true

# BLOCKS
# a new block begins when the indentation increases
# blocks can contain other blocks
# a block ends when the indentation decreases to zero, or to a containing blocks indentation
# python expects a new block immediately after any statement that ends with a colon

# if, else, and elif
# the clause is the block following the if statement
# the block will execute if the statements condition is True, and skipped if False
# if statement can be read as: if this condition is true, execute the code in the clause

# %%

name = 'Alice'
if name == 'Alice':
    print('Hi Alice.')

##########
# basically: if 'name == 'Alice' evaluates to True, the clause runs.


# else
# the else clause is executed only when the if statements condition is False
# "if this condition is true, execute this code. or else execute that code.

# %%

name = 'Mike'
if name == 'Alice':
    print('Hello Alice')
else:
    print('Hello stranger')

#####
# use if or else when you only want one of the clauses to execute.
# but you might want 1 of many possible clauses to execute
# elif = elise if. always follows if or elif
# it provides another condition that is checked only if all of the previous conditions were False

# %%

name = 'Alice'
age = 33
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('Youre too young to be Alice')


# %%

name = 'Alice'
age = 2000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')


# %%

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')

# the rest of the elif statements are skipped once one is found to be true
# at most, only ONE of the clauses will be executed, and for elif statements, order matters

# %%

today_is_opposite_day = True

# Set say_it_is_opposite_day based on today_is_opposite_day:
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

# If it is opposite day, toggle say_it_is_opposite_day:
if today_is_opposite_day == True:
  say_it_is_opposite_day = not say_it_is_opposite_day

# Say what day it is:
if say_it_is_opposite_day == True:
    print('Today is Opposite Day.')
else:
    print('Today is not Opposite Day.')

###

# %%

print('Enter TB or GB for the advertised unit:')
unit = input('>')

# Calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)

##

# %%

spam = 1
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')