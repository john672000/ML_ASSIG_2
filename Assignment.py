import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('data.csv')

# Step 2: Show basic statistical description
description = df.describe()
print(description)

# Step 3: Check for null values and replace with mean
has_null = df.isnull().sum().any()
if has_null:
    df.fillna(df.mean(), inplace=True)

print("Checking the Mean Values: ", df.mean())
print("checking to see if it actually replaced the null with mean: ")
print(df.iloc[19-2])

# Step 4: Aggregate data using min, max, count, mean
columns_to_aggregate = ['Pulse', 'Maxpulse']
aggregations = {
    'min_value': df[columns_to_aggregate].min(),
    'max_value': df[columns_to_aggregate].max(),
    'count': df[columns_to_aggregate].count(),
    'mean': df[columns_to_aggregate].mean()
}
aggregated_data = pd.DataFrame(aggregations)
print(aggregated_data)

# Step 5: Filter rows with calories between 500 and 1000
print("\nRows with calories between 500 and 1000 are : \n")
filtered_data1 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]
print(filtered_data1)

# Step 6: Filter rows with calories > 500 and pulse < 100
print("\nRows with calories > 500 and pulse < 100 are : \n")
filtered_data2 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print(filtered_data2)

# Step 7: Create new dataframe without "Maxpulse" column
print("\n New dataframe without Maxpluse: \n")
df_modified = df.drop('Maxpulse', axis=1)
print(df_modified)

# Step 8: Delete "Maxpulse" column from the main dataframe
df.drop('Maxpulse', axis=1, inplace=True)

# Step 9: Convert Calories column to int datatype
df['Calories'] = df['Calories'].astype(int)

# Step 10: Create scatter plot for Duration and Calories

print("PLOT: ")
plot = df.plot.scatter(x='Duration', y='Calories')

# Display the modified dataframes and plots
print(df_modified.head())
print(filtered_data1.head())
print(filtered_data2.head())