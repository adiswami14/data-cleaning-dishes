import pandas as pd

# Load the CSV file
df = pd.read_csv("intermediate_data/Dish_cleaned_with_ic.csv")  # Replace with your actual filename

# Convert year columns to numeric, coercing errors to NaN
df['first_appeared'] = pd.to_numeric(df['first_appeared'], errors='coerce')
df['last_appeared'] = pd.to_numeric(df['last_appeared'], errors='coerce')
df['menus_appeared'] = pd.to_numeric(df['menus_appeared'], errors='coerce')
df['times_appeared'] = pd.to_numeric(df['times_appeared'], errors='coerce')
df['lowest_price'] = pd.to_numeric(df['lowest_price'], errors='coerce')
df['highest_price'] = pd.to_numeric(df['highest_price'], errors='coerce')

# Define the valid range
valid_start = 1840
valid_end = 2025

# Filter rows where both years are within the valid range
filtered_df = df[
    (df['first_appeared'].between(valid_start, valid_end)) &
    (df['last_appeared'].between(valid_start, valid_end))
]

filtered_df = filtered_df[filtered_df['menus_appeared'] <= filtered_df['times_appeared']]
filtered_df = filtered_df[filtered_df['lowest_price'] <= filtered_df['highest_price']]
filtered_df = filtered_df.drop_duplicates(subset=['name'], keep='first')

# Save the cleaned data to a new CSV
filtered_df.to_csv("clean/Dish_clean.csv", index=False)
