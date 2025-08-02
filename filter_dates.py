import pandas as pd

# Load the CSV file
df = pd.read_csv("data/Dish.csv")  # Replace with your actual filename

# Convert year columns to numeric, coercing errors to NaN
df['first_appeared'] = pd.to_numeric(df['first_appeared'], errors='coerce')
df['last_appeared'] = pd.to_numeric(df['last_appeared'], errors='coerce')

# Define the valid range
valid_start = 1840
valid_end = 2025

# Filter rows where both years are within the valid range
filtered_df = df[
    (df['first_appeared'].between(valid_start, valid_end)) &
    (df['last_appeared'].between(valid_start, valid_end))
]

# Save the cleaned data to a new CSV
filtered_df.to_csv("intermediate_data/Dish_clean_dates.csv", index=False)
