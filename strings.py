# Multiline strings
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# Escape characters + multiline comments:
""" Escape characters
    \' single quote
    \" double quote
    \t tab
    \n newline - line break
    \\ backlash
"""

# Raw strings
print(r'That is Carol\'s cat.')
""" Because this is a raw string, Python considers the backslash as part of the string and 
 not as the start of an escape character. 
 Raw strings are helpful if you are typing string values that contain many backslashes, 
 such as the strings used for Windows file paths or regular expressions
"""

# in String count, the space is counted as well
spam = 'Hello, world!'
print("space: " + spam[6])

# String slice
fizz = spam[0:5]
print(fizz)

# String interpolation (%s) and {}
name = 'Al'
age = 4000
print('My name is %s. I am %s years old.' % (name, age))
print(f'My name is {name}. Next year I will be {age + 1}.')
