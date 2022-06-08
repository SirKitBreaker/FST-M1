
import pandas as pd

data = pd.read_csv("User_Details.csv")
print("All the data :", data)
# fetch usernames
print("Usernames :", data["Username"])
# fetch 2nd row details
print("Username :", data["Username"][1], ", Password : ", data["Passwords"][1])
# sort on username
print("Sorted on Usernames :", data.sort_values("Username"))
# sort on passwords descending
print("Sorted on passwords descending :", data.sort_values("Passwords", ascending=False))



