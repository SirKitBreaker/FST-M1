# Write a recursive function to calculate the sum of numbers from 0 to 10

def total(num):
    if num == 0:
        return 0
    else:
        return num + total(num - 1)


# call function total
print("Total : ", total(10))
