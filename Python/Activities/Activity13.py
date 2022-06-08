# Write a function sum() such that it can accept a list of elements and print the sum of all elements

def sum(numbers):
    total = 0
    for num in numbers:
        if num.isnumeric():
            total = total + int(num)
        else:
            pass
    return total


num_list = list(input("Enter numbers separated by comma : ").split(","))
print("Your list : ", num_list)
print("Sum of all the numbers in list : ", sum(num_list))
