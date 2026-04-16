import pandas as pd

# Mapping of PCODE to District Name for Rwanda Eastern Province
DISTRICT_MAPPING = {
    'RW51': 'Rwamagana',
    'RW52': 'Nyagatare',
    'RW53': 'Gatsibo',
    'RW54': 'Kayonza',
    'RW55': 'Kirehe',
    'RW56': 'Ngoma',
    'RW57': 'Bugesera'
}

def filter_data():
    filename = 'data/rwa_rainfall_5ytd.csv'
    print(f"Reading {filename}...")
    df = pd.read_excel(filename) if filename.endswith('.xlsx') else pd.read_csv(filename)

    # Filter for the specific PCODEs in Eastern Province
    print("Filtering for Eastern Province districts...")
    eastern_df = df[df['PCODE'].isin(DISTRICT_MAPPING.keys())].copy()

    # Add the district name column
    eastern_df['district_name'] = eastern_df['PCODE'].map(DISTRICT_MAPPING)

    output_filename = 'data/eastern_province_drought.csv'
    print(f"Saving filtered data to {output_filename}...")
    eastern_df.to_csv(output_filename, index=False)
    print("Done!")

if __name__ == "__main__":
    filter_data()
