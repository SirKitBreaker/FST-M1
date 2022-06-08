# Given a list of numbers, return True if first and last number of a list is same

# Take input from user
numbers = list(input('Enter list of numbers separated by comma : ').split(","))
print("Your List : ", numbers)

first = numbers[0]
last = numbers[-1]

# check if first and last number is same
if first == last:
    print("First and last value is same")
else:
    print("First and last value is different")
