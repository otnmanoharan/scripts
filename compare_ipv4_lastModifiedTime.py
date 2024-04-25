import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('ipv4_list.csv')

# Assuming 'ip_address' is the column with IP addresses and 'value' is the column with integer values
# Group by 'ip_address' and get the row with the max 'value' for each group
result = df.loc[df.groupby('indicator_value')['last_modified_time'].idxmax()]

# Save the result to a new CSV file
result.to_csv('filtered_list.csv', index=False)
