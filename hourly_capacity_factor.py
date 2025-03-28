import pandas as pd
import numpy as np
import sys

df = pd.read_csv('dSTAC_US.csv')
print(df.info())
print(type(df['hourly_capacity_factor'][0]))
print(len(df["hourly_capacity_factor"][0].split(",")))
sys.exit()
# df = df.sample(500)

# Access the 0th index array
hourly_cf = np.array(eval(df['hourly_capacity_factor'][0])) / float(df['hourly_capacity_factor_scalar'][0])

# Access all arrays
df['hourly_cf'] = df.apply(lambda x: np.array(eval(x.hourly_capacity_factor))/ float(x.hourly_capacity_factor_scalar), axis=1)

print(df.head())

print(df[df["state_abbr"] == "IL"])
