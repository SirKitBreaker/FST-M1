# Create a Python dictionary that contains a bunch of fruits and their prices.
# Write a program that checks if a certain fruit is available or not.

# create a dictionary
fruits = {
    "Apple": 150,
    "Banana": 50,
    "Musk Melon": 75,
    "Orange": 100,
    "Mango": 300

}

search = input("What fruit you want ? ").capitalize()
# check if fruit is there in dict
if search in fruits:
    print("Congrats !! we have it and price is :", fruits.get(search))
else:
    print("Sorry we don't have it, we only have these fruits : ", fruits)
