import pandas

# read excel using pandas and store as dataframe
dataframe = pandas.read_excel("userData.xlsx", sheet_name="Sheet1")

# get rows and columns using shape method
print("Number of rows and columns : ", dataframe.shape)

# get data in email column

print("List of Emails : \n", dataframe['Email'])

# sort the data on FirstName
print("\nValues sorted on FirstName : ")
print(dataframe.sort_values("FirstName"))


