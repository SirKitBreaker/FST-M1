# Given a tuple of numbers, iterate through it and print only those numbers which are divisible by 5

# take input from user
numbers = tuple(input("Enter numbers separated by comma : ").split(","))

print("Your List : ", numbers)

# iterate through tuple and check if divisible by 5
print("Numbers divisible by 5 : ")
for number in numbers:
    if number.isnumeric():
        if int(number) % 5 == 0:
            print(number)
    else:
        pass

