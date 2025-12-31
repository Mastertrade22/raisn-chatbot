"""
Import Purva projects from cost sheet - improved version with key-value parsing
"""

import pandas as pd
import sqlite3
import uuid
import re

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
        value_str = str(value).replace(',', '').strip()
        numbers = re.findall(r'[\d.]+', value_str)
        if numbers:
            return float(numbers[0])
    except:
        pass
    return None

def extract_project_data(df, project_name):
    """Extract project and unit data from Recknor sheet"""

    project_info = {
        'land_area': None,
        'total_units': None,
        'floors': None,
        'blocks': None,
        'carpet_percentage': None,
        'approval': None,
        'location': None,
        'rera': None
    }

    units = []

    # Parse key-value pairs
    for idx, row in df.iterrows():
        key = clean_data(row.iloc[1]) if len(row) > 1 else None
        value = clean_data(row.iloc[2]) if len(row) > 2 else None

        if not key:
            continue

        key_lower = key.lower()

        # Extract project-level information
        if 'land area' in key_lower:
            project_info['land_area'] = value
        elif 'total units' in key_lower:
            project_info['total_units'] = parse_number(value)
        elif 'number of floors' in key_lower or 'floor' in key_lower:
            project_info['floors'] = value
        elif 'number of blocks' in key_lower or 'blocks' in key_lower:
            project_info['blocks'] = parse_number(value)
        elif 'carpet area' in key_lower:
            project_info['carpet_percentage'] = value
        elif 'approval' in key_lower:
            project_info['approval'] = value
        elif 'location' in key_lower:
            project_info['location'] = value
        elif 'rera' in key_lower:
            project_info['rera'] = value

        # Extract unit configurations
        if 'bhk' in key_lower:
            # Look for patterns like "2BHK Dimensions", "3BHK Variants", etc.
            bhk_match = re.search(r'(\d+)\s*bhk', key_lower)
            if bhk_match:
                bhk_type = f"{bhk_match.group(1)}BHK"

                # Extract area from value
                area = parse_number(value) if value else None

                # Look for price in nearby rows
                price = None
                rate_psf = None

                # Check next few rows for pricing
                for j in range(idx + 1, min(idx + 5, len(df))):
                    next_row = df.iloc[j]
                    next_key = clean_data(next_row.iloc[1]) if len(next_row) > 1 else None
                    next_val = clean_data(next_row.iloc[2]) if len(next_row) > 2 else None

                    if next_key and next_val:
                        next_key_lower = next_key.lower()
                        if 'price' in next_key_lower or 'cost' in next_key_lower:
                            price = parse_number(next_val)
                        elif 'rate' in next_key_lower or 'psf' in next_key_lower:
                            rate_psf = parse_number(next_val)

                if area:
                    units.append({
                        'configuration': bhk_type,
                        'built_up_area': area,
                        'base_price': price,
                        'rate_psf': rate_psf
                    })

        # Also look for direct variant entries like "Comfort - 1680 Sq. Ft"
        if value and 'sq' in value.lower() and 'ft' in value.lower():
            area = parse_number(value)
            if area and area > 100:  # Reasonable area filter
                # Try to determine BHK from recent context
                bhk_type = None
                for j in range(max(0, idx - 3), idx):
                    prev_row = df.iloc[j]
                    prev_key = clean_data(prev_row.iloc[1]) if len(prev_row) > 1 else None
                    if prev_key and 'bhk' in prev_key.lower():
                        bhk_match = re.search(r'(\d+)\s*bhk', prev_key.lower())
                        if bhk_match:
                            bhk_type = f"{bhk_match.group(1)}BHK"
                            break

                if bhk_type:
                    # Check if this variant is already added
                    existing = [u for u in units if u['configuration'] == bhk_type and u['built_up_area'] == area]
                    if not existing:
                        units.append({
                            'configuration': bhk_type,
                            'built_up_area': area,
                            'base_price': None,
                            'rate_psf': None
                        })

    return project_info, units

def import_purva_projects(excel_path, db_path="real_estate_data.db"):
    """Import Purva projects from cost sheet"""

    print("📖 Reading Purva Excel file...")
    excel_file = pd.ExcelFile(excel_path)

    # Filter Recknor/Reckor sheets
    recknor_sheets = [s for s in excel_file.sheet_names if 'Recknor' in s or 'Reckor' in s]

    print(f"✅ Found {len(recknor_sheets)} project sheets")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Clear existing Purva projects
    print("🗑️  Clearing existing Purva projects...")
    cursor.execute("DELETE FROM project_units WHERE tenant_id = 'PURVA_001'")
    cursor.execute("DELETE FROM projects WHERE developer_name = 'Purva' OR tenant_id = 'PURVA_001'")
    conn.commit()

    inserted_projects = 0
    inserted_units = 0
    skipped_projects = 0

    # Process each sheet
    for sheet_name in recknor_sheets:
        try:
            df = pd.read_excel(excel_path, sheet_name=sheet_name)

            # Extract project name from sheet name
            project_name = sheet_name.replace(' Recknor', '').replace('Recknor', '').replace(' Reckor', '').replace('Reckor', '').replace('-', '').strip()

            # Extract project data
            project_info, units = extract_project_data(df, project_name)

            # Skip if no units found
            if not units:
                print(f"⚠️  {project_name}: No unit data found, skipping")
                skipped_projects += 1
                continue

            print(f"✅ {project_name}: Found {len(units)} unit configurations")

            # Generate project ID
            project_id = str(uuid.uuid4())[:8]

            # Determine city from project name or default
            city = 'Bangalore'
            if any(word in project_name.lower() for word in ['kochi', 'cochin', 'kerala']):
                city = 'Kochi'
            elif 'goa' in project_name.lower():
                city = 'Goa'
            elif 'mumbai' in project_name.lower():
                city = 'Mumbai'
            elif 'pune' in project_name.lower():
                city = 'Pune'
            elif 'chennai' in project_name.lower():
                city = 'Chennai'

            # Insert project
            project_data = {
                'project_id': project_id,
                'tenant_id': 'PURVA_001',
                'project_name': f"Purva {project_name}",
                'developer_name': 'Purva',
                'city': city,
                'description': f"Purva {project_name} residential project",
                'total_project_area_acres': parse_number(project_info['land_area']),
                'number_of_towers': int(project_info['blocks']) if project_info['blocks'] else None,
                'total_units_count': int(project_info['total_units']) if project_info['total_units'] else None,
                'tower_structure_details': project_info['floors'],
                'approval_body': project_info['approval'],
                'rera_registration_number': project_info['rera']
            }

            columns = ', '.join(project_data.keys())
            placeholders = ', '.join(['?' for _ in project_data])
            query = f"INSERT INTO projects ({columns}) VALUES ({placeholders})"
            cursor.execute(query, list(project_data.values()))
            inserted_projects += 1

            # Insert units
            for unit in units:
                unit_data = {
                    'unit_id': str(uuid.uuid4())[:8],
                    'project_id': project_id,
                    'tenant_id': 'PURVA_001',
                    'configuration_type': unit['configuration'],
                    'property_type': 'Apartment',
                    'built_up_area_sqft': unit['built_up_area'],
                    'carpet_area_sqft': None,
                    'base_price': unit['base_price'],
                    'current_average_psf': unit['rate_psf'],
                    'market_psf': None
                }

                columns = ', '.join(unit_data.keys())
                placeholders = ', '.join(['?' for _ in unit_data])
                query = f"INSERT INTO project_units ({columns}) VALUES ({placeholders})"
                cursor.execute(query, list(unit_data.values()))
                inserted_units += 1

        except Exception as e:
            print(f"❌ Error processing {sheet_name}: {e}")

    conn.commit()
    conn.close()

    print(f"\n✅ Purva Import Complete!")
    print(f"   Projects inserted: {inserted_projects}")
    print(f"   Projects skipped: {skipped_projects}")
    print(f"   Units inserted: {inserted_units}")

    return inserted_projects, inserted_units


if __name__ == "__main__":
    excel_path = "/Users/mudit/Downloads/Purva Cost Sheet as of 12th Dec'25.xlsx"
    db_path = "real_estate_data.db"

    print("🏗️  Starting Purva Projects Import (v2)...\n")
    projects, units = import_purva_projects(excel_path, db_path)

    print(f"\n📊 Database updated successfully!")
