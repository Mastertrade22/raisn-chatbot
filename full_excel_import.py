"""
Complete Excel import script for Casagrand projects
"""

import pandas as pd
import sqlite3
import uuid
from datetime import datetime

def clean_data(value):
    """Clean and normalize data values"""
    if pd.isna(value) or value == '' or str(value).strip() == '':
        return None
    return str(value).strip()

def parse_area(area_str):
    """Extract numeric area from strings like '2178 sq.ft'"""
    if pd.isna(area_str):
        return None
    try:
        # Extract numbers from string
        import re
        numbers = re.findall(r'[\d.]+', str(area_str))
        if numbers:
            return float(numbers[0])
    except:
        pass
    return None

def import_casagrand_projects(excel_path, db_path="real_estate_data.db"):
    """Import Casagrand projects from Excel to database"""

    print("📖 Reading Excel file...")

    # Read the main sheet with proper header row
    df = pd.read_excel(excel_path, sheet_name=0, header=0)

    # Skip the first row if it contains header labels
    if 'Project Name' in str(df.iloc[0].values):
        df = pd.read_excel(excel_path, sheet_name=0, header=1)

    print(f"✅ Found {len(df)} rows")

    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Clear existing Casagrand projects
    print("🗑️  Clearing existing Casagrand projects...")
    cursor.execute("DELETE FROM project_units WHERE tenant_id = 'TM_TEAM_001'")
    cursor.execute("DELETE FROM projects WHERE tenant_id = 'TM_TEAM_001'")
    conn.commit()

    inserted_projects = 0
    inserted_units = 0

    # Process each row
    for idx, row in df.iterrows():
        # Skip rows without project name
        project_name = clean_data(row.get('Project Name') or row.get('Unnamed: 1'))
        if not project_name or project_name == 'NaN':
            continue

        location = clean_data(row.get('Location') or row.get('Unnamed: 2'))
        if not location:
            continue

        # Generate unique project ID
        project_id = str(uuid.uuid4())[:8]

        # Extract project data
        project_data = {
            'project_id': project_id,
            'tenant_id': 'TM_TEAM_001',
            'project_name': project_name,
            'developer_name': 'Casagrand',
            'city': location,
            'description': clean_data(row.get('Offers Details') or row.get('Unnamed: 4')),
            'total_project_area_acres': parse_area(row.get('Total Land Extent') or row.get('Unnamed: 37')),
            'number_of_towers': None,
            'total_units_count': clean_data(row.get('No of Units') or row.get('Unnamed: 5')),
            'tower_structure_details': clean_data(row.get('Floor') or row.get('Unnamed: 7')),
            'rera_registration_number': clean_data(row.get('RERA Project Registration No') or row.get('Unnamed: 44')),
            'approval_body': clean_data(row.get('Approval') or row.get('Unnamed: 34')),
            'launch_date': None,
            'estimated_possession_date': clean_data(row.get('Completion Date') or row.get('Unnamed: 38')),
            'amenities': clean_data(row.get('Amenities') or row.get('Unnamed: 33')),
            'unique_selling_propositions': clean_data(row.get("Unique selling Proportion (USP's)") or row.get('Unnamed: 40')),
            'project_theme': clean_data(row.get('Theme') or row.get('Unnamed: 45')),
            'nearby_top_places': clean_data(row.get('Landmark') or row.get('Unnamed: 4'))
        }

        try:
            # Insert project
            columns = ', '.join(project_data.keys())
            placeholders = ', '.join(['?' for _ in project_data])
            query = f"INSERT INTO projects ({columns}) VALUES ({placeholders})"
            cursor.execute(query, list(project_data.values()))
            inserted_projects += 1

            # Extract unit data if available
            bhk = clean_data(row.get('BHK') or row.get('Unnamed: 10'))
            built_up = parse_area(row.get('Built up Area') or row.get('Unnamed: 12'))
            carpet_area = parse_area(row.get('Carpet Area') or row.get('Unnamed: 39'))
            basic_cost = clean_data(row.get('Basic Cost') or row.get('Unnamed: 20'))
            rate_per_sqft = clean_data(row.get('Actual Rate per Sqft') or row.get('Unnamed: 17'))

            if bhk and built_up:
                unit_data = {
                    'unit_id': str(uuid.uuid4())[:8],
                    'project_id': project_id,
                    'tenant_id': 'TM_TEAM_001',
                    'configuration_type': bhk,
                    'property_type': clean_data(row.get('Type') or row.get('Unnamed: 6')) or 'Apartment',
                    'built_up_area_sqft': built_up,
                    'carpet_area_sqft': carpet_area,
                    'base_price': None,
                    'current_average_psf': parse_area(rate_per_sqft),
                    'market_psf': None,
                    'current_festive_offers': clean_data(row.get('Offer') or row.get('Unnamed: 3'))
                }

                columns = ', '.join(unit_data.keys())
                placeholders = ', '.join(['?' for _ in unit_data])
                query = f"INSERT INTO project_units ({columns}) VALUES ({placeholders})"
                cursor.execute(query, list(unit_data.values()))
                inserted_units += 1

        except sqlite3.IntegrityError as e:
            print(f"⚠️  Skipping duplicate: {project_name} - {e}")
        except Exception as e:
            print(f"❌ Error inserting {project_name}: {e}")

    conn.commit()
    conn.close()

    print(f"\n✅ Import Complete!")
    print(f"   Projects inserted: {inserted_projects}")
    print(f"   Units inserted: {inserted_units}")

    return inserted_projects, inserted_units


if __name__ == "__main__":
    excel_path = "/Users/mudit/Downloads/READY RECKONER - TM Team.xlsx"
    db_path = "real_estate_data.db"

    print("🏗️  Starting Casagrand Projects Import...\n")
    projects, units = import_casagrand_projects(excel_path, db_path)

    print(f"\n📊 Database updated successfully!")
