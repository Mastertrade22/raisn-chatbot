"""
Database Interface Module
Handles all database operations and schema management
"""

import sqlite3
import json
import os
from typing import List, Tuple, Optional
from config import DB_PATH
from real_estate_db import create_real_estate_db


class DatabaseInterface:
    """Interface for database operations"""

    def __init__(self, db_path: str = None):
        """
        Initialize database interface

        Args:
            db_path: Optional custom database path (defaults to config)
        """
        self.db_path = db_path or DB_PATH
        self._ensure_database_exists()

    def _ensure_database_exists(self) -> None:
        """Create database if it doesn't exist"""
        if not os.path.exists(self.db_path):
            print(f"📁 Database not found at {self.db_path}, creating...")
            create_real_estate_db()
            print("✅ Database created successfully!")

    def execute_query(self, sql_query: str) -> Tuple[List, Optional[str]]:
        """
        Execute SQL query and return results

        Args:
            sql_query: SQL query string

        Returns:
            Tuple of (results, error_message)
            - results: List of tuples with query results (empty if error)
            - error_message: Error string if failed, None if successful
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(sql_query)
            results = cursor.fetchall()
            conn.close()
            return results, None
        except Exception as e:
            return [], str(e)

    def get_schema(self, tenant_id: Optional[str] = None) -> str:
        """
        Get database schema as formatted string

        Args:
            tenant_id: Optional tenant ID for filtering (None means no filtering)

        Returns:
            str: Formatted database schema with tenant context
        """
        tenant_filter_note = ""
        if tenant_id:
            tenant_filter_note = f"""
IMPORTANT TENANT FILTERING:
- Current tenant_id: '{tenant_id}'
- ALWAYS add: WHERE tenant_id = '{tenant_id}' to filter by this specific client
- For projects table: WHERE tenant_id = '{tenant_id}'
- For project_units table: WHERE tenant_id = '{tenant_id}'
- For JOINs: Add tenant_id filter to both tables or the result set
"""

        return f"""
DATABASE: real_estate_data.db
{tenant_filter_note}
TABLE: projects
Columns:
- project_id (TEXT PRIMARY KEY)
- tenant_id (TEXT NOT NULL) - Client/tenant identifier
- project_name (TEXT NOT NULL) - Name of the real estate project
- developer_name (TEXT NOT NULL) - Builder/developer name
- city (TEXT NOT NULL)
- description (TEXT)
- total_project_area_acres (DECIMAL)
- open_space_percentage (DECIMAL)
- number_of_towers (INTEGER)
- total_units_count (INTEGER)
- tower_structure_details (TEXT)
- is_block_wing_structure (BOOLEAN)
- rera_registration_number (TEXT)
- approval_body (TEXT)
- launch_date, sales_launch_date, construction_start_date (DATE)
- rera_possession_date, estimated_possession_date (DATE)
- construction_status (VARCHAR) - Values: 'Under Construction', 'Completed', 'Ready to Move'
- completion_percentage (DECIMAL)
- construction_technology (TEXT)
- stamp_duty_percentage, registration_charges_percentage (DECIMAL)
- construction_partners (TEXT)
- amenities, payment_plans, unique_selling_propositions (TEXT - JSON)
- schools, colleges, hospitals, it_parks_companies (TEXT)
- nearby_top_places, shopping_malls, health_fitness (TEXT)
- connecting_roads, metro_stations, bus_stands, airport_distance (TEXT)
- created_at, modified_at (TIMESTAMP)

TABLE: project_units
Columns:
- unit_id (TEXT PRIMARY KEY)
- project_id (TEXT - FOREIGN KEY to projects.project_id)
- tenant_id (TEXT NOT NULL) - Client/tenant identifier
- configuration_type (VARCHAR) - Examples: '2BHK', '3BHK', '4BHK', 'Villa'
- property_type (VARCHAR) - Examples: 'Apartment', 'Villa', 'Penthouse'
- built_up_area_sqft (DECIMAL)
- carpet_area_sqft (DECIMAL)
- base_price (DECIMAL) - Price in currency
- current_average_psf (DECIMAL) - Price per square foot
- market_psf (DECIMAL)
- view_premium_details, high_floor_premium_details, corner_unit_premium_details (TEXT)
- last_price_revision_date, next_planned_revision_date (DATE)
- last_price_change_percentage (DECIMAL)
- current_festive_offers (TEXT)
- created_at (TIMESTAMP)

IMPORTANT SQL GUIDELINES:
- Use JOIN to combine project and unit information
- For project queries: SELECT * FROM projects WHERE ...
- For unit queries: SELECT * FROM project_units WHERE ...
- For combined queries: SELECT p.project_name, u.* FROM projects p JOIN project_units u ON p.project_id = u.project_id WHERE ...
- IMPORTANT: Use LIKE for pattern matching on text fields (developer_name, project_name, client names)
  Example: WHERE developer_name LIKE '%Casagrand%' or WHERE project_name LIKE '%Purva%'
- Configuration type pattern matching: WHERE configuration_type LIKE '%3BHK%'
- Count projects: SELECT COUNT(*) FROM projects
- Count units: SELECT COUNT(*) FROM project_units
"""

    def test_connection(self) -> bool:
        """
        Test database connection

        Returns:
            bool: True if connection successful
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM projects")
            result = cursor.fetchone()
            conn.close()
            return True
        except Exception as e:
            print(f"Database connection test failed: {e}")
            return False

    def get_table_counts(self) -> dict:
        """
        Get row counts for all tables

        Returns:
            dict: Table names mapped to row counts
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM projects")
            projects_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM project_units")
            units_count = cursor.fetchone()[0]

            conn.close()

            return {
                "projects": projects_count,
                "project_units": units_count
            }
        except Exception as e:
            print(f"Error getting table counts: {e}")
            return {}


# Singleton instance for easy import
db_interface = DatabaseInterface()


def get_database_schema(tenant_id: Optional[str] = None) -> str:
    """
    Get database schema (convenience function)

    Args:
        tenant_id: Optional tenant ID for filtering

    Returns:
        str: Database schema
    """
    return db_interface.get_schema(tenant_id)


def execute_sql(sql_query: str) -> Tuple[List, Optional[str]]:
    """
    Execute SQL query (convenience function)

    Args:
        sql_query: SQL query string

    Returns:
        Tuple of (results, error_message)
    """
    return db_interface.execute_query(sql_query)
