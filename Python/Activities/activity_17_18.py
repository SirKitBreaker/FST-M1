import pandas as pd

# Create a dataset
data = {
    "usernames": ["admin", "Charles", "Deku"],
    "passwords": ["password", "Charl13", "AllMight"]
}

# Convert the dataset in to a DataFrame
df = pd.DataFrame(data)

# Write to the CSV file
df.to_csv("../inputs/creds.csv", index=False)

# Read from the CSV file
creds = pd.read_csv("../inputs/creds.csv")
print(creds)

# Print the values only in the Usernames column
print("-----------------------------------")
print(creds["usernames"])
# Print the username and password of the second row
print("-----------------------------------")
print("Username:", creds["usernames"][1], "| Password:", creds["passwords"][1])
# Sort the Usernames column data in ascending order and print data
print("-----------------------------------")
print(creds.sort_values("usernames", ascending=True))
# Sort the Passwords column in descending order and print data
print("-----------------------------------")
print(creds.sort_values("passwords", ascending=False))
