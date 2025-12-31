"""
Import projects data from Excel spreadsheet to SQLite database
"""

import pandas as pd
import sqlite3
import json
from datetime import datetime

def import_excel_to_db(excel_path, db_path="real_estate_data.db"):
    """Import project data from Excel to database"""

    print(f"📖 Reading Excel file: {excel_path}")

    # Read all sheets from the Excel file
    excel_file = pd.ExcelFile(excel_path)
    print(f"📊 Available sheets: {excel_file.sheet_names}")

    # Read the first sheet (or you can specify which sheet to read)
    df = pd.read_excel(excel_path, sheet_name=0)

    print(f"\n📋 Sheet has {len(df)} rows and {len(df.columns)} columns")
    print(f"\n📌 Column names:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")

    # Display first few rows to understand the data structure
    print(f"\n🔍 First 3 rows of data:")
    print(df.head(3).to_string())

    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get existing column names from projects table
    cursor.execute("PRAGMA table_info(projects)")
    db_columns = [row[1] for row in cursor.fetchall()]
    print(f"\n💾 Database columns available:")
    for col in db_columns[:10]:
        print(f"  - {col}")

    conn.close()

    print("\n✅ Excel file read successfully!")
    print(f"\n⏳ Ready to map and import data...")

    return df, excel_file.sheet_names


if __name__ == "__main__":
    excel_path = "/Users/mudit/Downloads/READY RECKONER - TM Team.xlsx"
    df, sheets = import_excel_to_db(excel_path)
