def collatz(number):
    if number % 2 == 0:
        a = number // 2
        print(a)
        return a
    elif number % 2 == 1:
        b = 3 * number + 1
        print(b)
        return b
try:
    user_input = int(input("Enter a number: "))
    while user_input != 1:
        user_input = collatz(user_input)

except ValueError:
    print("Your input must be an integer")   

