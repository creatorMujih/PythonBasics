while True:
    print('Enter your age: ')
    age = input()
    if age .isdecimal():
        break
    print('Please enter a number for your age.')    

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if len(password) < 10:
        print('Password should be atleast 10 characters long')
    elif password .isalnum():
        break
    print('Password can only have numbers and letters.')
   
