import pandas as pd
from sklearn.metrics import r2_score

# Part 1: Load the data.csv file into a pandas DataFrame
data = pd.read_csv('data.csv')

# Part 2: Calculate R-squared for NREL's model
def calculate_r_squared(group):
    actual = group["Solar Energy"]
    predicted = group["Energy Per Area"]
    return r2_score(actual, predicted)

r_squared_results = data.groupby(["County", "Sector Abbreviation"]).apply(calculate_r_squared, include_groups=False).reset_index(name="R_Squared")
print(r_squared_results)

# Part 3: Create and use a correlation matrix to determine which weather variables are most correlated with solar energy production
# Select relevant columns for correlation analysis
weather_columns = ["Solar Energy", "Temperature", "Humidity", "Precipitation", "Dew", "Precipitation Type", "Snow", "Cloud Cover", "Solar Radiation", "Visibility", "UV Index", "Conditions"]

# Convert categorical variables to one-hot encoded variables
data_encoded = pd.get_dummies(data[weather_columns], drop_first=True)

correlation_matrix = data_encoded.corr()
print(correlation_matrix["Solar Energy"].sort_values(ascending=False))
