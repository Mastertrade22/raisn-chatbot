"""
Real Estate Database Setup
Creates a SQLite database with projects schema and sample data
"""

import sqlite3
import json
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

    # Sample data - Purvankara real estate projects
    sample_projects = [
        # Purva Clermont - Mumbai
        {
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "project_name": "Purva Clermont",
            "developer_name": "Brigade Group",
            "city": "Bangalore",
            "description": "Premium residential apartments in Bagalur with world-class amenities and modern architecture",
            "total_project_area_acres": 17.5,
            "open_space_percentage": 75.0,
            "number_of_towers": 8,
            "total_units_count": 1080,
            "tower_structure_details": "G+19 floors",
            "is_block_wing_structure": False,
            "rera_registration_number": "PRM/KA/RERA/1251/446/PR/171117/001586",
            "approval_body": "BBMP",
            "launch_date": "2023-01-15",
            "sales_launch_date": "2023-02-01",
            "construction_start_date": "2023-03-01",
            "rera_possession_date": "2026-12-31",
            "estimated_possession_date": "2026-10-30",
            "construction_status": "Under Construction",
            "completion_percentage": 35.5,
            "construction_technology": "Mivan Technology",
            "stamp_duty_percentage": 5.0,
            "registration_charges_percentage": 1.0,
            "construction_partners": "L&T Construction, Shapoorji Pallonji",
            "amenities": json.dumps([
                "Swimming Pool", "Gymnasium", "Clubhouse", "Indoor Games Room",
                "Children's Play Area", "Jogging Track", "Yoga Deck", "Tennis Court",
                "Basketball Court", "Amphitheatre", "Party Hall", "Library"
            ]),
            "payment_plans": json.dumps({
                "Construction Linked": "10:20:70 plan",
                "Subvention": "20:80 plan with zero EMI till possession",
                "Flexi": "30:70 plan"
            }),
            "unique_selling_propositions": "75% open space, Mivan construction, Strategic location near Aerospace Park",
            "undivided_share_land_details": "42.5 sq ft per 1000 sq ft",
            "project_theme": "Mediterranean",
            "schools": json.dumps([
                {"name": "Ryan International School", "distance": "2.5 km"},
                {"name": "Greenwood High", "distance": "3.2 km"},
                {"name": "Delhi Public School", "distance": "4.1 km"}
            ]),
            "colleges": json.dumps([
                {"name": "PES University", "distance": "8.5 km"},
                {"name": "Christ University", "distance": "12.3 km"}
            ]),
            "hospitals": json.dumps([
                {"name": "Columbia Asia Hospital", "distance": "3.8 km"},
                {"name": "Manipal Hospital", "distance": "5.2 km"},
                {"name": "Aster CMI Hospital", "distance": "7.5 km"}
            ]),
            "it_parks_companies": json.dumps([
                {"name": "Manyata Tech Park", "distance": "8.2 km"},
                {"name": "Aerospace Park", "distance": "2.0 km"},
                {"name": "Kirloskar Business Park", "distance": "6.5 km"}
            ]),
            "nearby_top_places": json.dumps([
                {"name": "Nandi Hills", "distance": "25 km"},
                {"name": "Bangalore Palace", "distance": "18 km"}
            ]),
            "shopping_malls": json.dumps([
                {"name": "Elements Mall", "distance": "4.5 km"},
                {"name": "Orion Mall", "distance": "10.2 km"}
            ]),
            "health_fitness": json.dumps([
                {"name": "Cult.fit", "distance": "Within Complex"},
                {"name": "Gold's Gym", "distance": "3.5 km"}
            ]),
            "connecting_roads": json.dumps([
                "Bellary Road (NH 44)", "Bagalur Main Road", "Outer Ring Road"
            ]),
            "metro_stations": json.dumps([
                {"name": "Nagawara Metro Station (Purple Line)", "distance": "7.5 km"}
            ]),
            "bus_stands": json.dumps([
                {"name": "Bagalur Bus Stop", "distance": "1.2 km"}
            ]),
            "airport_distance": "22 km from Kempegowda International Airport"
        },
        {
            "project_id": "proj-002",
            "tenant_id": "tenant-prestige",
            "project_name": "Prestige Lavender Fields",
            "developer_name": "Prestige Group",
            "city": "Bangalore",
            "description": "Luxurious 2, 3 & 4 BHK apartments in Whitefield with premium specifications",
            "total_project_area_acres": 25.0,
            "open_space_percentage": 80.0,
            "number_of_towers": 12,
            "total_units_count": 1520,
            "tower_structure_details": "G+24 floors",
            "is_block_wing_structure": True,
            "rera_registration_number": "PRM/KA/RERA/1251/309/PR/190815/002678",
            "approval_body": "BBMP",
            "launch_date": "2022-06-01",
            "sales_launch_date": "2022-07-15",
            "construction_start_date": "2022-08-01",
            "rera_possession_date": "2025-12-31",
            "estimated_possession_date": "2025-09-30",
            "construction_status": "Under Construction",
            "completion_percentage": 62.0,
            "construction_technology": "Precast Technology",
            "stamp_duty_percentage": 5.0,
            "registration_charges_percentage": 1.0,
            "construction_partners": "Sobha Developers, NCC Limited",
            "amenities": json.dumps([
                "Olympic Size Swimming Pool", "Multi-tier Clubhouse", "Squash Court",
                "Badminton Court", "Cricket Net Practice", "Indoor Games", "Spa",
                "Banquet Hall", "Mini Theatre", "Kids Play Zone", "Skating Rink"
            ]),
            "payment_plans": json.dumps({
                "Standard": "20:20:20:20:20 plan",
                "Possession Linked": "10:90 plan",
                "Down Payment": "40:60 plan"
            }),
            "unique_selling_propositions": "80% open space, Next to IT corridor, Premium clubhouse, Precast technology",
            "undivided_share_land_details": "38.2 sq ft per 1000 sq ft",
            "project_theme": "Urban Luxury",
            "schools": json.dumps([
                {"name": "Legacy School", "distance": "1.8 km"},
                {"name": "Oakridge International", "distance": "3.5 km"},
                {"name": "Inventure Academy", "distance": "4.2 km"}
            ]),
            "colleges": json.dumps([
                {"name": "REVA University", "distance": "6.5 km"},
                {"name": "Jain University", "distance": "9.2 km"}
            ]),
            "hospitals": json.dumps([
                {"name": "Sakra World Hospital", "distance": "2.5 km"},
                {"name": "Vydehi Hospital", "distance": "4.8 km"},
                {"name": "Columbia Asia - Whitefield", "distance": "3.2 km"}
            ]),
            "it_parks_companies": json.dumps([
                {"name": "ITPL (International Tech Park)", "distance": "3.5 km"},
                {"name": "Cessna Business Park", "distance": "5.2 km"},
                {"name": "Prestige Tech Park", "distance": "2.8 km"},
                {"name": "RMZ Ecospace", "distance": "4.5 km"}
            ]),
            "nearby_top_places": json.dumps([
                {"name": "Phoenix Marketcity", "distance": "6.5 km"},
                {"name": "Whitefield Forum Mall", "distance": "4.2 km"}
            ]),
            "shopping_malls": json.dumps([
                {"name": "Phoenix Marketcity", "distance": "6.5 km"},
                {"name": "Park Square Mall", "distance": "3.8 km"},
                {"name": "VR Bengaluru", "distance": "5.5 km"}
            ]),
            "health_fitness": json.dumps([
                {"name": "Fitness First", "distance": "Within Complex"},
                {"name": "Talwalkars Gym", "distance": "2.5 km"}
            ]),
            "connecting_roads": json.dumps([
                "Whitefield Main Road", "ITPL Main Road", "Old Madras Road"
            ]),
            "metro_stations": json.dumps([
                {"name": "Whitefield Metro (Purple Line)", "distance": "5.2 km"},
                {"name": "Kadugodi Metro", "distance": "3.8 km"}
            ]),
            "bus_stands": json.dumps([
                {"name": "Whitefield TTMC", "distance": "4.5 km"}
            ]),
            "airport_distance": "38 km from Kempegowda International Airport"
        },
        {
            "project_id": "proj-003",
            "tenant_id": "tenant-sobha",
            "project_name": "Sobha Dream Acres",
            "developer_name": "Sobha Limited",
            "city": "Bangalore",
            "description": "Premium plotted development with villas in Panathur, East Bangalore",
            "total_project_area_acres": 45.0,
            "open_space_percentage": 65.0,
            "number_of_towers": 0,
            "total_units_count": 280,
            "tower_structure_details": "Individual Villas - G+2",
            "is_block_wing_structure": False,
            "rera_registration_number": "PRM/KA/RERA/1251/304/PR/200615/003425",
            "approval_body": "BDA",
            "launch_date": "2021-03-01",
            "sales_launch_date": "2021-04-15",
            "construction_start_date": "2021-05-01",
            "rera_possession_date": "2024-06-30",
            "estimated_possession_date": "2024-03-31",
            "construction_status": "Nearing Completion",
            "completion_percentage": 89.5,
            "construction_technology": "Conventional RCC",
            "stamp_duty_percentage": 5.0,
            "registration_charges_percentage": 1.0,
            "construction_partners": "Sobha In-house Construction Team",
            "amenities": json.dumps([
                "Clubhouse", "Swimming Pool", "Gym", "Landscaped Gardens",
                "Kids Play Area", "Jogging Track", "Indoor Badminton", "Table Tennis",
                "Cafeteria", "Convenience Store", "Meditation Center"
            ]),
            "payment_plans": json.dumps({
                "Standard": "30:70 plan",
                "Ready to Move": "100% on possession"
            }),
            "unique_selling_propositions": "Gated villa community, 65% green cover, Sobha quality construction",
            "undivided_share_land_details": "100% ownership on plot area",
            "project_theme": "Eco-Friendly Villas",
            "schools": json.dumps([
                {"name": "Greenwood High School", "distance": "2.2 km"},
                {"name": "The International School", "distance": "3.5 km"}
            ]),
            "colleges": json.dumps([
                {"name": "CMR University", "distance": "7.5 km"}
            ]),
            "hospitals": json.dumps([
                {"name": "Manipal Hospital Sarjapur", "distance": "3.5 km"},
                {"name": "Sparsh Hospital", "distance": "5.8 km"}
            ]),
            "it_parks_companies": json.dumps([
                {"name": "Eco Space Business Park", "distance": "4.5 km"},
                {"name": "Embassy Tech Village", "distance": "8.2 km"},
                {"name": "RMZ Ecoworld", "distance": "6.5 km"}
            ]),
            "nearby_top_places": json.dumps([
                {"name": "Varthur Lake", "distance": "3.5 km"},
                {"name": "Innovative Film City", "distance": "12 km"}
            ]),
            "shopping_malls": json.dumps([
                {"name": "Total Mall", "distance": "5.2 km"},
                {"name": "Phoenix Marketcity", "distance": "10.5 km"}
            ]),
            "health_fitness": json.dumps([
                {"name": "Community Gym", "distance": "Within Complex"},
                {"name": "Snap Fitness", "distance": "4.2 km"}
            ]),
            "connecting_roads": json.dumps([
                "Sarjapur Road", "Outer Ring Road", "Panathur Main Road"
            ]),
            "metro_stations": json.dumps([
                {"name": "Upcoming Sarjapur Metro", "distance": "Planned - 3 km"}
            ]),
            "bus_stands": json.dumps([
                {"name": "Panathur Bus Stop", "distance": "1.5 km"}
            ]),
            "airport_distance": "45 km from Kempegowda International Airport"
        },
        {
            "project_id": "proj-004",
            "tenant_id": "tenant-godrej",
            "project_name": "Godrej Woodsville",
            "developer_name": "Godrej Properties",
            "city": "Bangalore",
            "description": "Nature-themed residential project in Devanahalli with modern amenities",
            "total_project_area_acres": 12.8,
            "open_space_percentage": 70.0,
            "number_of_towers": 6,
            "total_units_count": 720,
            "tower_structure_details": "G+15 floors",
            "is_block_wing_structure": False,
            "rera_registration_number": "PRM/KA/RERA/1251/308/PR/210901/004156",
            "approval_body": "Gram Panchayat",
            "launch_date": "2023-09-01",
            "sales_launch_date": "2023-10-01",
            "construction_start_date": "2023-11-01",
            "rera_possession_date": "2027-03-31",
            "estimated_possession_date": "2027-01-31",
            "construction_status": "Under Construction",
            "completion_percentage": 18.0,
            "construction_technology": "Aluminium Formwork",
            "stamp_duty_percentage": 3.0,
            "registration_charges_percentage": 1.0,
            "construction_partners": "Shapoorji Pallonji, Tata Projects",
            "amenities": json.dumps([
                "Clubhouse", "Swimming Pool", "Fitness Center", "Yoga Pavilion",
                "Children's Play Area", "Senior Citizen Corner", "Indoor Games",
                "Amphitheater", "Party Lawn", "Walking Trails", "Organic Farm"
            ]),
            "payment_plans": json.dumps({
                "Construction Linked": "10:10:10:10:60 plan",
                "Godrej Flexi": "20:20:20:40 plan"
            }),
            "unique_selling_propositions": "Near Airport, Nature-themed design, Investment opportunity, Lower stamp duty",
            "undivided_share_land_details": "45.8 sq ft per 1000 sq ft",
            "project_theme": "Nature Living",
            "schools": json.dumps([
                {"name": "Delhi Public School - North", "distance": "5.5 km"},
                {"name": "Greenwood High - Devanahalli", "distance": "6.2 km"}
            ]),
            "colleges": json.dumps([
                {"name": "Presidency University", "distance": "8.5 km"}
            ]),
            "hospitals": json.dumps([
                {"name": "Akash Hospital", "distance": "4.2 km"},
                {"name": "Columbia Asia - Hebbal", "distance": "18 km"}
            ]),
            "it_parks_companies": json.dumps([
                {"name": "Aerospace SEZ", "distance": "5.5 km"},
                {"name": "Devanahalli Business Park", "distance": "3.8 km"}
            ]),
            "nearby_top_places": json.dumps([
                {"name": "Nandi Hills", "distance": "15 km"},
                {"name": "Devanahalli Fort", "distance": "4 km"}
            ]),
            "shopping_malls": json.dumps([
                {"name": "Esteem Mall", "distance": "8.5 km"}
            ]),
            "health_fitness": json.dumps([
                {"name": "In-house Fitness Center", "distance": "Within Complex"}
            ]),
            "connecting_roads": json.dumps([
                "NH 44 (Bellary Road)", "Devanahalli Airport Road", "BIAL Road"
            ]),
            "metro_stations": json.dumps([
                {"name": "Upcoming Airport Metro", "distance": "Planned"}
            ]),
            "bus_stands": json.dumps([
                {"name": "Devanahalli Bus Stand", "distance": "3.5 km"}
            ]),
            "airport_distance": "8 km from Kempegowda International Airport"
        },
        # Purva Clermont - Mumbai
        {
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "project_name": "Purva Clermont",
            "developer_name": "Puravankara Limited",
            "city": "Mumbai",
            "description": "4 luxurious residential towers spread over 2.25 acres in Chembur, Mumbai. Homes equipped with BluNex technology including home automation, Google Home, 5-way secured door lock, and 24x7 potable water. Features 11 ft floor-to-ceiling height and oxygenated clubhouse designed by Singapore architect Andy Fisher.",
            "total_project_area_acres": 2.25,
            "open_space_percentage": None,
            "number_of_towers": 4,
            "total_units_count": 238,
            "tower_structure_details": "A to C - 17 Floors, D - 16 floors",
            "is_block_wing_structure": True,
            "rera_registration_number": None,
            "approval_body": "RERA",
            "launch_date": "2021-03-13",
            "sales_launch_date": None,
            "construction_start_date": None,
            "rera_possession_date": None,
            "estimated_possession_date": "2025-12-01",
            "construction_status": "Under Construction",
            "completion_percentage": None,
            "construction_technology": "Hybrid Technology",
            "stamp_duty_percentage": 6.0,
            "registration_charges_percentage": None,
            "construction_partners": "Techno Infracon",
            "amenities": json.dumps([
                "Wood Play", "Kids pool", "Roastery", "Amphitheatre", "Viewing deck",
                "Lawn/Barbeque deck", "Zen Deck", "Camping area", "Basketball Hoop",
                "Hammock zone", "Gathering space", "Jogging track", "Swimming Pool",
                "Reflexology path", "Sitting Alcove", "Zip Lining", "Pet zone", "Green Zone"
            ]),
            "payment_plans": json.dumps(["CLP (Construction Link Payment)"]),
            "unique_selling_propositions": "BluNex technology with Google Home automation, 5-way secured door lock, 24x7 potable water in kitchen, 11 ft floor-to-ceiling height, Oxygenated clubhouse by Singapore architect Andy Fisher, 40+ world-class amenities, Premium location in Chembur near Eastern Freeway",
            "undivided_share_land_details": None,
            "project_theme": "Luxury Living",
            "schools": json.dumps([
                {"name": "RKB International School", "distance": "1 Km"},
                {"name": "Swami Vivekanand College", "distance": "4 Km"},
                {"name": "K J Somaiya College", "distance": "5 Km"},
                {"name": "Dhirubhai Ambani School", "distance": "6.2 Km"},
                {"name": "Orchid International School", "distance": "5 Km"},
                {"name": "Loretto Convent School", "distance": "2 Km"},
                {"name": "Bombay Scottish School", "distance": "11 Km"}
            ]),
            "colleges": json.dumps([
                {"name": "Tata Institute of Social Sciences", "distance": "200 m"}
            ]),
            "hospitals": json.dumps([
                {"name": "Asian Hearts Hospital", "distance": "7.9 km"},
                {"name": "Tata Hospital", "distance": "400 m"},
                {"name": "Hinduja Hospital", "distance": "11 Km"},
                {"name": "Surana Hospital", "distance": "2 Km"}
            ]),
            "it_parks_companies": json.dumps([
                "Infotech Park Vashi", "Neelkanth IT Park (Kurla)",
                "Neelkanth Corporate IT Park (Ghatkopar West)", "Godrej IT Park Vikhroli",
                "BSEL IT Park Vashi", "Reliance Knowledge Park Ghansoli"
            ]),
            "nearby_top_places": json.dumps([
                "Vashi", "Lokmanya Tilak Terminus", "Eastern Freeway"
            ]),
            "shopping_malls": json.dumps([
                {"name": "Cubic Mall", "distance": "1 Km"},
                {"name": "K Star Mall", "distance": "4 Km"},
                {"name": "Phoenix Mall Kurla", "distance": "6 Km"},
                {"name": "R City Mall", "distance": "8 Km"}
            ]),
            "health_fitness": None,
            "connecting_roads": None,
            "metro_stations": None,
            "bus_stands": None,
            "airport_distance": None
        },
        # Palm Vista - Mumbai
        {
            "project_id": "b8d1f15a",
            "tenant_id": "PURVA_001",
            "project_name": "Palm Vista",
            "developer_name": "Provident Housing Limited",
            "city": "Mumbai",
            "description": "Tropical-themed development spread over 16 acres at Kalyan-Shil Corridor (Shilphata). Features 30 varieties of Palm Trees, 60+ curated amenities, and smart automation features. Under TMC jurisdiction.",
            "total_project_area_acres": 16.0,
            "open_space_percentage": None,
            "number_of_towers": 8,
            "total_units_count": 1275,
            "tower_structure_details": "30 Floors",
            "is_block_wing_structure": True,
            "rera_registration_number": None,
            "approval_body": "TMC",
            "launch_date": None,
            "sales_launch_date": None,
            "construction_start_date": None,
            "rera_possession_date": None,
            "estimated_possession_date": "2028-06-01",
            "construction_status": "Under Construction",
            "completion_percentage": None,
            "construction_technology": None,
            "stamp_duty_percentage": None,
            "registration_charges_percentage": None,
            "construction_partners": None,
            "amenities": json.dumps([
                "60+ curated amenities", "Smart automation features",
                "30 varieties of Palm Trees", "Tropical landscaping",
                "Construction museum", "Show apartment"
            ]),
            "payment_plans": json.dumps([
                "CLP (Construction Link Payment) - 10% + SD + 90% on loan",
                "Godrej Home Finance - 10% + 80% loan + 10% at possession, Pre EMI Rs.5999 for 48 months",
                "Bajaj Home Finance - 15% + 80% loan + 5% at possession, 12 months EMI holiday",
                "Monthly SIP - 20% now, 12 months payment holiday",
                "ICICI Subvention Scheme - 10% + 90% loan"
            ]),
            "unique_selling_propositions": "Tropical-themed development with 30 varieties of Palm Trees, 60+ state-of-the-art curated amenities, Smart automation features in apartments, Under TMC jurisdiction (not KDMC), Well-connected Kalyan-Shil Corridor location, Significant infrastructure development in next 4-5 years, Home Loan @ 3.99% (partial interest reimbursement)",
            "undivided_share_land_details": None,
            "project_theme": "Tropical Living",
            "schools": None,
            "colleges": None,
            "hospitals": None,
            "it_parks_companies": None,
            "nearby_top_places": json.dumps(["Shilphata junction", "Kalyan-Shil Corridor"]),
            "shopping_malls": None,
            "health_fitness": None,
            "connecting_roads": None,
            "metro_stations": None,
            "bus_stands": None,
            "airport_distance": None
        }
    ]

    # Insert sample projects data
    for project in sample_projects:
        columns = ", ".join(project.keys())
        placeholders = ", ".join(["?" for _ in project])
        query = f"INSERT INTO projects ({columns}) VALUES ({placeholders})"
        cursor.execute(query, list(project.values()))

    # Sample unit data for projects
    sample_units = [
        # Brigade Eldorado units
        {
            "unit_id": "unit-001",
            "project_id": "proj-001",
            "tenant_id": "tenant-brigade",
            "configuration_type": "2BHK",
            "property_type": "Apartment",
            "built_up_area_sqft": 1250.00,
            "carpet_area_sqft": 950.00,
            "base_price": 7500000.00,
            "current_average_psf": 6000.00,
            "market_psf": 6200.00,
            "view_premium_details": "Garden facing: +2%, Park facing: +3%",
            "high_floor_premium_details": "Floor 15+: +5%",
            "corner_unit_premium_details": "Corner units: +4%",
            "last_price_revision_date": "2024-10-01",
            "last_price_change_percentage": 3.5,
            "next_planned_revision_date": "2025-04-01",
            "current_festive_offers": "New Year offer: 2% discount + Free modular kitchen"
        },
        {
            "unit_id": "unit-002",
            "project_id": "proj-001",
            "tenant_id": "tenant-brigade",
            "configuration_type": "3BHK",
            "property_type": "Apartment",
            "built_up_area_sqft": 1650.00,
            "carpet_area_sqft": 1300.00,
            "base_price": 10500000.00,
            "current_average_psf": 6364.00,
            "market_psf": 6500.00,
            "view_premium_details": "Garden facing: +2%, Park facing: +3%",
            "high_floor_premium_details": "Floor 15+: +5%",
            "corner_unit_premium_details": "Corner units: +4%",
            "last_price_revision_date": "2024-10-01",
            "last_price_change_percentage": 3.5,
            "next_planned_revision_date": "2025-04-01",
            "current_festive_offers": "New Year offer: 2% discount + Free modular kitchen"
        },
        {
            "unit_id": "unit-003",
            "project_id": "proj-001",
            "tenant_id": "tenant-brigade",
            "configuration_type": "4BHK",
            "property_type": "Apartment",
            "built_up_area_sqft": 2300.00,
            "carpet_area_sqft": 1850.00,
            "base_price": 15500000.00,
            "current_average_psf": 6739.00,
            "market_psf": 6900.00,
            "view_premium_details": "Garden facing: +2%, Park facing: +3%, Lake view: +8%",
            "high_floor_premium_details": "Floor 15+: +5%",
            "corner_unit_premium_details": "Corner units: +6%",
            "last_price_revision_date": "2024-10-01",
            "last_price_change_percentage": 3.5,
            "next_planned_revision_date": "2025-04-01",
            "current_festive_offers": "New Year offer: 3% discount + Free home automation"
        },
        # Prestige Lavender Fields units
        {
            "unit_id": "unit-004",
            "project_id": "proj-002",
            "tenant_id": "tenant-prestige",
            "configuration_type": "2BHK",
            "property_type": "Apartment",
            "built_up_area_sqft": 1320.00,
            "carpet_area_sqft": 1020.00,
            "base_price": 9800000.00,
            "current_average_psf": 7424.00,
            "market_psf": 7600.00,
            "view_premium_details": "Premium view: +4%",
            "high_floor_premium_details": "Floor 20+: +6%",
            "corner_unit_premium_details": "Corner units: +5%",
            "last_price_revision_date": "2024-11-15",
            "last_price_change_percentage": 4.0,
            "next_planned_revision_date": "2025-03-01",
            "current_festive_offers": "Republic Day: Waiver on registration charges"
        },
        {
            "unit_id": "unit-005",
            "project_id": "proj-002",
            "tenant_id": "tenant-prestige",
            "configuration_type": "3BHK",
            "property_type": "Apartment",
            "built_up_area_sqft": 1850.00,
            "carpet_area_sqft": 1450.00,
            "base_price": 14500000.00,
            "current_average_psf": 7838.00,
            "market_psf": 8000.00,
            "view_premium_details": "Premium view: +4%, Tech park view: +3%",
            "high_floor_premium_details": "Floor 20+: +6%",
            "corner_unit_premium_details": "Corner units: +5%",
            "last_price_revision_date": "2024-11-15",
            "last_price_change_percentage": 4.0,
            "next_planned_revision_date": "2025-03-01",
            "current_festive_offers": "Republic Day: Waiver on registration charges"
        },
        {
            "unit_id": "unit-006",
            "project_id": "proj-002",
            "tenant_id": "tenant-prestige",
            "configuration_type": "4BHK",
            "property_type": "Penthouse",
            "built_up_area_sqft": 3200.00,
            "carpet_area_sqft": 2600.00,
            "base_price": 28000000.00,
            "current_average_psf": 8750.00,
            "market_psf": 9000.00,
            "view_premium_details": "Penthouse premium: +10%, Panoramic view: +5%",
            "high_floor_premium_details": "Top floor: +8%",
            "corner_unit_premium_details": "Duplex corner: +7%",
            "last_price_revision_date": "2024-11-15",
            "last_price_change_percentage": 4.0,
            "next_planned_revision_date": "2025-03-01",
            "current_festive_offers": "Exclusive: Free club membership for 5 years"
        },
        # Sobha Dream Acres units
        {
            "unit_id": "unit-007",
            "project_id": "proj-003",
            "tenant_id": "tenant-sobha",
            "configuration_type": "3BHK",
            "property_type": "Villa",
            "built_up_area_sqft": 2200.00,
            "carpet_area_sqft": 1900.00,
            "base_price": 18500000.00,
            "current_average_psf": 8409.00,
            "market_psf": 8500.00,
            "view_premium_details": "Corner plot: +8%, Park facing: +5%",
            "high_floor_premium_details": "N/A",
            "corner_unit_premium_details": "Corner plot premium: +8%",
            "last_price_revision_date": "2024-06-01",
            "last_price_change_percentage": 2.0,
            "next_planned_revision_date": "2025-06-01",
            "current_festive_offers": "Ready to move: No price escalation"
        },
        {
            "unit_id": "unit-008",
            "project_id": "proj-003",
            "tenant_id": "tenant-sobha",
            "configuration_type": "4BHK",
            "property_type": "Villa",
            "built_up_area_sqft": 3000.00,
            "carpet_area_sqft": 2650.00,
            "base_price": 26500000.00,
            "current_average_psf": 8833.00,
            "market_psf": 9000.00,
            "view_premium_details": "Corner plot: +8%, Lake view: +10%",
            "high_floor_premium_details": "N/A",
            "corner_unit_premium_details": "Corner plot premium: +10%",
            "last_price_revision_date": "2024-06-01",
            "last_price_change_percentage": 2.0,
            "next_planned_revision_date": "2025-06-01",
            "current_festive_offers": "Ready to move: Free landscaping worth 5 lakhs"
        },
        # Godrej Woodsville units
        {
            "unit_id": "unit-009",
            "project_id": "proj-004",
            "tenant_id": "tenant-godrej",
            "configuration_type": "2BHK",
            "property_type": "Apartment",
            "built_up_area_sqft": 1180.00,
            "carpet_area_sqft": 900.00,
            "base_price": 5500000.00,
            "current_average_psf": 4661.00,
            "market_psf": 4800.00,
            "view_premium_details": "Nature view: +3%",
            "high_floor_premium_details": "Floor 12+: +4%",
            "corner_unit_premium_details": "Corner units: +3%",
            "last_price_revision_date": "2024-12-01",
            "last_price_change_percentage": 5.0,
            "next_planned_revision_date": "2025-06-01",
            "current_festive_offers": "Pre-launch: 8% discount + Free car parking"
        },
        {
            "unit_id": "unit-010",
            "project_id": "proj-004",
            "tenant_id": "tenant-godrej",
            "configuration_type": "3BHK",
            "property_type": "Apartment",
            "built_up_area_sqft": 1580.00,
            "carpet_area_sqft": 1250.00,
            "base_price": 7800000.00,
            "current_average_psf": 4937.00,
            "market_psf": 5100.00,
            "view_premium_details": "Nature view: +3%, Hills view: +6%",
            "high_floor_premium_details": "Floor 12+: +4%",
            "corner_unit_premium_details": "Corner units: +4%",
            "last_price_revision_date": "2024-12-01",
            "last_price_change_percentage": 5.0,
            "next_planned_revision_date": "2025-06-01",
            "current_festive_offers": "Pre-launch: 8% discount + Free car parking + Gold coins"
        },
        # Purva Clermont units
        {
            "unit_id": "4b6a839f",
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "configuration_type": "2 BHK Elite",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 533,
            "base_price": 23700000,
            "current_average_psf": 44465.29,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "d345e72c",
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "configuration_type": "2 BHK Grandeur",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 619,
            "base_price": 27400000,
            "current_average_psf": 44264.94,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "329d69b9",
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "configuration_type": "2 BHK Grandeur",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 628,
            "base_price": 27800000,
            "current_average_psf": 44267.52,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "57515d3b",
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "configuration_type": "3 BHK Elite",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 974,
            "base_price": 43100000,
            "current_average_psf": 44250.51,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "b53ed528",
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "configuration_type": "3 BHK Grandeur",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 1000,
            "base_price": 44100000,
            "current_average_psf": 44100.0,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "15d200b3",
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "configuration_type": "3 BHK Grandeur",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 1019,
            "base_price": 45000000,
            "current_average_psf": 44160.94,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "2a6b0b25",
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "configuration_type": "4 BHK Duplex",
            "property_type": "Duplex",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 1354,
            "base_price": 61200000,
            "current_average_psf": 45199.41,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "c999600b",
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "configuration_type": "3 BHK Elite (Mount Prive)",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 970,
            "base_price": 40500000,
            "current_average_psf": 41752.58,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "a5949b72",
            "project_id": "a8487c5a",
            "tenant_id": "PURVA_001",
            "configuration_type": "3 BHK Elite (Mount Prive)",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 996,
            "base_price": 41200000,
            "current_average_psf": 41365.46,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        # Palm Vista units
        {
            "unit_id": "fddbf44d",
            "project_id": "b8d1f15a",
            "tenant_id": "PURVA_001",
            "configuration_type": "1 BHK",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 395,
            "base_price": 4700000,
            "current_average_psf": 11898.73,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "e16d2cb6",
            "project_id": "b8d1f15a",
            "tenant_id": "PURVA_001",
            "configuration_type": "2 BHK",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 685,
            "base_price": 8000000,
            "current_average_psf": 11678.83,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "3538130b",
            "project_id": "b8d1f15a",
            "tenant_id": "PURVA_001",
            "configuration_type": "2.5 BHK",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 764,
            "base_price": 9300000,
            "current_average_psf": 12172.77,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "c08f7e8f",
            "project_id": "b8d1f15a",
            "tenant_id": "PURVA_001",
            "configuration_type": "1 BHK (Serenity)",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 453,
            "base_price": 5600000,
            "current_average_psf": 12362.03,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        },
        {
            "unit_id": "ce92dd7a",
            "project_id": "b8d1f15a",
            "tenant_id": "PURVA_001",
            "configuration_type": "2 BHK (Serenity)",
            "property_type": "Apartment",
            "built_up_area_sqft": None,
            "carpet_area_sqft": 637,
            "base_price": 7500000,
            "current_average_psf": 11773.94,
            "market_psf": None,
            "view_premium_details": None,
            "high_floor_premium_details": None,
            "corner_unit_premium_details": None,
            "last_price_revision_date": None,
            "last_price_change_percentage": None,
            "next_planned_revision_date": None,
            "current_festive_offers": "No Stamp Duty & Registration"
        }
    ]

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
    print("\n📊 Sample data added:")
    print("  Projects:")
    print("    - Brigade Eldorado (Bagalur) - 3 unit types")
    print("    - Prestige Lavender Fields (Whitefield) - 3 unit types")
    print("    - Sobha Dream Acres (Panathur) - 2 villa types")
    print("    - Godrej Woodsville (Devanahalli) - 2 unit types")
    print("\n  Total: 4 projects, 10 unit configurations")
