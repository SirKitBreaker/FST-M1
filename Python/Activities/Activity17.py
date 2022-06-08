# import pandas
import pandas as pd

# Create a dictionary to hold our data
data = {
    "Username": ["admin", "Charles", "Deku"],
    "Passwords": ["password", "Charl13", "AllMight"]
}

# Create a new DataFrame using our dictionary
table = pd.DataFrame(data)
print(table)

# write to CSV file
table.to_csv("User_Details.csv", index=False)
