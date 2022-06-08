# Take input from user
# num = int(input('Enter any number : '))
# Check if number is even or odd

num = input('Enter any number : ')
if num.isnumeric():
    if int(num) % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')

else:
    print("Enter a number not alphabets :")

