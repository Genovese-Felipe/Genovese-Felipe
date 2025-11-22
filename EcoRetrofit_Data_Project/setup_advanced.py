import clickhouse_connect
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
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

def setup_advanced_schema():
    client = get_client()
    if not client:
        print("Skipping schema setup due to missing connection.")
        return

    print("Setting up Advanced Schema (S3 + Materialized Views)...")

    # 1. S3 Queue Table (The "Landing Zone")
    # Note: Requires valid AWS keys in the SQL or ClickHouse config.
    # We use placeholders here for demonstration.
    s3_url = "https://ecoretrofit-datalake-demo.s3.amazonaws.com/data/*.json"
    aws_key = os.getenv("AWS_ACCESS_KEY_ID", "replace_me")
    aws_secret = os.getenv("AWS_SECRET_ACCESS_KEY", "replace_me")

    # NOTE: In a real scenario, we would execute this.
    # Commenting out to prevent syntax errors if the user runs it without keys.
    print(f"""
    [INSTRUCTION] To enable S3 ingestion, run this SQL in ClickHouse:

    CREATE TABLE IF NOT EXISTS raw_sensors_s3_queue (
        timestamp DateTime,
        home_id String,
        temperature Float32,
        humidity Float32,
        energy_kwh Float32,
        voltage Float32
    ) ENGINE = S3Queue('{s3_url}', '{aws_key}', '{aws_secret}', 'JSONEachRow');
    """)

    # 2. Target MergeTree Table (The "Permanent Store")
    client.command("""
        CREATE TABLE IF NOT EXISTS smart_city_telemetry (
            timestamp DateTime,
            home_id String,
            temperature Float32,
            humidity Float32,
            energy_kwh Float32,
            voltage Float32
        ) ENGINE = MergeTree()
        PARTITION BY toYYYYMMDD(timestamp)
        ORDER BY (home_id, timestamp)
        TTL timestamp + INTERVAL 30 DAY
    """)
    print("Table 'smart_city_telemetry' created.")

    # 3. Materialized View (The "Real-Time Aggregator")
    # This automatically aggregates data as it is inserted into 'smart_city_telemetry'
    client.command("""
        CREATE TABLE IF NOT EXISTS hourly_energy_stats (
            hour DateTime,
            home_id String,
            avg_temp Float32,
            total_energy Float32,
            max_voltage Float32
        ) ENGINE = SummingMergeTree()
        ORDER BY (home_id, hour)
    """)

    client.command("""
        CREATE MATERIALIZED VIEW IF NOT EXISTS mv_hourly_energy_stats TO hourly_energy_stats
        AS SELECT
            toStartOfHour(timestamp) as hour,
            home_id,
            avg(temperature) as avg_temp,
            sum(energy_kwh) as total_energy,
            max(voltage) as max_voltage
        FROM smart_city_telemetry
        GROUP BY home_id, hour
    """)
    print("Materialized View 'mv_hourly_energy_stats' created.")

if __name__ == "__main__":
    setup_advanced_schema()
