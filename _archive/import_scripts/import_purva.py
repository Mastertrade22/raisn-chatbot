"""
Import Purva projects from cost sheet based on semantic field mapping
"""

import pandas as pd
import sqlite3
import uuid
import re
from datetime import datetime

def clean_data(value):
    """Clean and normalize data values"""
    if pd.isna(value) or value == '' or str(value).strip() == '':
        return None
    return str(value).strip()

def parse_number(value):
    """Extract numeric value from string"""
    if pd.isna(value):
        return None
    try:
        # Remove commas and extract number
        value_str = str(value).replace(',', '').strip()
        numbers = re.findall(r'[\d.]+', value_str)
        if numbers:
            return float(numbers[0])
    except:
        pass
    return None

def semantic_field_mapping(df_columns):
    """
    Map Excel columns to database fields based on semantic similarity
    Returns mapping dictionary
    """

    # Define semantic mappings - flexible matching
    field_map = {}

    # Normalize column names
    columns_lower = [str(col).lower() for col in df_columns]

    # Project identification fields
    for i, col in enumerate(columns_lower):
        if 'project' in col and 'name' in col:
            field_map['project_name'] = df_columns[i]
        elif col in ['project', 'property name', 'name']:
            field_map['project_name'] = df_columns[i]
        elif 'location' in col or 'city' in col or 'area' in col:
            field_map['city'] = df_columns[i]
        elif 'configuration' in col or 'type' in col or 'bhk' in col:
            field_map['configuration'] = df_columns[i]
        elif 'carpet' in col and 'area' in col:
            field_map['carpet_area'] = df_columns[i]
        elif 'built' in col or 'super' in col or 'saleable' in col:
            field_map['built_up_area'] = df_columns[i]
        elif 'price' in col or 'cost' in col or 'rate' in col:
            if 'psf' in col or 'sqft' in col or 'sq.ft' in col:
                field_map['rate_per_sqft'] = df_columns[i]
            elif 'total' in col or 'basic' in col:
                field_map['base_price'] = df_columns[i]
        elif 'rera' in col:
            field_map['rera_number'] = df_columns[i]
        elif 'possession' in col or 'handover' in col or 'completion' in col:
            field_map['possession_date'] = df_columns[i]
        elif 'tower' in col or 'block' in col:
            field_map['towers'] = df_columns[i]
        elif 'unit' in col:
            field_map['units'] = df_columns[i]
        elif 'amenity' in col or 'amenities' in col:
            field_map['amenities'] = df_columns[i]
        elif 'usp' in col or 'highlight' in col or 'feature' in col:
            field_map['usp'] = df_columns[i]

    return field_map

def extract_project_from_recknor_sheet(df, sheet_name):
    """Extract project data from a Recknor sheet"""

    projects = []

    # Try to find project name from sheet name
    project_name = sheet_name.replace(' Recknor', '').replace('Recknor', '').replace('-', '').strip()

    # Map fields
    field_map = semantic_field_mapping(df.columns)

    # Look for project details in the sheet
    # Often the first few rows contain project-level info
    for idx, row in df.iterrows():
        # Skip empty rows
        if row.isna().all():
            continue

        # Extract unit-level data
        config = None
        carpet_area = None
        built_up = None
        rate_psf = None
        base_price = None

        for col in df.columns:
            col_lower = str(col).lower()
            value = row[col]

            if pd.notna(value):
                if 'bhk' in str(value).lower() or 'bedroom' in str(value).lower():
                    config = clean_data(value)
                elif 'carpet' in col_lower:
                    carpet_area = parse_number(value)
                elif 'built' in col_lower or 'super' in col_lower:
                    built_up = parse_number(value)
                elif 'rate' in col_lower and ('psf' in col_lower or 'sqft' in col_lower):
                    rate_psf = parse_number(value)
                elif 'price' in col_lower or 'cost' in col_lower:
                    base_price = parse_number(value)

        # If we found valid unit data, create entry
        if config and (built_up or carpet_area):
            projects.append({
                'project_name': project_name,
                'configuration': config,
                'built_up_area': built_up,
                'carpet_area': carpet_area,
                'rate_per_sqft': rate_psf,
                'base_price': base_price
            })

    return projects

def import_purva_projects(excel_path, db_path="real_estate_data.db"):
    """Import Purva projects from cost sheet"""

    print("📖 Reading Purva Excel file...")
    excel_file = pd.ExcelFile(excel_path)

    # Filter sheets that contain project data (Recknor sheets)
    recknor_sheets = [s for s in excel_file.sheet_names if 'Recknor' in s or 'Reckor' in s]

    print(f"✅ Found {len(recknor_sheets)} project sheets (Recknor/Reckor)")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Clear existing Purva projects
    print("🗑️  Clearing existing Purva projects...")
    cursor.execute("DELETE FROM project_units WHERE tenant_id = 'PURVA_001'")
    cursor.execute("DELETE FROM projects WHERE developer_name = 'Purva' OR tenant_id = 'PURVA_001'")
    conn.commit()

    inserted_projects = 0
    inserted_units = 0

    # Process each Recknor sheet
    for sheet_name in recknor_sheets:
        try:
            print(f"\n📄 Processing: {sheet_name}")
            df = pd.read_excel(excel_path, sheet_name=sheet_name)

            # Extract project name from sheet name
            project_name = sheet_name.replace(' Recknor', '').replace('Recknor', '').replace(' Reckor', '').replace('Reckor', '').replace('-', '').strip()

            # Get location from Script sheet if available
            script_sheet = sheet_name.replace('Recknor', 'Script').replace('Reckor', 'Script')
            location = None

            if script_sheet in excel_file.sheet_names:
                try:
                    script_df = pd.read_excel(excel_path, sheet_name=script_sheet)
                    # Look for location in script sheet
                    for col in script_df.columns:
                        if 'location' in str(col).lower():
                            location = clean_data(script_df[col].iloc[0])
                            break
                except:
                    pass

            # Generate project ID
            project_id = str(uuid.uuid4())[:8]

            # Insert project
            project_data = {
                'project_id': project_id,
                'tenant_id': 'PURVA_001',
                'project_name': f"Purva {project_name}",
                'developer_name': 'Purva',
                'city': location or 'Bangalore',  # Default to Bangalore if not found
                'description': f"Purva {project_name} project details",
            }

            columns = ', '.join(project_data.keys())
            placeholders = ', '.join(['?' for _ in project_data])
            query = f"INSERT INTO projects ({columns}) VALUES ({placeholders})"
            cursor.execute(query, list(project_data.values()))
            inserted_projects += 1

            # Process units from the Recknor sheet
            # Map columns semantically
            field_map = semantic_field_mapping(df.columns)

            for idx, row in df.iterrows():
                # Skip empty rows
                if row.isna().all():
                    continue

                # Try to extract unit data
                config = None
                built_up = None
                carpet_area = None
                rate_psf = None
                base_price = None

                # Look for configuration (BHK type)
                for col in df.columns:
                    val = str(row[col]).lower()
                    if 'bhk' in val and pd.notna(row[col]):
                        config = clean_data(row[col])
                        break

                # Extract areas and pricing using semantic mapping
                if 'configuration' in field_map:
                    config = config or clean_data(row[field_map['configuration']])
                if 'built_up_area' in field_map:
                    built_up = parse_number(row[field_map['built_up_area']])
                if 'carpet_area' in field_map:
                    carpet_area = parse_number(row[field_map['carpet_area']])
                if 'rate_per_sqft' in field_map:
                    rate_psf = parse_number(row[field_map['rate_per_sqft']])
                if 'base_price' in field_map:
                    base_price = parse_number(row[field_map['base_price']])

                # Insert unit if we have minimum required data
                if config and (built_up or carpet_area):
                    unit_data = {
                        'unit_id': str(uuid.uuid4())[:8],
                        'project_id': project_id,
                        'tenant_id': 'PURVA_001',
                        'configuration_type': config,
                        'property_type': 'Apartment',
                        'built_up_area_sqft': built_up,
                        'carpet_area_sqft': carpet_area,
                        'base_price': base_price,
                        'current_average_psf': rate_psf,
                        'market_psf': None
                    }

                    columns = ', '.join(unit_data.keys())
                    placeholders = ', '.join(['?' for _ in unit_data])
                    query = f"INSERT INTO project_units ({columns}) VALUES ({placeholders})"
                    cursor.execute(query, list(unit_data.values()))
                    inserted_units += 1

        except Exception as e:
            print(f"⚠️  Error processing {sheet_name}: {e}")

    conn.commit()
    conn.close()

    print(f"\n✅ Purva Import Complete!")
    print(f"   Projects inserted: {inserted_projects}")
    print(f"   Units inserted: {inserted_units}")

    return inserted_projects, inserted_units


if __name__ == "__main__":
    excel_path = "/Users/mudit/Downloads/Purva Cost Sheet as of 12th Dec'25.xlsx"
    db_path = "real_estate_data.db"

    print("🏗️  Starting Purva Projects Import...\n")
    projects, units = import_purva_projects(excel_path, db_path)

    print(f"\n📊 Database updated successfully!")
