# Take name and age from user
name = input('Enter your name : ')
age = input('Enter your age : ')

# calculate year
turn_year = (2022 - int(age)) + 100
print(name + ' will turn 100 in ' + str(turn_year))
