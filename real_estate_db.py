"""
Real Estate Database Setup
Creates a SQLite database with projects schema and sample data
"""

import sqlite3
from datetime import datetime, date

def create_real_estate_db():
    """Create real estate database with projects table and sample data"""

    conn = sqlite3.connect("real_estate_data.db")
    cursor = conn.cursor()

    # Drop existing tables if they exist (reverse order due to foreign keys)
    cursor.execute("DROP TABLE IF EXISTS project_units")
    cursor.execute("DROP TABLE IF EXISTS projects")

    # Create projects table (SQLite adapted schema)
    cursor.execute("""
        CREATE TABLE projects (
            project_id TEXT PRIMARY KEY,
            tenant_id TEXT NOT NULL,

            -- Core Identity
            project_name TEXT NOT NULL,
            developer_name TEXT NOT NULL,
            city TEXT NOT NULL,
            description TEXT,

            -- Structure & Area
            total_project_area_acres DECIMAL(10, 2),
            open_space_percentage DECIMAL(5, 2),
            number_of_towers INTEGER,
            total_units_count INTEGER,
            tower_structure_details TEXT,
            is_block_wing_structure BOOLEAN,

            -- Legal & Dates
            rera_registration_number TEXT,
            approval_body TEXT,
            launch_date DATE,
            sales_launch_date DATE,
            construction_start_date DATE,
            rera_possession_date DATE,
            estimated_possession_date DATE,

            -- Construction Status
            construction_status VARCHAR(50),
            completion_percentage DECIMAL(5, 2),
            construction_technology TEXT,

            -- Financials & Partners
            stamp_duty_percentage DECIMAL(5, 2),
            registration_charges_percentage DECIMAL(5, 2),
            construction_partners TEXT,

            -- Marketing & Features (stored as JSON text)
            amenities TEXT,
            payment_plans TEXT,
            unique_selling_propositions TEXT,
            undivided_share_land_details TEXT,
            project_theme TEXT,
            schools TEXT,
            colleges TEXT,
            hospitals TEXT,
            it_parks_companies TEXT,
            nearby_top_places TEXT,
            shopping_malls TEXT,
            health_fitness TEXT,
            connecting_roads TEXT,
            metro_stations TEXT,
            bus_stands TEXT,
            airport_distance TEXT,

            -- Metadata
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create index for tenant filtering
    cursor.execute("CREATE INDEX idx_projects_tenant ON projects(tenant_id)")

    # Create project_units table
    cursor.execute("""
        CREATE TABLE project_units (
            unit_id TEXT PRIMARY KEY,
            project_id TEXT REFERENCES projects(project_id) ON DELETE CASCADE,
            tenant_id TEXT NOT NULL,

            -- Classification
            configuration_type VARCHAR(50),
            property_type VARCHAR(50),

            -- Areas (Crucial for calculations)
            built_up_area_sqft DECIMAL(10, 2),
            carpet_area_sqft DECIMAL(10, 2),

            -- Pricing
            base_price DECIMAL(15, 2),
            current_average_psf DECIMAL(10, 2),
            market_psf DECIMAL(10, 2),

            -- Premiums & Variations
            view_premium_details TEXT,
            high_floor_premium_details TEXT,
            corner_unit_premium_details TEXT,

            -- Offers & Revisions
            last_price_revision_date DATE,
            last_price_change_percentage DECIMAL(5, 2),
            next_planned_revision_date DATE,
            current_festive_offers TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create index for project_units
    cursor.execute("CREATE INDEX idx_units_project ON project_units(project_id)")
    cursor.execute("CREATE INDEX idx_units_tenant ON project_units(tenant_id)")

    # Sample data - No sample projects included by default
    # Add your own projects data here or load from external source
    sample_projects = []

    # Insert sample projects data
    for project in sample_projects:
        columns = ", ".join(project.keys())
        placeholders = ", ".join(["?" for _ in project])
        query = f"INSERT INTO projects ({columns}) VALUES ({placeholders})"
        cursor.execute(query, list(project.values()))

    # Sample unit data - No sample units included by default
    # Add your own unit data here or load from external source
    sample_units = []

    # Insert sample units data
    for unit in sample_units:
        columns = ", ".join(unit.keys())
        placeholders = ", ".join(["?" for _ in unit])
        query = f"INSERT INTO project_units ({columns}) VALUES ({placeholders})"
        cursor.execute(query, list(unit.values()))

    conn.commit()
    conn.close()

    # Return schema description for LLM
    schema_description = """
    Real Estate Database Schema:

    Table 1: projects

    Core Identity:
    - project_id: TEXT PRIMARY KEY (unique identifier)
    - tenant_id: TEXT (SaaS client identifier)
    - project_name: TEXT (name of the project)
    - developer_name: TEXT (builder/developer name)
    - city: TEXT (city location)
    - description: TEXT (project description/USP)

    Structure & Area:
    - total_project_area_acres: DECIMAL (total area in acres)
    - open_space_percentage: DECIMAL (% of open/green space)
    - number_of_towers: INTEGER (count of towers)
    - total_units_count: INTEGER (total residential units)
    - tower_structure_details: TEXT (e.g., "G+20 floors")
    - is_block_wing_structure: BOOLEAN (block/wing layout)

    Legal & Dates:
    - rera_registration_number: TEXT (RERA number)
    - approval_body: TEXT (e.g., BBMP, BDA)
    - launch_date: DATE
    - sales_launch_date: DATE
    - construction_start_date: DATE
    - rera_possession_date: DATE
    - estimated_possession_date: DATE

    Construction Status:
    - construction_status: VARCHAR (e.g., 'Under Construction', 'Ready to Move')
    - completion_percentage: DECIMAL (0-100)
    - construction_technology: TEXT (e.g., "Mivan", "Precast")

    Financials:
    - stamp_duty_percentage: DECIMAL
    - registration_charges_percentage: DECIMAL
    - construction_partners: TEXT

    Marketing & Features (JSON fields):
    - amenities: TEXT (JSON array of amenities)
    - payment_plans: TEXT (JSON object of payment options)
    - unique_selling_propositions: TEXT
    - undivided_share_land_details: TEXT (UDS info)
    - project_theme: TEXT (e.g., "Mediterranean")

    Connectivity (JSON fields):
    - schools: TEXT (JSON array with name, distance)
    - colleges: TEXT (JSON array)
    - hospitals: TEXT (JSON array)
    - it_parks_companies: TEXT (JSON array)
    - nearby_top_places: TEXT (JSON array)
    - shopping_malls: TEXT (JSON array)
    - health_fitness: TEXT (JSON array)
    - connecting_roads: TEXT (JSON array)
    - metro_stations: TEXT (JSON array)
    - bus_stands: TEXT (JSON array)
    - airport_distance: TEXT

    Metadata:
    - created_at: TIMESTAMP
    - modified_at: TIMESTAMP

    Table 2: project_units

    Core Fields:
    - unit_id: TEXT PRIMARY KEY (unique identifier)
    - project_id: TEXT REFERENCES projects(project_id) (foreign key to projects)
    - tenant_id: TEXT (SaaS client identifier)

    Classification:
    - configuration_type: VARCHAR(50) (e.g., '2BHK', '3BHK', '4BHK')
    - property_type: VARCHAR(50) (e.g., 'Apartment', 'Villa', 'Penthouse')

    Areas:
    - built_up_area_sqft: DECIMAL (built-up area in sq ft)
    - carpet_area_sqft: DECIMAL (carpet area in sq ft)

    Pricing:
    - base_price: DECIMAL (base price in INR)
    - current_average_psf: DECIMAL (price per sq ft)
    - market_psf: DECIMAL (market price per sq ft)

    Premiums:
    - view_premium_details: TEXT (view-based premiums)
    - high_floor_premium_details: TEXT (floor-based premiums)
    - corner_unit_premium_details: TEXT (corner unit premiums)

    Offers & Revisions:
    - last_price_revision_date: DATE
    - last_price_change_percentage: DECIMAL
    - next_planned_revision_date: DATE
    - current_festive_offers: TEXT

    Metadata:
    - created_at: TIMESTAMP

    Sample Queries:

    Projects Table:
    - "How many projects are under construction?"
      SELECT COUNT(*) FROM projects WHERE construction_status = 'Under Construction'

    - "Show me projects near the airport"
      SELECT project_name, airport_distance FROM projects WHERE airport_distance LIKE '%8 km%'

    - "Which projects have more than 80% open space?"
      SELECT project_name, open_space_percentage FROM projects WHERE open_space_percentage > 80

    - "List all projects by Prestige Group"
      SELECT project_name, city, construction_status FROM projects WHERE developer_name LIKE '%Prestige%'

    Project Units Table:
    - "What is the average price per sqft for 3BHK units?"
      SELECT AVG(current_average_psf) FROM project_units WHERE configuration_type = '3BHK'

    - "Show me units with current festive offers"
      SELECT u.configuration_type, u.base_price, u.current_festive_offers, p.project_name
      FROM project_units u JOIN projects p ON u.project_id = p.project_id
      WHERE u.current_festive_offers IS NOT NULL

    - "Which project has the cheapest 2BHK?"
      SELECT p.project_name, u.configuration_type, u.base_price, u.current_average_psf
      FROM project_units u JOIN projects p ON u.project_id = p.project_id
      WHERE u.configuration_type = '2BHK'
      ORDER BY u.base_price ASC LIMIT 1

    - "List all villas with their prices"
      SELECT p.project_name, u.configuration_type, u.built_up_area_sqft, u.base_price
      FROM project_units u JOIN projects p ON u.project_id = p.project_id
      WHERE u.property_type = 'Villa'
    """

    return schema_description


if __name__ == "__main__":
    print("🏗️  Creating Real Estate Database...")
    schema = create_real_estate_db()
    print("✅ Database created successfully!")
    print("\n" + schema)
    print("\n📊 No sample data added - database is empty.")
    print("  Add your own projects and units data to the database.")
