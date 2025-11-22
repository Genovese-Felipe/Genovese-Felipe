import clickhouse_connect
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_client():
    """Connects to ClickHouse using environment variables."""
    try:
        client = clickhouse_connect.get_client(
            host=os.getenv('CLICKHOUSE_HOST'),
            port=os.getenv('CLICKHOUSE_PORT', 8443),
            username=os.getenv('CLICKHOUSE_USERNAME', 'default'),
            password=os.getenv('CLICKHOUSE_PASSWORD'),
            secure=True
        )
        return client
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def create_tables():
    client = get_client()
    if not client:
        print("Skipping table creation due to missing connection.")
        return

    # 1. Smart Home Sensor Data (Time-Series)
    # Stores hourly readings for temperature, humidity, energy usage.
    client.command("""
        CREATE TABLE IF NOT EXISTS smart_home_sensors (
            home_id String,
            timestamp DateTime,
            temperature Float32,
            humidity Float32,
            energy_consumption_kwh Float32,
            occupancy_status UInt8,
            solar_generation_kwh Float32
        ) ENGINE = MergeTree()
        ORDER BY (home_id, timestamp)
    """)
    print("Table 'smart_home_sensors' created or exists.")

    # 2. Retrofit Materials Catalog
    # Stores potential retrofit options with costs and benefits.
    client.command("""
        CREATE TABLE IF NOT EXISTS retrofit_materials (
            material_id String,
            category String, -- e.g., 'Insulation', 'Windows', 'Smart Thermostat'
            name String,
            cost_per_unit Float32,
            efficiency_rating Float32, -- e.g., R-value or Energy Star score
            sustainability_score UInt8, -- 1-10
            description String
        ) ENGINE = MergeTree()
        ORDER BY category
    """)
    print("Table 'retrofit_materials' created or exists.")

if __name__ == "__main__":
    create_tables()
