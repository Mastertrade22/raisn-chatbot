"""
Insert Chennai and Kochi Projects into Database
Adds 2 Chennai projects and 1 Kochi project
"""

import sqlite3
import json

# Connect to database
conn = sqlite3.connect("real_estate_data.db")
cursor = conn.cursor()

# =====================
# PURVA WINDERMERE (Chennai)
# =====================
purva_windermere = {
    "project_id": "e4c22e70",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Windermere",
    "developer_name": "Puravankara Limited",
    "city": "Chennai",
    "description": "Large residential project spread over 55 acres at Medavakkam, just 10 minutes from Thoraipakkam. Features 64 towers across multiple phases. Phase 1 & 2 (1876 units) RTMI, Phase 3 Lakevista (1910 units) under construction. 75% open space with award-winning construction.",
    "total_project_area_acres": 55.0,
    "open_space_percentage": 75.0,
    "number_of_towers": 64,
    "total_units_count": 3954,
    "tower_structure_details": "Windermere S+7, Lakevista S+10/11/12",
    "is_block_wing_structure": True,
    "rera_registration_number": None,
    "approval_body": "CMDA",
    "launch_date": "2011-03-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2026-12-01",
    "construction_status": "RTMI / Under Construction",
    "completion_percentage": None,
    "construction_technology": "Conventional",
    "stamp_duty_percentage": 9.0,
    "registration_charges_percentage": None,
    "construction_partners": "Kalpatru Constructions",
    "amenities": json.dumps([
        "Club House", "Swimming Pool", "Childrens Play Area", "Jogging track", "Super market",
        "Multi-purpose Hall", "Landscaped Garden", "Gymnasium", "Billiards", "Table tennis Room",
        "Entertainment center", "Squash Court", "Cards Room/Indoor Game", "Health club",
        "Provision for restaurant", "Parlours", "Creche", "Jamming Room", "Aerobics/Yoga Room"
    ]),
    "payment_plans": json.dumps(["Payment within 45 days from booking", "CLP for Lakevista"]),
    "unique_selling_propositions": "55 Acres development - one of the largest in Chennai, 75% open space, Award: BEST CONSTRUCTION PROJECT - 9th CIDC Vishwakarma Awards 2017, 3954 total units across phases, Conventional construction technology, Near OMR IT corridor",
    "undivided_share_land_details": None,
    "project_theme": "Large Community Living",
    "schools": json.dumps([
        "Satyabhama University - 10.8 Km", "St. Joseph College of Engineering - 12.4 Km",
        "Jain Engineering College - 8.4 Km", "Mohd Sathak Engineering College - 6.3 Km",
        "Apple Kids, Global Kids - 6.5 Km", "Christ the King School - 9.4 Km",
        "Zigma Matriculation School - 4 Km", "BS Matriculation School - 3.6 Km",
        "PSBB Millennium - 12.7 Km", "Bharathi Vidyalaya - 4.2 Km"
    ]),
    "colleges": json.dumps([
        "KCG College of Technology - 12.5 Km", "Balaji Dental College - 3.9 Km",
        "Jerusalem College of Arts and Science - 4.1 Km"
    ]),
    "hospitals": json.dumps([
        "Kamakshi Hospital - 4.6 Km", "Global Hospitals - 5.2 Km", "V-Cure Hospital - 1.8 Km",
        "Prashanth Super Speciality Hospital, Velachery - 7.9 Km",
        "Chettinad Super Speciality Hospital - 22.5 Km"
    ]),
    "it_parks_companies": json.dumps([
        "Mahindra Satyam - 5.6 Km", "Tata Consultancy Services - 7.75 Km",
        "Accenture India - 7.4 Km", "Cognizant Technology Solutions - 6.9 Km",
        "Wipro Technologies - 6.6 Km", "Infosys - 9 Km", "Siemens - 10.3 Km",
        "Ford - 4.4 Km", "Sutherland Global Service - 7.4 Km"
    ]),
    "nearby_top_places": json.dumps(["Medavakkam", "Thoraipakkam", "Velachery", "OMR"]),
    "shopping_malls": json.dumps(["PVR Mall - 8 Km", "Phoenix Mall - 10.3 Km"]),
    "health_fitness": None,
    "connecting_roads": json.dumps([
        "Outer Ring Road", "Airport", "Tambaram", "OMR Velacherry connecting to Taramani",
        "Adyar & Thiruvanmiyur", "Guindy Race Course", "Sholinganallur to Siruseri",
        "Pallavaram to Airport Link road"
    ]),
    "metro_stations": json.dumps([
        "Velacherry MTC", "Guindy Metro & Railway station", "Tambaram Railway station"
    ]),
    "bus_stands": None,
    "airport_distance": "Near Airport via Pallavaram Link road"
}

# =====================
# PURVA SOMERSET HOUSE (Chennai)
# =====================
purva_somerset_house = {
    "project_id": "ea54683d",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Somerset House",
    "developer_name": "Puravankara Limited",
    "city": "Chennai",
    "description": "WorldHome Collection ultra-luxury project on Five Furlong Road, off Adyar near Raj Bhavan and Madras Race Course. 1.97 acres with 161 units across 4 towers. Features stunning views of 55-acre Madras Race Club and 667-acre Guindy National Park. Façade by Hadi Teherani (Germany), 23,000 sqft clubhouse by Andy Fisher (Singapore).",
    "total_project_area_acres": 1.97,
    "open_space_percentage": 65.0,
    "number_of_towers": 4,
    "total_units_count": 161,
    "tower_structure_details": "3B+S+12 with Penthouse only in Tower C & D",
    "is_block_wing_structure": True,
    "rera_registration_number": "TN/29/BUILDING/013/2019",
    "approval_body": "RERA",
    "launch_date": "2019-06-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": "2024-06-01",
    "estimated_possession_date": None,
    "construction_status": "RTMI - CC Received",
    "completion_percentage": 100.0,
    "construction_technology": "Conventional RCC frame Construction",
    "stamp_duty_percentage": 9.0,
    "registration_charges_percentage": None,
    "construction_partners": "JMC",
    "amenities": json.dumps([
        "Oxygenated Club House", "Infinity Rooftop Swimming Pool", "Home Automation (BluNex)",
        "The Gallery - Roof Top Lounge", "Rooftop BBQ Lounge",
        "The Ascot Lounge - Inspired by Royal Ascot Racecourse UK",
        "The Edge - Swimming pool on 12th Floor with stunning view",
        "Pulse Gym - Inspired by playground in Denmark", "Kids Splash Pool", "Play Areas",
        "Terrace Gardens (Water, Sound, Fragrance)", "Kids Cycling Track",
        "The Equestrian Grill & Barbeque Area", "Rooftop Dining Area", "Adult Fitness Zone",
        "Green Walls & Water Bodies", "Squash Court", "Spa Services", "Yoga and Meditation areas",
        "Pet-Friendly Zones", "Convenience Store", "3-point Security"
    ]),
    "payment_plans": json.dumps(["5 Lakhs Booking", "15% in 10 days", "80% in 30 days", "5% at possession"]),
    "unique_selling_propositions": "WorldHome Collection - Ultra Luxury, Views of 55-acre Madras Race Club, Overlooking 667-acre Guindy National Park, Façade by Hadi Teherani, Germany, 23,000 sqft clubhouse by Andy Fisher Workshop, Singapore, Japanese-themed rooftop gardens, Infinity pool on 12th floor, BluNex Home Automation with drinking water from tap, 15 minutes from Chennai International Airport, 5 mins from Phoenix Marketcity, Only 161 exclusive units - 4 units per floor, RERA registered, 1% benefit for women homebuyers",
    "undivided_share_land_details": None,
    "project_theme": "Ultra Luxury - WorldHome Collection",
    "schools": json.dumps([
        "DAV Baba Vidyalaya, Ashram, Arsha Vidya Mandir - 950 mts",
        "Guru Nanak Matric School, GEM School - 1.4 Km",
        "Gurunanak, MGR University, DAV Baba IIT, HIET, NIFT - 2.5 Km",
        "Anna University - 5.9 Km"
    ]),
    "colleges": None,
    "hospitals": json.dumps([
        "Raadha Rajendran, Balaji Hospital, VHS, Prashant - 2.1 Km",
        "Apollo Hospital - 2.3 Km"
    ]),
    "it_parks_companies": json.dumps([
        "Tidel Park - 6.7 Km", "Ascendas - 6.8 Km", "Ramanujam IT - 7.2 Km",
        "Guindy Industrial Estate - 3 Km", "DLF - 6.2 Km", "Olympia - 2.8 Km",
        "Tamarai Tech Park - 2.5 Km", "HP", "Verizon", "IBM", "Cognizant", "TCS"
    ]),
    "nearby_top_places": json.dumps([
        "Madras Race Club", "Guindy National Park", "Kathipara Flyover",
        "Phoenix Marketcity Mall", "Five Furlong Road", "Adyar", "Guindy"
    ]),
    "shopping_malls": json.dumps([
        "Phoenix Mall - 2.2 Km", "More Supermarket - 1.5 Km",
        "Nilgiris - 10 mins drive", "Brand Factory - 7.1 Km"
    ]),
    "health_fitness": None,
    "connecting_roads": json.dumps(["Velacherry Road", "GST Road", "OMR"]),
    "metro_stations": json.dumps(["Metro - 950 Mts from site"]),
    "bus_stands": None,
    "airport_distance": "15 minutes from Chennai International Airport"
}

# =====================
# MARINA ONE (Kochi)
# =====================
marina_one = {
    "project_id": "1af769b2",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Marina One",
    "developer_name": "Puravankara Limited",
    "city": "Kochi",
    "description": "Largest waterfront community in Kerala, spread over 16.7 acres at Marine Drive. Features 12 towers with G+25/27/28 floors and 1147 units. Unique C-shape building design ensures every home has water views of Arabian Sea. 5 acres central courtyard with 50+ amenities. Jointly developed by Puravankara and Sobha.",
    "total_project_area_acres": 16.7,
    "open_space_percentage": None,
    "number_of_towers": 12,
    "total_units_count": 1147,
    "tower_structure_details": "G+ 25/27/28",
    "is_block_wing_structure": True,
    "rera_registration_number": None,
    "approval_body": "Corporation of Cochin",
    "launch_date": "2018-01-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2028-01-01",
    "construction_status": "Under Construction",
    "completion_percentage": None,
    "construction_technology": "RCC",
    "stamp_duty_percentage": 8.0,
    "registration_charges_percentage": 2.0,
    "construction_partners": "Sobha Ltd",
    "amenities": json.dumps([
        "50 metre Lap Pool", "Mini Theatre (30 Seater)", "Landscaped Parks", "Walking Zones",
        "Kids Play Area", "Community Space", "Children Play Park", "Barbeque Corner",
        "Jogging/Bike Track", "Cricket Pitch", "Clinic", "Multi Court (Football, Basketball, Volleyball)",
        "Tennis Court", "Amphitheatre", "Skating Rink", "Butterfly/Eco Trail", "Sun Deck",
        "Leisure Pool", "Tree Promenade", "Events Plaza", "Party Lawn", "Creche",
        "Multipurpose Hall", "Squash Court", "Chess/Carrom", "Salon", "Steam/Sauna",
        "Club", "Yoga/Aerobics", "Table Tennis", "Badminton Court", "Library",
        "Convenience Store", "5 Acre Urban Oasis"
    ]),
    "payment_plans": json.dumps(["Construction Link Payment (CLP)"]),
    "unique_selling_propositions": "Largest waterfront community in Kerala, Marine Drive - Kochis most coveted neighbourhood, Views of Arabian Sea, Unique C-shape building design - every home has water views, 5 acres urban oasis with 50m swimming pool, Next to 2.74-hectare Mangalavanam Bird Sanctuary, Jointly developed by Puravankara and Sobha Ltd, 45+ modern amenities, Contemporary open design with large windows",
    "undivided_share_land_details": None,
    "project_theme": "Waterfront Living",
    "schools": json.dumps([
        "ST Teresas College - 3 Km", "ST Teresas Higher Secondary School - 3.1 Km",
        "ST Alberts College - 2.5 Km", "Maharajas College - 3.7 Km",
        "Govt Law College - 3.2 Km", "ST Antonys Higher Secondary School - 3.2 Km",
        "Chinmaya Vidyalaya Higher Secondary School - 3.6 Km"
    ]),
    "colleges": None,
    "hospitals": json.dumps([
        "Lourdes Hospital - 1.5 kms", "Medical Trust Hospital - 5 kms", "Lisie Hospital - 4 kms",
        "General Hospital EKM - 3.7 Km", "City Hospital - 3.3 Km", "Sree Krishna Hospital - 5.2 Km"
    ]),
    "it_parks_companies": json.dumps([
        "Info Park Kakkanad - 15 Km", "CES - 7.8 Km", "KINFRA - 22 Km"
    ]),
    "nearby_top_places": json.dumps([
        "Marine Drive", "Arabian Sea", "Mangalavanam Bird Sanctuary", "Kochi Backwaters"
    ]),
    "shopping_malls": json.dumps([
        "Centre Square Mall - 4.4 Km", "Ashis Shopping Centre - 9.7 Km",
        "Lulu Mall - 9 Km", "GCDA Shopping Mall - 6.3 Km"
    ]),
    "health_fitness": None,
    "connecting_roads": json.dumps([
        "Container Terminal Road", "Marine Drive connecting Chattiyath Road",
        "MG Road", "High Court Road"
    ]),
    "metro_stations": json.dumps(["3.2 kms from Metro Station"]),
    "bus_stands": None,
    "airport_distance": None
}

# Insert all projects
projects = [purva_windermere, purva_somerset_house, marina_one]

for project in projects:
    columns = ", ".join(project.keys())
    placeholders = ", ".join(["?" for _ in project])
    query = f"INSERT INTO projects ({columns}) VALUES ({placeholders})"
    cursor.execute(query, list(project.values()))
    print(f"✅ Inserted project: {project['project_name']} ({project['city']})")

# =====================
# UNITS DATA
# =====================

all_units = []

# Purva Windermere Units
windermere_units = [
    {"unit_id": "a94a8893", "project_id": "e4c22e70", "tenant_id": "PURVA_DEFAULT", "configuration_type": "1 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 610, "base_price": 5200000, "current_average_psf": 8524.59, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "RTMI"},
    {"unit_id": "b8984f10", "project_id": "e4c22e70", "tenant_id": "PURVA_DEFAULT", "configuration_type": "1 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 620, "base_price": 5200000, "current_average_psf": 8387.1, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "Lakevista - Under Construction"},
    {"unit_id": "85bbafa4", "project_id": "e4c22e70", "tenant_id": "PURVA_DEFAULT", "configuration_type": "2 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 908, "base_price": 7099000, "current_average_psf": 7818.28, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "New Tower"},
    {"unit_id": "d0afb8d3", "project_id": "e4c22e70", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1169, "base_price": 11100000, "current_average_psf": 9495.3, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "New Tower"},
    {"unit_id": "f29ebd74", "project_id": "e4c22e70", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3B + 3T", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1468, "base_price": 11700000, "current_average_psf": 7970.03, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "New Tower"}
]

# Purva Somerset House Units
somerset_units = [
    {"unit_id": "1dd0ee64", "project_id": "ea54683d", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BR", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1929, "base_price": 29500000, "current_average_psf": 15292.9, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "c0fd62fb", "project_id": "ea54683d", "tenant_id": "PURVA_DEFAULT", "configuration_type": "4 BR", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 2475, "base_price": 45000000, "current_average_psf": 18181.82, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "7d459a0c", "project_id": "ea54683d", "tenant_id": "PURVA_DEFAULT", "configuration_type": "Duplex Penthouse", "property_type": "Penthouse", "built_up_area_sqft": None, "carpet_area_sqft": 2651, "base_price": 58000000, "current_average_psf": 21878.54, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "800-850 sqft Pvt Terrace"},
    {"unit_id": "63c3ee44", "project_id": "ea54683d", "tenant_id": "PURVA_DEFAULT", "configuration_type": "5 BHK Imperial Mansions", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 3752, "base_price": 70000000, "current_average_psf": 18656.72, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None}
]

# Marina One Units
marina_units = [
    {"unit_id": "e02690e3", "project_id": "1af769b2", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3.5 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 2300, "base_price": 30000000, "current_average_psf": 13043.48, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "ad6d8c62", "project_id": "1af769b2", "tenant_id": "PURVA_DEFAULT", "configuration_type": "4 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 3000, "base_price": 45000000, "current_average_psf": 15000.0, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None}
]

# Combine all units
all_units = windermere_units + somerset_units + marina_units

# Insert all units
for unit in all_units:
    columns = ", ".join(unit.keys())
    placeholders = ", ".join(["?" for _ in unit])
    query = f"INSERT INTO project_units ({columns}) VALUES ({placeholders})"
    cursor.execute(query, list(unit.values()))

print(f"\n✅ Inserted {len(windermere_units)} units for Purva Windermere")
print(f"✅ Inserted {len(somerset_units)} units for Purva Somerset House")
print(f"✅ Inserted {len(marina_units)} units for Marina One")

# Commit and close
conn.commit()
conn.close()

print("\n🎉 Successfully inserted all Chennai and Kochi projects!")
print(f"\nTotal: 3 projects (2 Chennai + 1 Kochi), {len(all_units)} units")
