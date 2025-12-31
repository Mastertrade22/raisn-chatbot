"""
Inspect a specific Purva Recknor sheet to understand structure
"""

import pandas as pd

excel_path = "/Users/mudit/Downloads/Purva Cost Sheet as of 12th Dec'25.xlsx"

# Look at Grand Bay Recknor in detail
sheet_name = "Grand Bay Recknor"

print(f"🔍 Inspecting: {sheet_name}\n")

df = pd.read_excel(excel_path, sheet_name=sheet_name)

print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns\n")

print("Column names:")
for i, col in enumerate(df.columns):
    print(f"  {i}: {col}")

print("\n" + "="*80)
print("Full data preview (first 15 rows):")
print("="*80)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
print(df.head(15).to_string())

print("\n" + "="*80)
print("Looking for BHK/configuration data:")
print("="*80)

for idx, row in df.iterrows():
    row_str = ' '.join([str(val) for val in row.values if pd.notna(val)])
    if 'BHK' in row_str.upper() or 'BEDROOM' in row_str.upper():
        print(f"Row {idx}: {row.to_dict()}")

print("\n" + "="*80)
print("Another sheet - Atmosphere Recknor:")
print("="*80)

df2 = pd.read_excel(excel_path, sheet_name="Atmosphere Recknor")
print(f"Shape: {df2.shape[0]} rows x {df2.shape[1]} columns\n")
print("Columns:", df2.columns.tolist())
print("\nFirst 10 rows:")
print(df2.head(10).to_string())
