import pandas
from pandas import ExcelWriter, DataFrame

# Create the dataset
data = {
    'FirstName': ["Satvik", "Avinash", "Lahri"],
    'LastName': ["Shah", "Kati", "Rath"],
    'Email': ["satshah@example.com", "avinashK@example.com", "lahri.rath@example.com"],
    'PhoneNumber': ["4537829158", "4892184058", "4528727830"]
}

# Convert dataset into a DataFrame
df = pandas.DataFrame(data)

# Write the data to the Excel file
writer = ExcelWriter("../inputs/users.xlsx")
df.to_excel(excel_writer=writer, sheet_name="users", index=False)
writer._save()  # Save the Excel file

# Read from the Excel file
users = pandas.read_excel("../inputs/users.xlsx", sheet_name="users")
print(users)

# Print the number of rows and columns
print("-----------------------")
print("No. of rows:", users.shape[0])
print("No. of columns:", users.shape[1])
# Print the data in the emails column only
print("-----------------------")
print(users["Email"])
# Sort the data based on FirstName in ascending order and print the data
print("-----------------------")
print(users.sort_values("FirstName"))
