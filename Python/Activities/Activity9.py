# Given a two list of numbers create a new list such that
# new list should contain only odd numbers from the first list and
# even numbers from the second list

list1 = [1, 5, 2, 8, 9, 4]
list2 = [11, 22, 33, 66, 99, 55]

print("First List : ", list1)
print("Second List : ", list2)

new_list = []
# add numbers from list1 to new_list if odd
for num in list1:
    if num % 2 != 0:
        new_list.append(num)

# add numbers from list1 to new_list if even
for num in list2:
    if num % 2 == 0:
        new_list.append(num)

# print the new list
print("New list is : ", new_list)
