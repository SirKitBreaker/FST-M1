# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.

def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


count = input("How many Fibonacci numbers you need ? ")

if count.isnumeric():
    # generate list of numbers
    for i in range(int(count)):
        print(fibonacci(i))
else:
    print("Please enter a number :")
