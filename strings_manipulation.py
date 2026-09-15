#formatting strings
age = 37
txt = f"Joe is a boy, he is {age} years old"
print(txt)

#modifying strings
#Making strings into upper case

b = "Ali is a boy"
print(b.upper())

#Making strings into lower case
m = "ADA IS A GIRL"
print(m.lower())

#removing white space
g = " you should go home now"
print(g.strip())

#replacing strings
v = "Hello, World"
print(v.replace("H", "Y"))


#Multiline Literal
print('''Dear Ada,

    Trust you are fine, you should remember your core always.

Yours,
Mercy.''')


#raw literal
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')


#multiline comment
"""This a multiline comment test
so i hope python compiler knows to ignore it.
Yeah! Just checking though."""

#slicing and indexing
hat = 'hello world'
print(hat[0])


#input
print('How are you')
feeling = input()
if feeling.lower == 'great':
    print('I feel great')
else:
    print('I hope the rest of your day is good')
