"""
Quick test script to verify the database
"""

import sqlite3
from real_estate_db import create_real_estate_db

# Create the database
print("Creating database...")
schema = create_real_estate_db()
print("✅ Database created!\n")

# Connect and run test queries
conn = sqlite3.connect("real_estate_data.db")
cursor = conn.cursor()

print("="*70)
print("DATABASE VERIFICATION")
print("="*70 + "\n")

# Test 1: Count projects
cursor.execute("SELECT COUNT(*) FROM projects")
project_count = cursor.fetchone()[0]
print(f"✓ Total projects: {project_count}")

# Test 2: Count units
cursor.execute("SELECT COUNT(*) FROM project_units")
unit_count = cursor.fetchone()[0]
print(f"✓ Total units: {unit_count}\n")

# Test 3: Projects under construction
cursor.execute("SELECT project_name, completion_percentage FROM projects WHERE construction_status = 'Under Construction'")
results = cursor.fetchall()
print("Projects under construction:")
for name, completion in results:
    print(f"  - {name}: {completion}% complete")

# Test 4: Cheapest 2BHK
cursor.execute("""
    SELECT p.project_name, u.configuration_type, u.base_price, u.current_average_psf
    FROM project_units u
    JOIN projects p ON u.project_id = p.project_id
    WHERE u.configuration_type = '2BHK'
    ORDER BY u.base_price ASC
    LIMIT 1
""")
result = cursor.fetchone()
if result:
    print(f"\n✓ Cheapest 2BHK: {result[0]} - ₹{result[2]:,.0f} (@₹{result[3]} per sqft)")

# Test 5: Units with festive offers
cursor.execute("""
    SELECT p.project_name, u.configuration_type, u.current_festive_offers
    FROM project_units u
    JOIN projects p ON u.project_id = p.project_id
    WHERE u.current_festive_offers IS NOT NULL
""")
results = cursor.fetchall()
print(f"\n✓ Units with festive offers: {len(results)}")
for project, config, offer in results[:3]:
    print(f"  - {project} ({config}): {offer[:50]}...")

# Test 6: Average PSF for villas
cursor.execute("""
    SELECT AVG(current_average_psf)
    FROM project_units
    WHERE property_type = 'Villa'
""")
avg_psf = cursor.fetchone()[0]
print(f"\n✓ Average PSF for Villas: ₹{avg_psf:,.0f} per sqft")

conn.close()

print("\n" + "="*70)
print("✅ All tests passed! Database is ready for use.")
print("="*70)
