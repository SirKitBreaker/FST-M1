# Take list of numbers from user
numbers = list(input('Enter list of numbers separated by comma : ').split(","))
total = 0
# iterate through list
for number in numbers:
    if number.isnumeric():
        total += int(number)
    else:
        pass

print("Sum of all the numbers : ", total)
