import pandas as pd

# 1. Read the Excel file (the FloodArchive)
# We use pandas, which is a powerful tool for working with tables.
filename = 'data/floodarchive.xlsx'
print(f"Reading {filename}...")
df = pd.read_excel(filename)

# 2. Filter the data
# We look at the 'Country' column.
# We use .str.strip() because sometimes there's an accidental space at the end of the name.
# We then check if the name is exactly 'Ghana'.
ghana_floods = df[df['Country'].str.strip() == 'Ghana']

# 3. Save the result as a new CSV file
output_filename = 'data/ghana_flood_events.csv'
print(f"Found {len(ghana_floods)} events for Ghana. Saving to {output_filename}...")
ghana_floods.to_csv(output_filename, index=False)

print("Done! You can now open ghana_flood_events.csv.")
