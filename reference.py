import random

messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']
print(messages[random.randint(2, len(messages) - 1)])

print('Four score and seven ' + \
'years ago...')

a = tuple(['rat', 'mice', 'toad'])
print(a)


#Reference (checking strings and ints against lists)
a = 42
b = a
a = 50
print(a)
print(b)

v = [1, 2, 3, 4, 5]
m = v.copy()
v[1] = 'ant'
m.append(6)
print(v)
print(m)