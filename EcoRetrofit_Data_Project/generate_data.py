import clickhouse_connect
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from setup_database import get_client

load_dotenv()

def generate_sensor_data(days=365):
    """Generates synthetic hourly data for 5 homes."""
    print(f"Generating {days} days of sensor data...")

    homes = ['Home_A_Drafty', 'Home_B_Eco', 'Home_C_Standard', 'Home_D_Glass', 'Home_E_Smart']
    start_date = datetime.now() - timedelta(days=days)
    timestamps = [start_date + timedelta(hours=i) for i in range(days * 24)]

    data = []

    for home in homes:
        # Base factors
        base_temp = 18 if 'Drafty' in home else 21
        insulation_factor = 0.8 if 'Drafty' in home else (0.2 if 'Eco' in home else 0.5)

        for ts in timestamps:
            # Simulate outside temp (seasonality)
            month = ts.month
            hour = ts.hour
            outside_temp = 15 + 10 * np.sin(2 * np.pi * (month - 4) / 12) + 5 * np.sin(2 * np.pi * (hour - 12) / 24)

            # Indoor temp logic (simplified physics)
            diff = base_temp - outside_temp
            energy_needed = max(0, diff * insulation_factor)  # Heating
            if outside_temp > 25: # Cooling
                energy_needed += (outside_temp - 24) * insulation_factor

            # Random noise
            energy_consumption = max(0, energy_needed + np.random.normal(0, 0.1))
            solar_gen = 0
            if 6 <= hour <= 18:
                solar_gen = max(0, 2 * np.sin(np.pi * (hour - 6) / 12) * (1 if 'Eco' in home else 0))

            data.append({
                'home_id': home,
                'timestamp': ts,
                'temperature': base_temp + np.random.normal(0, 0.5),
                'humidity': 40 + np.random.normal(0, 5),
                'energy_consumption_kwh': round(energy_consumption, 2),
                'occupancy_status': 1 if 7 < hour < 22 else 0,
                'solar_generation_kwh': round(solar_gen, 2)
            })

    return pd.DataFrame(data)

def generate_materials_catalog():
    """Generates a catalog of retrofit materials."""
    materials = [
        ('Insulation', 'Rockwool Comfortbatt', 50.0, 4.2, 9, 'Fire-resistant stone wool insulation'),
        ('Insulation', 'Fiberglass Roll', 30.0, 3.5, 6, 'Standard fiberglass insulation'),
        ('Windows', 'Double Glazed Argon', 200.0, 0.3, 8, 'Low-E coating with argon gas'),
        ('Windows', 'Triple Glazed', 350.0, 0.15, 10, 'Maximum thermal efficiency'),
        ('Smart Home', 'Ecobee Smart Thermostat', 150.0, 0.9, 8, 'AI-powered learning thermostat'),
        ('Lighting', 'Philips Hue LED Kit', 80.0, 0.95, 7, 'Smart LED lighting system'),
        ('Solar', 'Photovoltaic Panel 400W', 300.0, 0.8, 9, 'High-efficiency solar panel')
    ]

    return pd.DataFrame(materials, columns=['category', 'name', 'cost_per_unit', 'efficiency_rating', 'sustainability_score', 'description'])

def ingest_data():
    client = get_client()
    if not client:
        print("Cannot ingest data: No connection.")
        return

    # 1. Ingest Materials
    materials_df = generate_materials_catalog()
    # Add material_id
    materials_df['material_id'] = [f"MAT_{i:03d}" for i in range(len(materials_df))]

    print("Ingesting Retrofit Materials...")
    client.insert_df('retrofit_materials', materials_df)
    print(f"Inserted {len(materials_df)} materials.")

    # 2. Ingest Sensor Data (Batched)
    sensors_df = generate_sensor_data(days=30) # Start with 30 days for speed
    print("Ingesting Sensor Data...")
    client.insert_df('smart_home_sensors', sensors_df)
    print(f"Inserted {len(sensors_df)} sensor readings.")

if __name__ == "__main__":
    ingest_data()
