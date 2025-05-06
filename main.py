import pandas as pd
from sklearn.metrics import r2_score

# Load the data.csv file into a pandas DataFrame
data = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(data.head())

def calculate_r_squared(group):
    actual = group["Solar Energy"]
    predicted = group["Energy Per Area"]
    return r2_score(actual, predicted)

r_squared_results = data.groupby(["County", "Sector Abbreviation"]).apply(calculate_r_squared).reset_index(name="R_Squared")
print(r_squared_results)
