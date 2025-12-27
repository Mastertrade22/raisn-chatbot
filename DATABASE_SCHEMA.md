# Real Estate Database Schema Documentation

## Overview

A comprehensive real estate database designed for a SaaS multi-tenant chatbot system with two main tables: **projects** and **project_units**.

## Database: real_estate_data.db

---

## Table 1: projects

Stores real estate project information including location, construction status, amenities, and connectivity.

### Schema

#### Core Identity
| Column | Type | Description |
|--------|------|-------------|
| project_id | TEXT PRIMARY KEY | Unique identifier (e.g., "proj-001") |
| tenant_id | TEXT | SaaS client identifier |
| project_name | TEXT | Name of the project |
| developer_name | TEXT | Builder/developer name |
| city | TEXT | City location |
| description | TEXT | Project description/USP |

#### Structure & Area
| Column | Type | Description |
|--------|------|-------------|
| total_project_area_acres | DECIMAL(10,2) | Total area in acres |
| open_space_percentage | DECIMAL(5,2) | % of open/green space |
| number_of_towers | INTEGER | Count of towers |
| total_units_count | INTEGER | Total residential units |
| tower_structure_details | TEXT | e.g., "G+20 floors" |
| is_block_wing_structure | BOOLEAN | Block/wing layout flag |

#### Legal & Dates
| Column | Type | Description |
|--------|------|-------------|
| rera_registration_number | TEXT | RERA registration number |
| approval_body | TEXT | Approving authority (BBMP, BDA, etc.) |
| launch_date | DATE | Project launch date |
| sales_launch_date | DATE | Sales start date |
| construction_start_date | DATE | Construction start date |
| rera_possession_date | DATE | RERA possession date |
| estimated_possession_date | DATE | Estimated possession date |

#### Construction Status
| Column | Type | Description |
|--------|------|-------------|
| construction_status | VARCHAR(50) | Status (Under Construction, Ready to Move, etc.) |
| completion_percentage | DECIMAL(5,2) | Completion % (0-100) |
| construction_technology | TEXT | Technology used (Mivan, Precast, etc.) |

#### Financials & Partners
| Column | Type | Description |
|--------|------|-------------|
| stamp_duty_percentage | DECIMAL(5,2) | Stamp duty % |
| registration_charges_percentage | DECIMAL(5,2) | Registration charges % |
| construction_partners | TEXT | List of construction partners |

#### Marketing & Features (JSON fields)
| Column | Type | Description |
|--------|------|-------------|
| amenities | TEXT (JSON) | Array of amenities |
| payment_plans | TEXT (JSON) | Object of payment plans |
| unique_selling_propositions | TEXT | USP details |
| undivided_share_land_details | TEXT | UDS information |
| project_theme | TEXT | Theme (Mediterranean, Modern, etc.) |

#### Connectivity (JSON fields)
| Column | Type | Description |
|--------|------|-------------|
| schools | TEXT (JSON) | Array with {name, distance} |
| colleges | TEXT (JSON) | Array with {name, distance} |
| hospitals | TEXT (JSON) | Array with {name, distance} |
| it_parks_companies | TEXT (JSON) | Array with {name, distance} |
| nearby_top_places | TEXT (JSON) | Array with {name, distance} |
| shopping_malls | TEXT (JSON) | Array with {name, distance} |
| health_fitness | TEXT (JSON) | Array with {name, distance} |
| connecting_roads | TEXT (JSON) | Array of road names |
| metro_stations | TEXT (JSON) | Array with {name, distance} |
| bus_stands | TEXT (JSON) | Array with {name, distance} |
| airport_distance | TEXT | Distance from airport |

#### Metadata
| Column | Type | Description |
|--------|------|-------------|
| created_at | TIMESTAMP | Record creation time |
| modified_at | TIMESTAMP | Last modification time |

### Indexes
- `idx_projects_tenant` on `tenant_id`

---

## Table 2: project_units

Stores individual unit information with pricing, areas, and current offers.

### Schema

#### Core Fields
| Column | Type | Description |
|--------|------|-------------|
| unit_id | TEXT PRIMARY KEY | Unique identifier (e.g., "unit-001") |
| project_id | TEXT FK | References projects(project_id) |
| tenant_id | TEXT | SaaS client identifier |

#### Classification
| Column | Type | Description |
|--------|------|-------------|
| configuration_type | VARCHAR(50) | e.g., "2BHK", "3BHK", "4BHK" |
| property_type | VARCHAR(50) | e.g., "Apartment", "Villa", "Penthouse" |

#### Areas
| Column | Type | Description |
|--------|------|-------------|
| built_up_area_sqft | DECIMAL(10,2) | Built-up area in sq ft |
| carpet_area_sqft | DECIMAL(10,2) | Carpet area in sq ft |

#### Pricing
| Column | Type | Description |
|--------|------|-------------|
| base_price | DECIMAL(15,2) | Base price in INR |
| current_average_psf | DECIMAL(10,2) | Current price per sq ft |
| market_psf | DECIMAL(10,2) | Market price per sq ft |

#### Premiums & Variations
| Column | Type | Description |
|--------|------|-------------|
| view_premium_details | TEXT | View-based premiums description |
| high_floor_premium_details | TEXT | Floor-based premiums description |
| corner_unit_premium_details | TEXT | Corner unit premiums description |

#### Offers & Revisions
| Column | Type | Description |
|--------|------|-------------|
| last_price_revision_date | DATE | Last price change date |
| last_price_change_percentage | DECIMAL(5,2) | Last price change % |
| next_planned_revision_date | DATE | Next planned revision date |
| current_festive_offers | TEXT | Current festive offers description |

#### Metadata
| Column | Type | Description |
|--------|------|-------------|
| created_at | TIMESTAMP | Record creation time |

### Indexes
- `idx_units_project` on `project_id`
- `idx_units_tenant` on `tenant_id`

---

## Sample Data

### Projects (4 total)

1. **Brigade Eldorado** (Bagalur)
   - 8 towers, 1080 units
   - 35.5% complete
   - 75% open space
   - 3 unit types: 2BHK, 3BHK, 4BHK

2. **Prestige Lavender Fields** (Whitefield)
   - 12 towers, 1520 units
   - 62% complete
   - 80% open space
   - 3 unit types: 2BHK, 3BHK, 4BHK Penthouse

3. **Sobha Dream Acres** (Panathur)
   - Villas, 280 units
   - 89.5% complete (Nearing Completion)
   - 65% open space
   - 2 villa types: 3BHK, 4BHK

4. **Godrej Woodsville** (Devanahalli)
   - 6 towers, 720 units
   - 18% complete
   - 70% open space
   - 2 unit types: 2BHK, 3BHK

### Units (10 total configurations)

**Price Range:**
- Cheapest: ₹55 lakhs (Godrej Woodsville 2BHK)
- Most Expensive: ₹2.8 crores (Prestige Lavender Fields Penthouse)

**PSF Range:**
- Lowest: ₹4,661/sqft (Godrej Woodsville)
- Highest: ₹8,833/sqft (Sobha Dream Acres Villa)

---

## Common Query Patterns

### Projects Queries

```sql
-- Count projects by status
SELECT construction_status, COUNT(*)
FROM projects
GROUP BY construction_status;

-- Projects with high open space
SELECT project_name, open_space_percentage
FROM projects
WHERE open_space_percentage > 75
ORDER BY open_space_percentage DESC;

-- Projects by developer
SELECT project_name, construction_status, completion_percentage
FROM projects
WHERE developer_name LIKE '%Prestige%';

-- Near airport projects
SELECT project_name, airport_distance, developer_name
FROM projects
WHERE airport_distance LIKE '%km from%'
ORDER BY CAST(SUBSTR(airport_distance, 1, INSTR(airport_distance, ' ') - 1) AS INTEGER);
```

### Units Queries

```sql
-- Average PSF by configuration
SELECT configuration_type, AVG(current_average_psf) as avg_psf, COUNT(*) as count
FROM project_units
GROUP BY configuration_type;

-- Cheapest units by type
SELECT p.project_name, u.configuration_type, u.base_price, u.current_average_psf
FROM project_units u
JOIN projects p ON u.project_id = p.project_id
WHERE u.configuration_type = '2BHK'
ORDER BY u.base_price ASC
LIMIT 5;

-- Units with festive offers
SELECT p.project_name, u.configuration_type, u.base_price, u.current_festive_offers
FROM project_units u
JOIN projects p ON u.project_id = p.project_id
WHERE u.current_festive_offers IS NOT NULL;

-- Price comparison: Base vs Market
SELECT p.project_name, u.configuration_type,
       u.base_price,
       u.current_average_psf,
       u.market_psf,
       ((u.market_psf - u.current_average_psf) / u.current_average_psf * 100) as discount_percentage
FROM project_units u
JOIN projects p ON u.project_id = p.project_id
ORDER BY discount_percentage DESC;
```

### Combined Queries

```sql
-- Projects with units and pricing
SELECT p.project_name, p.city, p.construction_status,
       u.configuration_type, u.property_type, u.base_price
FROM projects p
LEFT JOIN project_units u ON p.project_id = u.project_id
ORDER BY p.project_name, u.base_price;

-- Investment analysis
SELECT p.project_name,
       p.completion_percentage,
       u.configuration_type,
       u.base_price,
       u.current_average_psf,
       p.estimated_possession_date
FROM projects p
JOIN project_units u ON p.project_id = u.project_id
WHERE p.construction_status = 'Under Construction'
ORDER BY p.completion_percentage DESC;
```

---

## Natural Language Query Examples

The chatbot can handle these types of questions:

### Basic Queries
- "How many projects are under construction?"
- "Which projects have more than 75% open space?"
- "List all projects in Bangalore"

### Pricing Queries
- "What is the cheapest 2BHK apartment?"
- "Show me all 3BHK units with their prices"
- "What is the average price per sqft for villas?"

### Comparison Queries
- "Compare prices between Prestige and Brigade projects"
- "Which developer offers the best value for 3BHK?"

### Offer Queries
- "Which units have festive offers?"
- "Show me projects with discounts"

### Location Queries
- "List projects near the airport"
- "Show me projects in Whitefield area"
- "Which projects are close to IT parks?"

### Complex Queries
- "Show me ready-to-move villas under 2 crores"
- "Find 3BHK apartments near metro stations with completion above 50%"
- "Which projects by Sobha have units with current offers?"

---

## JSON Field Examples

### Amenities
```json
[
  "Swimming Pool",
  "Gymnasium",
  "Clubhouse",
  "Tennis Court"
]
```

### Payment Plans
```json
{
  "Construction Linked": "10:20:70 plan",
  "Subvention": "20:80 plan",
  "Flexi": "30:70 plan"
}
```

### Schools (with distance)
```json
[
  {"name": "Ryan International School", "distance": "2.5 km"},
  {"name": "Greenwood High", "distance": "3.2 km"}
]
```

---

## Multi-Tenant Support

Each record includes `tenant_id` for SaaS isolation:
- Filter all queries by tenant_id for data isolation
- Indexes on tenant_id for performance
- Suitable for multi-tenant real estate platforms

---

## Usage with LangGraph Chatbot

This database schema is optimized for:
1. **Natural language queries** - Clear, descriptive column names
2. **LLM SQL generation** - Example queries in schema description
3. **JSON support** - Flexible storage for arrays and objects
4. **Real-world data** - Actual Bangalore projects with realistic pricing

See [app.py](app.py) for the LangGraph implementation that uses this database.
