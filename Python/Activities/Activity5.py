# take number from user
num = input('Enter any number : ')
i = 1
# loop 10 times
if num.isnumeric():
    while i <= 10:
        print(num, " Multiply by ", i, " = ", int(num) * i)
        i += 1
else:
    print('Number is not entered, try again')
