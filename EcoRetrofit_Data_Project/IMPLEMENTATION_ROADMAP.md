# Implementation Roadmap: Advanced ClickHouse Data Platform

This document details the step-by-step execution for the "Advanced" version of the project. It is written for a non-developer, with explicit "Click-by-Click" guidance concepts.

---

## Phase 1: Infrastructure Setup (AWS & ClickHouse)

### Step 1.1: AWS S3 Configuration (The Data Lake)
*   **Why:** We need a place to dump massive amounts of raw sensor data before ClickHouse digests it.
*   **Action:**
    1.  Login to AWS Console.
    2.  Search "S3" -> "Create Bucket".
    3.  Name: `ecoretrofit-datalake-user-id`.
    4.  Region: `us-east-1` (Same as ClickHouse).
    5.  **Crucial:** Generate Access Keys (IAM -> Users -> Create User "clickhouse-loader" -> Security Credentials -> Create Access Key). **Save these CSVs.**

### Step 1.2: ClickHouse S3 Integration
*   **Why:** ClickHouse needs permission to read from that bucket.
*   **Action (SQL Command in ClickHouse Console):**
    ```sql
    -- This query tests the connection
    SELECT * FROM s3(
        'https://ecoretrofit-datalake-user-id.s3.amazonaws.com/data/*.json',
        'AWS_ACCESS_KEY_ID',
        'AWS_SECRET_ACCESS_KEY',
        'JSONEachRow'
    ) LIMIT 10;
    ```

---

## Phase 2: High-Performance Data Generation

### Step 2.1: The "Firehose" Script
*   **Concept:** Instead of a loop that runs once, we create a script that runs *forever*, generating thousands of events per second.
*   **Key Technology:** Python `boto3` (for S3) and `faker`.
*   **The Script Structure:**
    1.  Define 1,000 `HomeID`s.
    2.  Every second, generate a random `CurrentTemp` and `EnergyUsage` for all 1,000 homes.
    3.  Bundle these 1,000 records into a JSON file.
    4.  Upload the JSON file to S3 bucket every 10 seconds (Batching).

### Step 2.2: Running the Generator
*   **For the User:**
    *   **Colab:** "Paste script, insert AWS Keys, Click Play. Leave tab open."
    *   **Local:** "Run `python firehose.py`. Watch the terminal fly."

---

## Phase 3: The ClickHouse Pipeline (Ingestion & Aggregation)

### Step 3.1: Create the Landing Table
*   **SQL:**
    ```sql
    CREATE TABLE raw_sensors (
        timestamp DateTime,
        home_id UInt32,
        temperature Float32,
        energy Float32
    ) ENGINE = S3Queue(...) -- Automatically sucks files from S3 as they appear!
    ```

### Step 3.2: Real-Time Aggregation (Materialized Views)
*   **Why:** We don't want to query billions of rows every time we want a chart. We want the answers pre-calculated.
*   **SQL:**
    ```sql
    CREATE MATERIALIZED VIEW hourly_stats
    ENGINE = SummingMergeTree()
    ORDER BY (home_id, toStartOfHour(timestamp))
    AS SELECT
        home_id,
        toStartOfHour(timestamp) as hour,
        avg(temperature) as avg_temp,
        sum(energy) as total_energy
    FROM raw_sensors
    GROUP BY home_id, hour;
    ```
*   **Impact:** As data lands in S3 -> ClickHouse S3Queue -> Raw Table -> Materialized View. The dashboard reads from the View instantly.

---

## Phase 4: Analytics & Visualization

### Step 4.1: Anomaly Detection via SQL
*   **Query:** Find homes where Energy is > 3 Standard Deviations above the norm.
    ```sql
    SELECT home_id, energy
    FROM hourly_stats
    WHERE energy > (SELECT avg(energy) + 3*stddevPop(energy) FROM hourly_stats)
    ```

### Step 4.2: The "Live" Dashboard
*   **Tool:** ClickHouse "Queries" tab or a connected Grafana instance.
*   **Action:** Set up a refresh rate of 5s. Watch the `total_energy` bars grow in real-time as the Python script runs.

---

## Summary of Skills Demonstrated
1.  **Cloud Engineering:** AWS IAM, S3, Cloud Storage integration.
2.  **Data Engineering:** Streaming pipelines (S3Queue), Materialized Views.
3.  **DevOps:** Handling credentials, high-volume data generation.
4.  **Analytics:** Statistical SQL.
