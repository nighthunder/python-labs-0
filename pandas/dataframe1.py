import pandas as pd

# Creating a DataFrame
data = {'Name': ['John', 'Mary', 'Alex', 'Jane'],
        'Age': [25, 28, 24, 27],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Printing the DataFrame
print(df)

# Accessing a column by name
print(df['Name'])

# Filtering the DataFrame based on a condition
filtered_df = df[df['Age'] > 25]
print(filtered_df)

# Grouping the DataFrame by a column and aggregating another column
grouped_df = df.groupby('City').agg({'Age': 'mean'})
print(grouped_df)
