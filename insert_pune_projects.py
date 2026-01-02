"""
Insert Pune Projects into Database
Adds Purva Silversands, Purva Emerald Bay Ph2, and Purva Aspire
"""

import sqlite3
import json

# Connect to database
conn = sqlite3.connect("real_estate_data.db")
cursor = conn.cursor()

# =====================
# PURVA SILVERSANDS
# =====================
purva_silversands = {
    "project_id": "6303abd4",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Silversands",
    "developer_name": "Puravankara Limited",
    "city": "Pune",
    "description": "Premium residential project spread over 19.37 acres at Keshav Nagar, Mundhwa. Features 6 residential towers with 21-22 floors plus 1 tower for Pods and Condos. Award-winning design with 87% open space.",
    "total_project_area_acres": 19.37,
    "open_space_percentage": 87.0,
    "number_of_towers": 7,
    "total_units_count": 674,
    "tower_structure_details": "3P+21 Floors, 2P+20/22 Floors",
    "is_block_wing_structure": True,
    "rera_registration_number": None,
    "approval_body": "PMC and RERA",
    "launch_date": "2016-04-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2023-11-01",
    "construction_status": "Nearing Possession",
    "completion_percentage": None,
    "construction_technology": "Mivan",
    "stamp_duty_percentage": 7.0,
    "registration_charges_percentage": None,
    "construction_partners": None,
    "amenities": json.dumps([
        "Gymnasium", "Jamming room", "Two cricket practice nets", "Provision for supermarket",
        "Lego room", "Outdoor children play area", "Squash court", "Wave pool", "Paw Park",
        "Table tennis", "Snorkeling fish tank view from swimming pool", "Well lit landscape garden",
        "Pool table", "Golf putting", "Science club hobby complete with benches and stools",
        "Yoga / Meditation / Aerobics / Ballet room", "Roof top gazing observatory area",
        "Party hall", "Swimming pool with kids pool", "Steam and Sauna", "One Tennis court",
        "Jacuzzi", "One multipurpose court (Volleyball/Badminton)", "Jogging track", "One Basketball post"
    ]),
    "payment_plans": json.dumps(["Construction Link Payment (CLP)"]),
    "unique_selling_propositions": "19.37 acres development with 87% open space, 674 units including 147 Pods & Condos, Mivan construction technology, Scale Model at Site Office, Sample flat in Tower No. 4, Award: REALTY+ EXCELLENCE AWARDS - Design Project of the Year, Rooftop gazing observatory area, Wave pool and Snorkeling fish tank view",
    "undivided_share_land_details": None,
    "project_theme": "Modern Living",
    "schools": json.dumps([
        "Vibgyor International (Magarpatta) - 2.5KM", "Pawar International (Amanora) - 2KM",
        "Phoenix School (Kharadi) - 3KM", "Orbis School (Keshavnagar) - 1KM",
        "St Arnolds - 3.2KM", "Kalyani School - 3.5KM", "HDFC School - 2KM",
        "Symbiosis International School - 4.5KM", "Lexicon International (Kalyani Nagar) - 4KM"
    ]),
    "colleges": None,
    "hospitals": json.dumps([
        "Columbia Asia (Kharadi) - 2 KM", "Nobel Hospital (Magarpatta) - 2.5 KM",
        "Sahyadri Hospital (Magarpatta) - 3 KM"
    ]),
    "it_parks_companies": json.dumps([
        "EON Free Zone (Kharadi) - 2 KM", "World Trade Centre (WTC) - 2KM",
        "Magarpatta IT Park - 3KM", "Commerzone - 6KM", "Global Business Park - 2KM",
        "Business Bay & Tech Park 1 - 6KM", "Cerebrum IT Park - 4KM", "Weikfield IT Park - 5KM"
    ]),
    "nearby_top_places": json.dumps(["Keshav Nagar", "Mundhwa", "Kharadi", "Magarpatta"]),
    "shopping_malls": json.dumps([
        "Season Mall - 2KM", "Amanora Mall - 2KM", "Phoenix Marketcity - 5KM", "Nitesh Hub - 3.5KM"
    ]),
    "health_fitness": None,
    "connecting_roads": json.dumps([
        "Kharadi Bypass connecting to WTC, EON IT Park", "Magarpatta & Solapur Highway",
        "Mundhwa Road connecting to Koregaon Park Kalyani Nagar"
    ]),
    "metro_stations": json.dumps(["Upcoming Bridge connecting to Kharadi in less than 1 KM"]),
    "bus_stands": None,
    "airport_distance": None
}

# =====================
# PURVA EMERALD BAY - PH2
# =====================
purva_emerald_bay = {
    "project_id": "6399a992",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Emerald Bay - Ph2",
    "developer_name": "Puravankara Limited",
    "city": "Pune",
    "description": "Beach-themed residential project spanning 19.37 acres at Keshav Nagar, Mundhwa. Phase 2 features G+24 floors with 87% lush green open spaces. 4 acres of dedicated beach-themed amenities including Snorkelling Pool, Sunken Bar, Wave Pool, and Infinity Pool.",
    "total_project_area_acres": 19.37,
    "open_space_percentage": 87.0,
    "number_of_towers": 3,
    "total_units_count": 280,
    "tower_structure_details": "Tower 2 (3P+21 Floors), Tower 3 (3P+21 Floors), Tower 11 (2P+28 Floors)",
    "is_block_wing_structure": True,
    "rera_registration_number": None,
    "approval_body": "PMC and RERA",
    "launch_date": "2020-09-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2025-06-01",
    "construction_status": "Under Construction",
    "completion_percentage": None,
    "construction_technology": "Mivan",
    "stamp_duty_percentage": 7.0,
    "registration_charges_percentage": None,
    "construction_partners": None,
    "amenities": json.dumps([
        "Infinity Pool", "Snorkelling Pool", "Sunken Bar", "Fish Feeding Deck", "Koi Pond",
        "Wave Pool", "Paddle Pool", "Beach Volleyball Court", "Multi-play Court", "Jogging Track",
        "Skating Rink", "Cricket Pitch", "Golf Putting Green", "Kids Play Area", "BBQ Deck",
        "Yoga Deck", "Meditation Pavilion", "Senior Citizens Court", "Paw Park",
        "World Class Clubhouse", "30+ Amenities"
    ]),
    "payment_plans": json.dumps(["CLP", "Flexi EMI Options", "Customized Payment Schedule"]),
    "unique_selling_propositions": "19 Acres development with G+24 Floors, 87% lush green open spaces, 4 Acres of dedicated beach-themed amenities, Snorkelling Pool, Sunken Bar, Wave Pool, Fish Feeding Deck & Koi Pond, World Class Clubhouse with 30+ Amenities, 15 km Elevated Corridor connecting Ramwadi to Vanaz with extension to Kharadi, Proximity to proposed Flyover to Magarpatta, Award: 13TH REALTY+ CONCLAVE & EXCELLENCE AWARDS 2022 - Design Project of the Year, Award: 12TH REALTY+ AWARDS - Themed Project of the Year 2021",
    "undivided_share_land_details": None,
    "project_theme": "Beach Theme",
    "schools": json.dumps([
        "Vibgyor International (Magarpatta) - 2.5KM", "Pawar International (Amanora) - 2KM",
        "Phoenix School (Kharadi) - 3KM", "Orbis School (Keshavnagar) - 1KM"
    ]),
    "colleges": None,
    "hospitals": json.dumps([
        "Columbia Asia (Kharadi) - 2 KM", "Nobel Hospital (Magarpatta) - 2.5 KM",
        "Sahyadri Hospital (Magarpatta) - 3 KM"
    ]),
    "it_parks_companies": json.dumps([
        "EON Free Zone (Kharadi) - 2 KM", "World Trade Centre (WTC) - 2KM", "Magarpatta IT Park - 3KM"
    ]),
    "nearby_top_places": json.dumps(["Pune Railway Station", "International Airport", "IT Parks", "Malls"]),
    "shopping_malls": json.dumps(["Season Mall - 2KM", "Amanora Mall - 2KM", "Phoenix Marketcity - 5KM"]),
    "health_fitness": None,
    "connecting_roads": json.dumps(["Pune Ring Road", "Flyover to Magarpatta"]),
    "metro_stations": json.dumps(["15 km Elevated Corridor (Ramwadi to Vanaz with extension to Kharadi)"]),
    "bus_stands": None,
    "airport_distance": None
}

# =====================
# PURVA ASPIRE
# =====================
purva_aspire = {
    "project_id": "de6b9b4c",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Aspire",
    "developer_name": "Puravankara Limited",
    "city": "Pune",
    "description": "Residential project spread over 2.3 acres at Bavdhan, Western Pune. Features 2 towers with B+G+P+17 floors. 75% carpet area loading. Near Ambrosia Resort and Spa. Metro coming up in 3 years at Chandani Chowk (1.5 km away).",
    "total_project_area_acres": 2.3,
    "open_space_percentage": None,
    "number_of_towers": 2,
    "total_units_count": 272,
    "tower_structure_details": "B + G + P + 17 Floors",
    "is_block_wing_structure": False,
    "rera_registration_number": None,
    "approval_body": "RERA",
    "launch_date": None,
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2025-09-01",
    "construction_status": "Under Construction",
    "completion_percentage": None,
    "construction_technology": "Conventional",
    "stamp_duty_percentage": 7.0,
    "registration_charges_percentage": None,
    "construction_partners": None,
    "amenities": json.dumps([
        "Multipurpose Hall", "Library Room", "Indoor Games", "GYM", "Swimming Pool"
    ]),
    "payment_plans": json.dumps(["Construction Link Payment Plan (CLP)"]),
    "unique_selling_propositions": "2.3 acres development in Western Pune, Near Ambrosia Resort and Spa, 75% carpet area (40% loading on RERA carpet), Metro coming in 3 years at Chandani Chowk (1.5 km), Oracle within 500M - Walkable, Easy connectivity to Chandani Chowk, Phoenix Market City coming in 3 years",
    "undivided_share_land_details": None,
    "project_theme": None,
    "schools": json.dumps([
        "Oxford International School - 1.8 Kms (6 mins drive)",
        "Periwinkle English Medium - 4.1 Kms (12 mins drive)",
        "Ryan International School - 1.6 Kms (19 mins drive)",
        "Sri Sri Ravishankar Bal Mandir - 2.8 Kms (8 mins drive)"
    ]),
    "colleges": json.dumps([
        "PVPIT Engineering College - 1.8 Kms (6 mins drive)",
        "Suryadatta College of Management - 4.2 Kms (10 mins drive)",
        "Indian Institute of Cost and Management Studies - 1.5 Kms (19 mins drive)",
        "Vasantdada Patil Institute of Engineering - 1.8 Kms (6 mins drive)"
    ]),
    "hospitals": json.dumps([
        "Aditya Birla Hospital - 17.8 Kms (33 mins drive)",
        "Asian Speciality Hospital - 1.7 Kms (4 mins drive)",
        "Bavdhan Medicare Centre - 1.7 Kms (4 mins drive)",
        "Chellaram Hospital - 5.6 Kms (10 mins drive)"
    ]),
    "it_parks_companies": json.dumps([
        "Oracle - 500M (Walkable)", "Hinjewadi IT Park - 16 Kms (30 mins drive)",
        "Fundtech - 3.9 Kms (9 mins drive)", "Calsoft - 5.7 Kms (11 mins drive)"
    ]),
    "nearby_top_places": json.dumps([
        "Chandani Chowk - 1.4 Kms (3 mins drive)", "Kothrud - 4.5 kms (12 mins drive)",
        "Maratha Mandir - 2.6 Kms (5 mins drive)", "Balewadi - 13 Kms (22 mins drive)",
        "Baner - 12 Kms (22 mins drive)"
    ]),
    "shopping_malls": json.dumps([
        "Phoenix Market City (coming in 3 years)", "Aditya Shagun Mall - 3.4 Kms (7 mins drive)",
        "Reliance Mall - 12.3 Kms (27 mins drive)", "Bagfull - 3.9 Kms (8 mins drive)"
    ]),
    "health_fitness": None,
    "connecting_roads": json.dumps([
        "Connecting to Chandani Chowk", "Karve Road - 7 Kms (20 mins drive)"
    ]),
    "metro_stations": json.dumps(["Metro coming at Chandani Chowk in 3 years - 1.5 km from project"]),
    "bus_stands": None,
    "airport_distance": "Pune International Airport - 22 Kms (50 mins drive)"
}

# Insert projects
projects = [purva_silversands, purva_emerald_bay, purva_aspire]
for project in projects:
    columns = ", ".join(project.keys())
    placeholders = ", ".join(["?" for _ in project])
    query = f"INSERT INTO projects ({columns}) VALUES ({placeholders})"
    cursor.execute(query, list(project.values()))
    print(f"✅ Inserted project: {project['project_name']}")

# =====================
# UNITS DATA
# =====================

# Purva Silversands Units
silversands_units = [
    {
        "unit_id": "0e6f8cae",
        "project_id": "6303abd4",
        "tenant_id": "PURVA_DEFAULT",
        "configuration_type": "2 BHK",
        "property_type": "Apartment",
        "built_up_area_sqft": None,
        "carpet_area_sqft": 804,
        "base_price": 10400000,
        "current_average_psf": 12935.32,
        "market_psf": None,
        "view_premium_details": None,
        "high_floor_premium_details": None,
        "corner_unit_premium_details": None,
        "last_price_revision_date": None,
        "last_price_change_percentage": None,
        "next_planned_revision_date": None,
        "current_festive_offers": None
    },
    {
        "unit_id": "3d881c24",
        "project_id": "6303abd4",
        "tenant_id": "PURVA_DEFAULT",
        "configuration_type": "3 BHK",
        "property_type": "Apartment",
        "built_up_area_sqft": None,
        "carpet_area_sqft": 1057,
        "base_price": 13400000,
        "current_average_psf": 12677.39,
        "market_psf": None,
        "view_premium_details": None,
        "high_floor_premium_details": None,
        "corner_unit_premium_details": None,
        "last_price_revision_date": None,
        "last_price_change_percentage": None,
        "next_planned_revision_date": None,
        "current_festive_offers": None
    }
]

# Purva Emerald Bay Ph2 Units
emerald_bay_units = [
    {
        "unit_id": "391234b5",
        "project_id": "6399a992",
        "tenant_id": "PURVA_DEFAULT",
        "configuration_type": "2 BHK Comfort",
        "property_type": "Apartment",
        "built_up_area_sqft": 903.56,
        "carpet_area_sqft": 669,
        "base_price": 8000000,
        "current_average_psf": 11958.15,
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
        "unit_id": "87efe8cb",
        "project_id": "6399a992",
        "tenant_id": "PURVA_DEFAULT",
        "configuration_type": "2 BHK Grand",
        "property_type": "Apartment",
        "built_up_area_sqft": 1117,
        "carpet_area_sqft": 828,
        "base_price": 9800000,
        "current_average_psf": 11835.75,
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
        "unit_id": "0d4dc830",
        "project_id": "6399a992",
        "tenant_id": "PURVA_DEFAULT",
        "configuration_type": "3 BHK Comfort",
        "property_type": "Apartment",
        "built_up_area_sqft": 1452,
        "carpet_area_sqft": 1062,
        "base_price": 12800000,
        "current_average_psf": 12052.73,
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

# Purva Aspire Units
aspire_units = [
    {
        "unit_id": "f36a83b1",
        "project_id": "de6b9b4c",
        "tenant_id": "PURVA_DEFAULT",
        "configuration_type": "2 BHK Grand",
        "property_type": "Apartment",
        "built_up_area_sqft": None,
        "carpet_area_sqft": 828,
        "base_price": 10900000,
        "current_average_psf": 13164.25,
        "market_psf": None,
        "view_premium_details": None,
        "high_floor_premium_details": None,
        "corner_unit_premium_details": None,
        "last_price_revision_date": None,
        "last_price_change_percentage": None,
        "next_planned_revision_date": None,
        "current_festive_offers": None
    },
    {
        "unit_id": "b047835a",
        "project_id": "de6b9b4c",
        "tenant_id": "PURVA_DEFAULT",
        "configuration_type": "2 BHK Luxe",
        "property_type": "Apartment",
        "built_up_area_sqft": None,
        "carpet_area_sqft": 928,
        "base_price": 12400000,
        "current_average_psf": 13362.07,
        "market_psf": None,
        "view_premium_details": None,
        "high_floor_premium_details": None,
        "corner_unit_premium_details": None,
        "last_price_revision_date": None,
        "last_price_change_percentage": None,
        "next_planned_revision_date": None,
        "current_festive_offers": None
    },
    {
        "unit_id": "66cae4d2",
        "project_id": "de6b9b4c",
        "tenant_id": "PURVA_DEFAULT",
        "configuration_type": "3 BR Grand",
        "property_type": "Apartment",
        "built_up_area_sqft": None,
        "carpet_area_sqft": 1153,
        "base_price": 15100000,
        "current_average_psf": 13096.27,
        "market_psf": None,
        "view_premium_details": None,
        "high_floor_premium_details": None,
        "corner_unit_premium_details": None,
        "last_price_revision_date": None,
        "last_price_change_percentage": None,
        "next_planned_revision_date": None,
        "current_festive_offers": None
    },
    {
        "unit_id": "ab938fce",
        "project_id": "de6b9b4c",
        "tenant_id": "PURVA_DEFAULT",
        "configuration_type": "3 BR Luxe",
        "property_type": "Apartment",
        "built_up_area_sqft": None,
        "carpet_area_sqft": 1226,
        "base_price": None,
        "current_average_psf": None,
        "market_psf": None,
        "view_premium_details": None,
        "high_floor_premium_details": None,
        "corner_unit_premium_details": None,
        "last_price_revision_date": None,
        "last_price_change_percentage": None,
        "next_planned_revision_date": None,
        "current_festive_offers": "Sold Out"
    }
]

# Insert all units
all_units = silversands_units + emerald_bay_units + aspire_units
for unit in all_units:
    columns = ", ".join(unit.keys())
    placeholders = ", ".join(["?" for _ in unit])
    query = f"INSERT INTO project_units ({columns}) VALUES ({placeholders})"
    cursor.execute(query, list(unit.values()))

print(f"✅ Inserted {len(silversands_units)} units for Purva Silversands")
print(f"✅ Inserted {len(emerald_bay_units)} units for Purva Emerald Bay - Ph2")
print(f"✅ Inserted {len(aspire_units)} units for Purva Aspire")

# Commit and close
conn.commit()
conn.close()

print("\n🎉 Successfully inserted all 3 Pune projects and their units!")
print(f"\nTotal: 3 projects, {len(all_units)} units")
