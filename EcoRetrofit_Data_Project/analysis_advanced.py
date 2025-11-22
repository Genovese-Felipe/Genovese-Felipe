import clickhouse_connect
import pandas as pd
import os
from dotenv import load_dotenv
from setup_advanced import get_client

load_dotenv()

def run_advanced_analysis():
    client = get_client()
    if not client:
        return

    print("--- Advanced In-Database Analytics ---")

    # 1. Real-Time Aggregation Query (Speed Test)
    # Instead of calculating sum() in Python, we query the pre-calculated View
    print("\n1. Querying Materialized View (Instant Results)...")
    start_time = pd.Timestamp.now()

    query_mv = """
    SELECT home_id, sum(total_energy) as lifetime_energy
    FROM hourly_energy_stats
    GROUP BY home_id
    ORDER BY lifetime_energy DESC
    LIMIT 5
    """
    try:
        top_consumers = client.query_df(query_mv)
        print(top_consumers)
        print(f"Query Time: {pd.Timestamp.now() - start_time}")
    except Exception as e:
        print(f"Query failed (likely no data yet): {e}")

    # 2. SQL-Based Anomaly Detection (Z-Score)
    # This is "Advanced" because it pushes the math to the DB
    print("\n2. Detecting Anomalies via SQL (Z-Score Method)...")

    query_anomaly = """
    WITH stats AS (
        SELECT
            avg(total_energy) as mean_val,
            stddevPop(total_energy) as std_val
        FROM hourly_energy_stats
    )
    SELECT
        home_id,
        hour,
        total_energy,
        (total_energy - (SELECT mean_val FROM stats)) / (SELECT std_val FROM stats) as z_score
    FROM hourly_energy_stats
    WHERE abs(z_score) > 3
    ORDER BY z_score DESC
    LIMIT 10
    """

    try:
        anomalies = client.query_df(query_anomaly)
        if anomalies.empty:
            print("No anomalies detected (Need more data variation).")
        else:
            print(f"Detected {len(anomalies)} critical events:")
            print(anomalies)
    except Exception as e:
        print(f"Anomaly query failed: {e}")

if __name__ == "__main__":
    run_advanced_analysis()
