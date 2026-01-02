"""
Insert Bangalore Projects into Database
Adds 8 Puravankara projects in Bangalore
"""

import sqlite3
import json

# Connect to database
conn = sqlite3.connect("real_estate_data.db")
cursor = conn.cursor()

# =====================
# PURVA ZENIUM
# =====================
purva_zenium = {
    "project_id": "4ab03bc7",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Zenium",
    "developer_name": "Puravankara Limited",
    "city": "Bangalore",
    "description": "Premium residential project spread over 10.05 acres near Yelahanka Air Force Station. Features 12 towers (Phase 1: Tower 7-14, Phase 2: Tower 1-4) with G+12/13 floors. Includes Nucleus and Celestial sub-projects. Award-winning design with 80% open space.",
    "total_project_area_acres": 10.05,
    "open_space_percentage": 80.0,
    "number_of_towers": 12,
    "total_units_count": 872,
    "tower_structure_details": "G+12 & G+13 Floors",
    "is_block_wing_structure": True,
    "rera_registration_number": None,
    "approval_body": "BIAAPA",
    "launch_date": "2019-06-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": None,
    "construction_status": "RTMI / Under Construction",
    "completion_percentage": None,
    "construction_technology": "Mivan",
    "stamp_duty_percentage": 5.6,
    "registration_charges_percentage": 1.0,
    "construction_partners": "JMC",
    "amenities": json.dumps([
        "Swimming Pool", "Children Play Area", "Cafeteria", "Amphitheatre", "Squash Court",
        "Car Wash Point", "Board Game Room", "Lawn Tennis", "Mini Forest and Park Walk", "Basketball Court"
    ]),
    "payment_plans": json.dumps(["Construction Link Payment (CLP)"]),
    "unique_selling_propositions": "10.05 acres development with 80% open space, Award: 14TH REALTY+ CONCLAVE 2022 - Residential Complex of the Year, Award: 12TH REALTY+ AWARDS 2020 - Design Project of the Year, Close to Bengaluru International Airport, Hebbal Flyover just 15 minutes away, Mivan construction technology, Phase 2 metro connectivity (Nagawara to Airport)",
    "undivided_share_land_details": None,
    "project_theme": "Modern Living",
    "schools": json.dumps([
        "Canadian International School - 9.2 Km", "Stonehill International School - 8.4 Km",
        "Mallya Aditi International School - 13.9 Km", "Vidyashilp Academy - 10 Km"
    ]),
    "colleges": json.dumps(["Sri M Visvesvaraya Institute of Technology - 5.8 Km"]),
    "hospitals": json.dumps([
        "Columbia Asia Hospital, Hebbal - 14.2 Km", "Aster CMI - 16.4 Km", "Cytecare Cancer Hospital - 10.2 Km"
    ]),
    "it_parks_companies": json.dumps([
        "Manyata Tech Park - 18.5 Km", "Kirloskar Tech Park - 14.4 Km",
        "L & T Tech Park - 12.8 Km", "Ecopolis SEZ - 5.5 Km", "North Gate SEZ - 9.7 Km"
    ]),
    "nearby_top_places": json.dumps([
        "Bangalore-Hyderabad Highway", "Yelahanka Airforce Station", "Bengaluru International Airport"
    ]),
    "shopping_malls": json.dumps([
        "Decathlon - 6.2 Km", "Galleria Mall - 12.5 Km", "Proposed Phoenix Mall", "Taj Hotels - 9.8 Km"
    ]),
    "health_fitness": None,
    "connecting_roads": json.dumps(["Bellary Road (Bangalore-Hyderabad Highway)"]),
    "metro_stations": json.dumps([
        "Chikkajala Metro Station - 4.4 Km (9 mins)", "Bettahalsoor Metro Station - 5.3 Km (13 mins)",
        "Phase 2B: Nagawara to Airport"
    ]),
    "bus_stands": None,
    "airport_distance": "Close to Bengaluru International Airport"
}

# =====================
# PURVA ATMOSPHERE
# =====================
purva_atmosphere = {
    "project_id": "733be9d8",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Atmosphere",
    "developer_name": "Puravankara Limited",
    "city": "Bangalore",
    "description": "Premium residential project spread over 13 acres at Thanisandra Main Road. Features 3 towers with 33 floors and clubhouse on 34th floor. 9 acres of open space with Air Filtration Tower (Aerosphere) - First in India. Miyawaki Forest with Japanese Trees.",
    "total_project_area_acres": 13.0,
    "open_space_percentage": 69.23,
    "number_of_towers": 3,
    "total_units_count": 939,
    "tower_structure_details": "33 Floors & Clubhouse on 34th floor",
    "is_block_wing_structure": True,
    "rera_registration_number": None,
    "approval_body": "BBMP, RERA",
    "launch_date": "2020-06-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2025-06-01",
    "construction_status": "Under Construction",
    "completion_percentage": None,
    "construction_technology": "Mivan",
    "stamp_duty_percentage": 5.6,
    "registration_charges_percentage": 1.0,
    "construction_partners": "Shapoorji Pallonji",
    "amenities": json.dumps([
        "Clubhouse on 34th floor", "Half Basket Ball Court", "Multipurpose Hall",
        "Air Filtration Tower (Aerosphere) - First In India", "Viewing Gallery", "Pure Drinking Water off the Tap",
        "Yoga / Aerobics Room", "Miyawaki Forest - Japanese Trees Plantation", "Games Room",
        "Reflexology Park (Buddha Statue)", "Provision for Café", "Natural trail", "Squash Court",
        "Adventure amenity: Tunnel, Ziplines, Tree House", "Tennis Court - Two", "Sports Sphere",
        "Swimming Pool With Deck", "Cricket Practice Pitch", "Festival Plaza", "Aroma Garden",
        "Pet Park", "Kids Play Area", "Bonfire Area", "Mini Forest settings with Deck",
        "Community Garden", "Kids Pool", "Open Air Gym", "Senior Citizen Court",
        "Yoga Deck with Lawn", "Experience Walking Trail", "24/7 Security",
        "Temple of Body & Soul (Sensory Garden)", "Camping Area"
    ]),
    "payment_plans": json.dumps(["Construction Linked Payment Plan", "Maximum Funding Scheme"]),
    "unique_selling_propositions": "13 acres with 9 acres open space, 33 floors with Clubhouse on 34th floor, Air Filtration Tower (Aerosphere) - First in India, Miyawaki Forest with Japanese Trees, Pure drinking water from tap, Construction by Shapoorji Pallonji, PRR and STRR connectivity planned",
    "undivided_share_land_details": None,
    "project_theme": "Wellness Living",
    "schools": json.dumps([
        "Stone Hill International School - 15.8 Kms", "Embassy International Riding School - 17.6 Kms",
        "Delhi Public School - 8.3 Kms", "Jain Heritage School - 6.6 Kms",
        "Kensri Academy - 5.8 Kms", "Vidyashilp Academy - 7.2 Kms"
    ]),
    "colleges": json.dumps([
        "Presidency College - 8.4 Kms", "Reva University - 5.9 Kms",
        "CMR College - 7 Kms", "KNS Institute of Technology - 3 Kms"
    ]),
    "hospitals": json.dumps([
        "Aster CMI - 7.9 Kms", "Baptist Hospital - 9.7 Kms", "Columbia Asia - 8 Kms",
        "Cloudnine Asia - 8.3 Kms", "Motherhood Hospital - 6.7 Kms"
    ]),
    "it_parks_companies": json.dumps([
        "Kirloskar Business Park - 8.5 Kms", "Manyata Tech Park - 4.1 Kms", "Ecopolis SEZ - 9.9 Kms"
    ]),
    "nearby_top_places": json.dumps([
        "Hebbal - 8.5 Kms", "Airport - 25 Kms", "Whitefield - 24 Kms", "Nagavara (ORR) - 4.3 Kms"
    ]),
    "shopping_malls": json.dumps([
        "RMZ Galleria - 7.8 Kms", "Elements Mall - 2.9 Kms", "Esteem Mall - 7.8 Kms", "Orion Mall - 16.2 Kms"
    ]),
    "health_fitness": None,
    "connecting_roads": json.dumps([
        "Hennur Road - 5.8 Kms", "Hebbal - 8.5 Kms", "Kogilu Road - 7.5 Kms", "Baglur Road - 5 Kms"
    ]),
    "metro_stations": json.dumps([
        "Upcoming Nagawara Metro Station", "PRR - 4 Kms", "STRR (Satellite Town Ring Road)"
    ]),
    "bus_stands": None,
    "airport_distance": "25 Kms"
}

# =====================
# PURVA PARK HILL
# =====================
purva_park_hill = {
    "project_id": "1d0508e9",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Park Hill",
    "developer_name": "Puravankara Limited",
    "city": "Bangalore",
    "description": "Phase 2 of Purva Highland, spread over 5 acres at Kanakapura Road. Features 4 towers (A,B,C,D) with G+20 floors. 70% open space with 69% carpet area ratio.",
    "total_project_area_acres": 5.0,
    "open_space_percentage": 70.0,
    "number_of_towers": 4,
    "total_units_count": 492,
    "tower_structure_details": "G+20 Floors",
    "is_block_wing_structure": True,
    "rera_registration_number": None,
    "approval_body": "RERA",
    "launch_date": "2022-09-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2026-12-01",
    "construction_status": "Under Construction",
    "completion_percentage": None,
    "construction_technology": "MIVAN",
    "stamp_duty_percentage": 5.6,
    "registration_charges_percentage": 1.0,
    "construction_partners": "StarWorth",
    "amenities": json.dumps([
        "Reception", "Lounge", "Gymnasium", "Steam, Sauna, Massage room",
        "Yoga/Meditation/Aerobics room", "Healthcare", "Squash Court", "Provision for Supermarket",
        "Provision for Cocktail lounge", "Provision for Restaurant/kitchen", "Table Tennis Room",
        "Cards Room", "Billiards Room"
    ]),
    "payment_plans": json.dumps(["5 Lac Booking Amount", "Construction Link Payment"]),
    "unique_selling_propositions": "Phase 2 of Purva Highland, 5 acres with 70% open space, 69% carpet area ratio, MIVAN construction technology, Near Talghatpura Metro Station (2 km), Nice Road access (3.5 km)",
    "undivided_share_land_details": None,
    "project_theme": None,
    "schools": json.dumps([
        "The Valley International School - 7.4 Kms", "Sri Kumarans School - 1.3 Kms",
        "Delhi Public School - 14.3 Kms", "Alpine Public School - 7.1 Kms", "Ryan International School - 12.2 kms"
    ]),
    "colleges": json.dumps(["Yellamma Dasappa Technical Institute - 3.9 Kms"]),
    "hospitals": json.dumps([
        "Apollo Hospital - 10.9 kms", "Sagar Hospital - 13.4 Kms",
        "Wockhardt Hospital - 20 Kms", "Jayadeva Hospital - 12.65 Kms"
    ]),
    "it_parks_companies": json.dumps([
        "Infosys - 19 Kms", "Mind Tree - 11 Kms", "Wipro - 11.8 Kms",
        "Accenture - 15.6 Kms", "Honeywell - 22 Kms"
    ]),
    "nearby_top_places": json.dumps([
        "Kanakapura Rd - 1.5 kms", "JP Nagar - 10 kms", "Bannerghatta Rd - 6 kms", "Banashankari - 11 kms"
    ]),
    "shopping_malls": json.dumps([
        "Big Bazaar", "Megamart - 20 Kms", "Metro Cash & Carry - 6.7 Kms",
        "Swagat Garuda Mall (Jayanagar) - 13 Kms"
    ]),
    "health_fitness": None,
    "connecting_roads": json.dumps(["Kanakapura Rd", "Holiday Village", "Resort Road"]),
    "metro_stations": json.dumps(["Talghatpura Metro Station - 2 kms", "Nice Road - 3.5 kms"]),
    "bus_stands": None,
    "airport_distance": None
}

# =====================
# SMILING WILLOWS PH2 & PH3
# =====================
smiling_willows = {
    "project_id": "f10604ab",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Smiling Willows - Ph 2 Sparkling Springs & Ph 3 Symphony",
    "developer_name": "Puravankara Limited",
    "city": "Bangalore",
    "description": "Villa project spread over 20 acres 22 guntas at Bannerghatta Road. Phase 1 (100 villas) RTMI, Phase 2 Sparkling Springs (47 villas) and Phase 3 Symphony (60 villas) under construction. Features Temple of Body and Mind with 40 ft Buddha statue, 60% open space with 1600 trees.",
    "total_project_area_acres": 20.5,
    "open_space_percentage": 60.0,
    "number_of_towers": None,
    "total_units_count": 207,
    "tower_structure_details": "G+1 and Terrace (Villas)",
    "is_block_wing_structure": False,
    "rera_registration_number": None,
    "approval_body": "BBMP & BDA",
    "launch_date": "2022-01-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2027-06-01",
    "construction_status": "Under Construction",
    "completion_percentage": None,
    "construction_technology": "Bricks and Pillars",
    "stamp_duty_percentage": 5.6,
    "registration_charges_percentage": 1.0,
    "construction_partners": "Starworth",
    "amenities": json.dumps([
        "Temple of Body and Mind (1 acre with 40 ft Buddha statue)", "Zen Garden with Meditation Lawn",
        "Yoga Deck", "Meandering streams", "Forest setting", "Multipurpose 5-A Side Court",
        "Basketball Post", "Tennis Court", "Cricket Practice Pitch", "Water Spout/Feature Wall",
        "Water Cascade", "Water Body", "Children Play Area", "Paw Park",
        "Tallest man-made waterfall in residential project"
    ]),
    "payment_plans": json.dumps(["Construction Link Payment (CLP)"]),
    "unique_selling_propositions": "Villa project with 20+ acres, Temple of Body and Mind with 40 ft Buddha statue, 60% open area with 1600 trees and plants, Tallest man-made waterfall in residential project, Award: Realty Plus Excellence Awards 2016 - Villa Project of the Year, Metro within 2 km",
    "undivided_share_land_details": None,
    "project_theme": "Villa Living with Zen Gardens",
    "schools": json.dumps([
        "IIM Bangalore - 8.6 Km", "SIBM Bangalore - 8.6 Km", "T-John College - 3 Km",
        "Sherwood High - 3.5 Km", "NPS - 3.3 Km", "Greenwood High - 2.3 Km", "DPS - 4.9 Km"
    ]),
    "colleges": None,
    "hospitals": json.dumps([
        "Apollo - 6.3 Km", "Fortis - 6.1 Km", "Jayadeva Hospitals - 9.1 Km", "Narayana Health City - 12 Km"
    ]),
    "it_parks_companies": json.dumps([
        "IBM - 17 Km", "Oracle - 17.9 Km", "Accenture - 11.5 Km", "Electronic City - 15 Km"
    ]),
    "nearby_top_places": json.dumps(["Begur Koppa Road", "Bannerghatta Road"]),
    "shopping_malls": json.dumps([
        "Royal Meenakshi Mall - 4.1 Km", "Gopalan Innovation - 8.3 Km", "Vega City Mall - 7.7 Km"
    ]),
    "health_fitness": None,
    "connecting_roads": json.dumps(["Begur Koppa Road", "Bannerghatta Road"]),
    "metro_stations": json.dumps(["Metro station within 2 Km"]),
    "bus_stands": None,
    "airport_distance": None
}

# =====================
# PURVA TIARA
# =====================
purva_tiara = {
    "project_id": "8ba3effd",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Tiara",
    "developer_name": "Puravankara Limited",
    "city": "Bangalore",
    "description": "Luxury villa project at JP Nagar 7th Phase. Features 5BHK Villas with 8000 Sq.Ft super built-up area. Ready to Move In (RTMI).",
    "total_project_area_acres": None,
    "open_space_percentage": None,
    "number_of_towers": None,
    "total_units_count": None,
    "tower_structure_details": "Villas",
    "is_block_wing_structure": False,
    "rera_registration_number": None,
    "approval_body": "RERA",
    "launch_date": None,
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": None,
    "construction_status": "RTMI",
    "completion_percentage": 100.0,
    "construction_technology": None,
    "stamp_duty_percentage": 5.6,
    "registration_charges_percentage": 1.0,
    "construction_partners": None,
    "amenities": None,
    "payment_plans": json.dumps(["RTMI"]),
    "unique_selling_propositions": "5BHK Luxury Villas, JP Nagar 7th Phase location, Ready to Move In",
    "undivided_share_land_details": None,
    "project_theme": "Luxury Villas",
    "schools": None,
    "colleges": None,
    "hospitals": None,
    "it_parks_companies": None,
    "nearby_top_places": json.dumps(["JP Nagar 7th Phase"]),
    "shopping_malls": None,
    "health_fitness": None,
    "connecting_roads": None,
    "metro_stations": None,
    "bus_stands": None,
    "airport_distance": None
}

# =====================
# PURVA MERAKI
# =====================
purva_meraki = {
    "project_id": "106890b0",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Meraki",
    "developer_name": "Puravankara Limited",
    "city": "Bangalore",
    "description": "Uber luxury residential project spread over 1 Acre 2 Guntas at HSR Layout Sector 2, near Somsundrapalya Lake. Features 44 apartments in 3 wings with 2B+G+8+T floors. 76% open space with 67% carpet area ratio.",
    "total_project_area_acres": 1.05,
    "open_space_percentage": 76.0,
    "number_of_towers": 3,
    "total_units_count": 44,
    "tower_structure_details": "2B + G + 8 + T",
    "is_block_wing_structure": True,
    "rera_registration_number": None,
    "approval_body": "RERA, BBMP",
    "launch_date": "2022-10-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2026-10-01",
    "construction_status": "Under Construction",
    "completion_percentage": None,
    "construction_technology": "Mivan Technology with Inner walls as block work",
    "stamp_duty_percentage": 5.65,
    "registration_charges_percentage": 1.0,
    "construction_partners": "SAI Developers",
    "amenities": json.dumps([
        "Pool with Infinity edge", "Kids Pool", "Seating Area", "Double side Lounge seating",
        "Kids Zone - Play Lawn, Floor Games, Arts and Craft Deck", "Acupressure sky walk",
        "Youth Zone - Hammock Zone, Table Tennis, Fire Place, Stage, Party Lawn",
        "Wellness Zone - Yoga & Meditation Lawn, Sunset viewing deck", "Gymnasium",
        "Outdoor amenities - Reflexology Path, Water cascade"
    ]),
    "payment_plans": json.dumps(["Construction Link Payment Plan"]),
    "unique_selling_propositions": "44 Uber luxury apartments, 76% open space, Near Somsundrapalya Lake, HSR Layout prime location, Kudlu gate metro station - Operational, 2 Car Parks per unit",
    "undivided_share_land_details": None,
    "project_theme": "Uber Luxury",
    "schools": json.dumps([
        "VIBGYOR High School HSR Layout - 1 KM", "PEP School Montessori - 1 KM", "SRI SAIRAM VIDYAMANDIRA - 500 M"
    ]),
    "colleges": json.dumps([
        "The Oxford College of Engineering - 3 KM", "ISBR College - 8 KM", "Dayananda Saraswathi University - 2 KM"
    ]),
    "hospitals": json.dumps([
        "Hamilton Hospital - 300 M", "Narayana Multispeciality Hospital - 1 KM", "Manipal Hospital - 4.5 KM"
    ]),
    "it_parks_companies": json.dumps([
        "EBC Space 4 - 300 M", "BHIVE Workspace - 1 KM", "Hustlehub Tech Park - 700 M",
        "Microsoft Corporation - 5 KM", "RMZ Ecospace - 6 KM"
    ]),
    "nearby_top_places": json.dumps(["HSR Layout", "Somsundrapalya Lake"]),
    "shopping_malls": json.dumps([
        "Cult Fitness - 1.5 KM", "Soul Space Spirit Central Mall - 6 KM", "Nexus Mall - 5.5 KM"
    ]),
    "health_fitness": None,
    "connecting_roads": json.dumps(["Kudlu road", "27th main road"]),
    "metro_stations": json.dumps(["Kudlu gate metro station - Operational"]),
    "bus_stands": None,
    "airport_distance": None
}

# =====================
# PURVA BLUBELLE
# =====================
purva_blubelle = {
    "project_id": "6927bb1d",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Blubelle",
    "developer_name": "Puravankara Limited",
    "city": "Bangalore",
    "description": "Residential project spread over 3.85 acres at Magadi Main Road, West Bangalore. Features 2 towers (A: G+31, B: G+32 floors) with 378 units. 80% open space with 17 themed gardens and 50+ luxurious amenities. Metro station 50m away.",
    "total_project_area_acres": 3.85,
    "open_space_percentage": 80.0,
    "number_of_towers": 2,
    "total_units_count": 378,
    "tower_structure_details": "Tower A G+31 floors, Tower B G+32 floors",
    "is_block_wing_structure": True,
    "rera_registration_number": None,
    "approval_body": "BBMP, RERA",
    "launch_date": "2023-04-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2028-06-01",
    "construction_status": "Under Construction",
    "completion_percentage": None,
    "construction_technology": "Mivan & Conventional (Hybrid)",
    "stamp_duty_percentage": 1.0,
    "registration_charges_percentage": 5.65,
    "construction_partners": "Creative Projects & Contracts Pvt. Ltd",
    "amenities": json.dumps([
        "17 Themed Gardens", "50+ luxurious amenities", "Fruit Garden", "Herbal Garden",
        "Wine Garden", "Bee Garden", "Vegetable Garden", "Butterfly Garden", "Festival Garden",
        "Temple Garden", "Tennis/Multipurpose Court", "Outdoor Gymnasium", "Meditation Lawn",
        "Party Lawn", "Cricket Practice Net", "Kids Play Area", "Swimming Pool", "Multipurpose Hall",
        "Indoor Games Room", "Gymnasium", "Yoga Space", "Co-working Space", "Pet Park",
        "Skating Rink", "Rock Climbing Wall"
    ]),
    "payment_plans": json.dumps(["Construction Linked Payment Plan"]),
    "unique_selling_propositions": "17 themed gardens with diverse flora, 50+ luxurious amenities, 80% open space, Magadi Road Metro Station - 50m (Operational), GT World Mall - 550m, 65% carpet area",
    "undivided_share_land_details": None,
    "project_theme": "Garden Living",
    "schools": json.dumps([
        "Gurukula International School - 500m", "Sophia High School - 5.3 km",
        "Bishop Cotton Boys School - 8.2 km", "The Brigade School - 6 km"
    ]),
    "colleges": None,
    "hospitals": json.dumps([
        "Gayathri Hospital - 1.7 km", "Mallige Hospital - 4.1 km", "Manipal Northside Hospital - 5.2 km"
    ]),
    "it_parks_companies": json.dumps([
        "Bagmane Pallavi Towers", "World Trade Center - 5.5 km", "Rajaji Nagar IT Park - 1.9 km"
    ]),
    "nearby_top_places": json.dumps(["Magadi Road", "Chickpet - 5.3 km"]),
    "shopping_malls": json.dumps([
        "GT World Mall - 550m", "Lulu Hypermarket - 2 km", "Dmart - 1.1 km", "Orion Mall - 5.5 km"
    ]),
    "health_fitness": None,
    "connecting_roads": json.dumps(["Magadi Main Road"]),
    "metro_stations": json.dumps(["Magadi Road Metro Station - Operational (50m)"]),
    "bus_stands": None,
    "airport_distance": "Kempagowda International Airport - 36 km"
}

# =====================
# PURVA ORIENT GRAND
# =====================
purva_orient_grand = {
    "project_id": "20070083",
    "tenant_id": "PURVA_DEFAULT",
    "project_name": "Purva Orient Grand",
    "developer_name": "Puravankara Limited",
    "city": "Bangalore",
    "description": "WorldHome Collection ultra-luxury project at Lalbagh Road, off Richmond Road. 24-story landmark on 1.15 acres with 97 residences. Designed by Andy Fisher (Singapore Changi Airport architect). Features infinity pool on 25th level, views of Lalbagh Gardens, Cubbon Park, UB City. Terrace clubhouse modelled after London Crystal Palace.",
    "total_project_area_acres": 1.15,
    "open_space_percentage": 65.0,
    "number_of_towers": 1,
    "total_units_count": 97,
    "tower_structure_details": "G + 24 Floors",
    "is_block_wing_structure": False,
    "rera_registration_number": None,
    "approval_body": "BBMP, RERA",
    "launch_date": "2022-02-01",
    "sales_launch_date": None,
    "construction_start_date": None,
    "rera_possession_date": None,
    "estimated_possession_date": "2027-06-01",
    "construction_status": "Under Construction",
    "completion_percentage": None,
    "construction_technology": "RCC",
    "stamp_duty_percentage": 6.0,
    "registration_charges_percentage": None,
    "construction_partners": "KAP India",
    "amenities": json.dumps([
        "Infinity Pool on 25th level", "Kids Pool", "Private Terrace", "Smoking Zone",
        "The Fete - Multipurpose hall overlooking Lalbagh Park", "Dovecote - Private dining inspired by Paris rooftops",
        "Fire pit Lounge", "Moon decks", "Private dining areas", "Rose and Cypress Oxygenated Clubhouse",
        "Aura Spa and Treatment Rooms", "Body CORE Fitness studio (Pilates, HIIT, TRX, Peloton)",
        "Salon", "Manicure Station", "Whiskey Lounge", "Larder Room", "Games Salon",
        "High Table for 8", "Zumba Deck", "Kinetic Garden", "Yoga Deck", "Healing Garden",
        "Mini Golf", "Paw Pet Park", "Koi Pond", "Half Basketball Court"
    ]),
    "payment_plans": json.dumps(["Construction Link Payment"]),
    "unique_selling_propositions": "WorldHome Collection - Ultra Luxury, Designed by Andy Fisher (Singapore Changi Airport architect), Views of Lalbagh, Cubbon Park, UB City, Vidhan Soudha, Infinity Pool on 25th level, Terrace Clubhouse modelled after London Crystal Palace, BluNex Technology - Home automation, biometric locks, video doorbell, Vaastu Compliant with North/East Entry, No common walls - 4 apartments per floor, Purified drinking water from kitchen tap, 1% benefit for women homebuyers",
    "undivided_share_land_details": None,
    "project_theme": "Ultra Luxury - WorldHome Collection",
    "schools": json.dumps(["Bishop Cotton Boys School", "The Brigade School"]),
    "colleges": json.dumps(["Government College of Pharmacy"]),
    "hospitals": json.dumps(["Mallya Hospital"]),
    "it_parks_companies": None,
    "nearby_top_places": json.dumps([
        "Lalbagh Botanical Gardens", "Cubbon Park", "UB City Mall", "Richmond Road",
        "Double Road", "Passport Office", "Vidhan Soudha"
    ]),
    "shopping_malls": json.dumps(["UB City Mall", "ITC Gardenia", "JW Marriott"]),
    "health_fitness": None,
    "connecting_roads": json.dumps(["Lalbagh Main Road", "Richmond Road"]),
    "metro_stations": None,
    "bus_stands": None,
    "airport_distance": None
}

# Insert all projects
projects = [
    purva_zenium, purva_atmosphere, purva_park_hill, smiling_willows,
    purva_tiara, purva_meraki, purva_blubelle, purva_orient_grand
]

for project in projects:
    columns = ", ".join(project.keys())
    placeholders = ", ".join(["?" for _ in project])
    query = f"INSERT INTO projects ({columns}) VALUES ({placeholders})"
    cursor.execute(query, list(project.values()))
    print(f"✅ Inserted project: {project['project_name']}")

# =====================
# UNITS DATA
# =====================

all_units = []

# Purva Zenium Units
zenium_units = [
    {"unit_id": "407141da", "project_id": "4ab03bc7", "tenant_id": "PURVA_DEFAULT", "configuration_type": "2 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1061, "base_price": 9800000, "current_average_psf": 9236.57, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "Elysian Fields"},
    {"unit_id": "e5b9117c", "project_id": "4ab03bc7", "tenant_id": "PURVA_DEFAULT", "configuration_type": "2 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1044, "base_price": 10100000, "current_average_psf": 9674.33, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "Phase II"},
    {"unit_id": "20b96c93", "project_id": "4ab03bc7", "tenant_id": "PURVA_DEFAULT", "configuration_type": "2 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1272, "base_price": 13500000, "current_average_psf": 10613.21, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "Nucleus"},
    {"unit_id": "6418bdd6", "project_id": "4ab03bc7", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1725, "base_price": 16800000, "current_average_psf": 9739.13, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "Nucleus"},
    {"unit_id": "3b80520e", "project_id": "4ab03bc7", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1763, "base_price": 17300000, "current_average_psf": 9812.82, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "Nucleus"}
]

# Purva Atmosphere Units
atmosphere_units = [
    {"unit_id": "54ad4641", "project_id": "733be9d8", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK Comfort", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1680, "base_price": 28000000, "current_average_psf": 16666.67, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "bb351a9e", "project_id": "733be9d8", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK Grand", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 2005, "base_price": 31500000, "current_average_psf": 15710.72, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None}
]

# Park Hill Units
park_hill_units = [
    {"unit_id": "d32111e3", "project_id": "1d0508e9", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK Grand", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1567, "base_price": 12300000, "current_average_psf": 7849.39, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "Ground Floor no Balcony"},
    {"unit_id": "ab826428", "project_id": "1d0508e9", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK Lux", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1743, "base_price": 17000000, "current_average_psf": 9753.3, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "Ground Floor no Balcony"},
    {"unit_id": "e1afbecc", "project_id": "1d0508e9", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK Grand", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1893, "base_price": 20200000, "current_average_psf": 10670.89, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "First Floor with 3 balcony"}
]

# Smiling Willows Units
willows_units = [
    {"unit_id": "e3a7b585", "project_id": "f10604ab", "tenant_id": "PURVA_DEFAULT", "configuration_type": "Type A - 4BR Villa", "property_type": "Villa", "built_up_area_sqft": None, "carpet_area_sqft": 5466, "base_price": None, "current_average_psf": None, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "Sold Out"},
    {"unit_id": "da29a71e", "project_id": "f10604ab", "tenant_id": "PURVA_DEFAULT", "configuration_type": "Type B - 3BR Villa", "property_type": "Villa", "built_up_area_sqft": None, "carpet_area_sqft": 4612, "base_price": 63200000, "current_average_psf": 13703.38, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "54ff15e3", "project_id": "f10604ab", "tenant_id": "PURVA_DEFAULT", "configuration_type": "Type C - 3BR Villa", "property_type": "Villa", "built_up_area_sqft": None, "carpet_area_sqft": 3622, "base_price": 51200000, "current_average_psf": 14135.84, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "3b5c3175", "project_id": "f10604ab", "tenant_id": "PURVA_DEFAULT", "configuration_type": "Type D - 3BR Villa", "property_type": "Villa", "built_up_area_sqft": None, "carpet_area_sqft": 3333, "base_price": 46600000, "current_average_psf": 13981.4, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None}
]

# Purva Tiara Units
tiara_units = [
    {"unit_id": "57435ac8", "project_id": "8ba3effd", "tenant_id": "PURVA_DEFAULT", "configuration_type": "5 BHK Villa", "property_type": "Villa", "built_up_area_sqft": None, "carpet_area_sqft": 8000, "base_price": None, "current_average_psf": None, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": "Sold Out"}
]

# Purva Meraki Units
meraki_units = [
    {"unit_id": "39411c02", "project_id": "106890b0", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK Grand", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 2523, "base_price": 39000000, "current_average_psf": 15457.79, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "d3aad848", "project_id": "106890b0", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK Grand", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 2591, "base_price": 40000000, "current_average_psf": 15438.05, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "3d28c81f", "project_id": "106890b0", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK Lux", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 2730, "base_price": 45400000, "current_average_psf": 16630.04, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "f07184b3", "project_id": "106890b0", "tenant_id": "PURVA_DEFAULT", "configuration_type": "4 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 3696, "base_price": 56000000, "current_average_psf": 15151.52, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None}
]

# Purva Blubelle Units
blubelle_units = [
    {"unit_id": "03d0c67c", "project_id": "6927bb1d", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1434, "base_price": 22500000, "current_average_psf": 15690.38, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "8fe27596", "project_id": "6927bb1d", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 BHK", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1630, "base_price": 25000000, "current_average_psf": 15337.42, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None}
]

# Purva Orient Grand Units
orient_grand_units = [
    {"unit_id": "5bb009ad", "project_id": "20070083", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 Bedroom", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 1992, "base_price": 60000000, "current_average_psf": 30120.48, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "b7c4c17f", "project_id": "20070083", "tenant_id": "PURVA_DEFAULT", "configuration_type": "3 Bedroom", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 2262, "base_price": 80000000, "current_average_psf": 35366.93, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "2ed04c11", "project_id": "20070083", "tenant_id": "PURVA_DEFAULT", "configuration_type": "4 Bedroom Elegance", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 2325, "base_price": 75000000, "current_average_psf": 32258.06, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "c83b2509", "project_id": "20070083", "tenant_id": "PURVA_DEFAULT", "configuration_type": "4 Bedroom Luxury", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 2740, "base_price": 81500000, "current_average_psf": 29744.53, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None},
    {"unit_id": "bed8f121", "project_id": "20070083", "tenant_id": "PURVA_DEFAULT", "configuration_type": "4 Grandeur Luxury", "property_type": "Apartment", "built_up_area_sqft": None, "carpet_area_sqft": 3228, "base_price": 99000000, "current_average_psf": 30669.14, "market_psf": None, "view_premium_details": None, "high_floor_premium_details": None, "corner_unit_premium_details": None, "last_price_revision_date": None, "last_price_change_percentage": None, "next_planned_revision_date": None, "current_festive_offers": None}
]

# Combine all units
all_units = (zenium_units + atmosphere_units + park_hill_units + willows_units +
             tiara_units + meraki_units + blubelle_units + orient_grand_units)

# Insert all units
for unit in all_units:
    columns = ", ".join(unit.keys())
    placeholders = ", ".join(["?" for _ in unit])
    query = f"INSERT INTO project_units ({columns}) VALUES ({placeholders})"
    cursor.execute(query, list(unit.values()))

print(f"\n✅ Inserted {len(zenium_units)} units for Purva Zenium")
print(f"✅ Inserted {len(atmosphere_units)} units for Purva Atmosphere")
print(f"✅ Inserted {len(park_hill_units)} units for Purva Park Hill")
print(f"✅ Inserted {len(willows_units)} units for Smiling Willows")
print(f"✅ Inserted {len(tiara_units)} units for Purva Tiara")
print(f"✅ Inserted {len(meraki_units)} units for Purva Meraki")
print(f"✅ Inserted {len(blubelle_units)} units for Purva Blubelle")
print(f"✅ Inserted {len(orient_grand_units)} units for Purva Orient Grand")

# Commit and close
conn.commit()
conn.close()

print("\n🎉 Successfully inserted all 8 Bangalore projects and their units!")
print(f"\nTotal: 8 projects, {len(all_units)} units")
