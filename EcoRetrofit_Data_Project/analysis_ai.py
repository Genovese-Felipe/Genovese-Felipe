import clickhouse_connect
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from setup_database import get_client

def analyze_efficiency():
    client = get_client()
    if not client:
        return

    # 1. Fetch Data
    print("Fetching data from ClickHouse...")
    query = """
    SELECT
        home_id,
        avg(temperature) as avg_indoor_temp,
        avg(energy_consumption_kwh) as avg_energy,
        sum(energy_consumption_kwh) as total_energy
    FROM smart_home_sensors
    GROUP BY home_id
    """
    summary_df = client.query_df(query)

    print("\n--- Energy Summary ---")
    print(summary_df)

    # 2. Detect Anomalies (AI Part)
    print("\nRunning Anomaly Detection (Isolation Forest)...")
    # We'll look for hours where energy is high but temp is moderate (inefficiency)
    detailed_query = "SELECT * FROM smart_home_sensors"
    df = client.query_df(detailed_query)

    features = df[['temperature', 'humidity', 'energy_consumption_kwh']]
    model = IsolationForest(contamination=0.05, random_state=42)
    df['anomaly'] = model.fit_predict(features)

    anomalies = df[df['anomaly'] == -1]
    print(f"Detected {len(anomalies)} anomalous hours (potential waste).")

    return summary_df, anomalies

def recommend_retrofits(summary_df):
    client = get_client()
    materials_df = client.query_df("SELECT * FROM retrofit_materials")

    recommendations = []

    for _, row in summary_df.iterrows():
        home = row['home_id']
        avg_energy = row['avg_energy']

        # Simple Logic Rule Engine
        if avg_energy > 1.0: # High consumption
            rec_material = materials_df[materials_df['category'] == 'Insulation'].iloc[0]
            reason = "High average energy usage detected. Insulation upgrade recommended."
        elif 'Glass' in home:
            rec_material = materials_df[materials_df['category'] == 'Windows'].iloc[0]
            reason = "Glass structure detected. Double glazing will reduce thermal loss."
        else:
            rec_material = materials_df[materials_df['category'] == 'Smart Home'].iloc[0]
            reason = "Energy usage is moderate. Optimize with Smart Thermostat."

        recommendations.append({
            'home_id': home,
            'recommendation': rec_material['name'],
            'estimated_cost': rec_material['cost_per_unit'] * 10, # Mock quantity
            'reason': reason
        })

    return pd.DataFrame(recommendations)

if __name__ == "__main__":
    summary, _ = analyze_efficiency()
    recs = recommend_retrofits(summary)
    print("\n--- Retrofit Recommendations ---")
    print(recs)
