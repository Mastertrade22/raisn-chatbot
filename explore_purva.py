"""
Explore Purva cost sheet structure
"""

import pandas as pd

def explore_purva_excel(excel_path):
    """Explore the Purva cost sheet structure"""

    print(f"📖 Reading Purva Excel file: {excel_path}\n")

    # Read all sheets
    excel_file = pd.ExcelFile(excel_path)
    print(f"📊 Available sheets ({len(excel_file.sheet_names)}):")
    for i, sheet in enumerate(excel_file.sheet_names, 1):
        print(f"  {i}. {sheet}")

    # Read first sheet to understand structure
    print(f"\n🔍 Exploring first sheet: '{excel_file.sheet_names[0]}'")
    df = pd.read_excel(excel_path, sheet_name=0)

    print(f"\n📋 Sheet has {len(df)} rows and {len(df.columns)} columns")
    print(f"\n📌 Column names:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")

    # Display first few rows
    print(f"\n🔍 First 5 rows of data:")
    print(df.head(5).to_string())

    # Check for additional sheets
    if len(excel_file.sheet_names) > 1:
        print(f"\n\n🔍 Exploring second sheet: '{excel_file.sheet_names[1]}'")
        df2 = pd.read_excel(excel_path, sheet_name=1)
        print(f"📋 Sheet has {len(df2)} rows and {len(df2.columns)} columns")
        print(f"\n📌 Column names:")
        for i, col in enumerate(df2.columns, 1):
            print(f"  {i}. {col}")
        print(f"\n🔍 First 3 rows:")
        print(df2.head(3).to_string())

    return excel_file.sheet_names


if __name__ == "__main__":
    excel_path = "/Users/mudit/Downloads/Purva Cost Sheet as of 12th Dec'25.xlsx"
    sheets = explore_purva_excel(excel_path)
