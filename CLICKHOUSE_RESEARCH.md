# 🔍 ClickHouse Research & Implementation Guide

## Overview

ClickHouse is an open-source column-oriented database management system (DBMS) designed for online analytical processing (OLAP). It's perfect for our Smart Building Analytics project due to its exceptional performance with time-series data.

---

## 🎯 Why ClickHouse for This Project?

### Key Advantages

1. **Ultra-Fast Query Performance**
   - Processes billions of rows per second
   - Columnar storage optimized for analytics
   - Perfect for IoT sensor data analysis

2. **Excellent Time-Series Support**
   - Native DateTime types with precision
   - Efficient time-based partitioning
   - Built-in time-series functions

3. **Cost-Effective**
   - High compression rates (10:1 typical)
   - Efficient resource utilization
   - $300 credit goes a long way

4. **Real-Time Analytics**
   - Low-latency queries (milliseconds)
   - Supports high ingestion rates
   - Materialized views for pre-aggregation

5. **Scalability**
   - Handles petabytes of data
   - Horizontal scaling capability
   - Perfect for growing projects

---

## 📊 ClickHouse Cloud Free Trial & Credits

### Getting Started

**Free Trial Details:**
- 30-day free trial
- $300 in credits (additional to your $300)
- **Total: $600 worth of resources**
- No credit card required initially

**Sign-up Process:**
1. Visit: https://clickhouse.com/cloud
2. Create account with GitHub (student email preferred)
3. Activate free trial
4. Receive $300 credits automatically
5. Add your additional $300 credits

**Credit Usage Optimization:**
- Enable automatic scaling down during idle
- Use development tier for testing
- Leverage materialized views to reduce query costs
- Monitor usage via dashboard
- Set budget alerts

### Pricing Structure

**Compute:**
- Development: ~$0.50/hour
- Production: ~$2-5/hour (auto-scaling)
- **Our Strategy**: Development tier + careful monitoring

**Storage:**
- $0.016/GB/month (highly compressed)
- 100GB actual = ~10GB stored (10:1 compression)
- **Our Estimate**: $20-30 for entire project

**Expected Total Cost:**
- Development phase (5 days): $50-100
- Demo hosting (30 days): $100-150
- Buffer for experiments: $50
- **Total**: $200-300 (within budget!)

---

## 🏗️ ClickHouse Architecture for IoT

### Table Engine Selection

**MergeTree Family** (Best for our use case)

```sql
-- Why MergeTree?
-- ✓ Primary index for fast lookups
-- ✓ Partition pruning (skip months of data)
-- ✓ Automatic data sorting
-- ✓ Background merges for optimization

CREATE TABLE sensor_readings (
    timestamp DateTime64(3),  -- millisecond precision
    building_id String,
    sensor_id String,
    sensor_type LowCardinality(String),  -- optimization for repeated values
    value Float64,
    quality_score Float32
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(timestamp)  -- monthly partitions
ORDER BY (building_id, sensor_type, timestamp)  -- primary key
TTL timestamp + INTERVAL 2 YEAR;  -- automatic data cleanup
```

**Key Design Decisions:**

1. **Partitioning by Month**
   - Queries often focus on recent data
   - Easy to drop old partitions
   - Optimal partition size (avoid too many)

2. **Ordering Key**
   - `building_id` first: filter by building is common
   - `sensor_type` second: often query specific sensor types
   - `timestamp` third: time-range queries

3. **Data Types**
   - `LowCardinality(String)`: optimize repeated values (sensor types)
   - `DateTime64(3)`: millisecond precision for IoT
   - `Float32` vs `Float64`: balance precision and storage

### Materialized Views for Performance

```sql
-- Pre-aggregate hourly data
-- Runs automatically on INSERT
-- Dramatically reduces query time

CREATE MATERIALIZED VIEW hourly_energy_stats
ENGINE = SummingMergeTree()
ORDER BY (building_id, hour)
AS SELECT
    toStartOfHour(timestamp) as hour,
    building_id,
    sum(value) as total_energy,
    avg(value) as avg_energy,
    max(value) as peak_energy,
    count() as reading_count
FROM sensor_readings
WHERE sensor_type = 'energy'
GROUP BY hour, building_id;

-- Query time improvement:
-- Without MV: 5-10 seconds for hourly aggregates
-- With MV: 50-100 milliseconds
-- 100x faster!
```

### Data Ingestion Patterns

**Pattern 1: Batch Ingestion (Initial Load)**

```python
import clickhouse_connect

client = clickhouse_connect.get_client(
    host='your-instance.clickhouse.cloud',
    port=8443,
    username='default',
    password='your-password'
)

# Batch insert 100,000 rows at once
# ClickHouse handles this efficiently
data = [
    [timestamp, building_id, sensor_id, sensor_type, value, quality]
    for ... in generate_sensor_data(100_000)
]

client.insert(
    'sensor_readings',
    data,
    column_names=[
        'timestamp', 'building_id', 'sensor_id',
        'sensor_type', 'value', 'quality_score'
    ]
)

# Performance: 10,000-50,000 rows/second
# 1 million rows: 20-100 seconds
```

**Pattern 2: Streaming Ingestion (Real-time)**

```python
import asyncio
from clickhouse_driver import Client

# Async client for real-time streaming
client = Client('your-instance.clickhouse.cloud', secure=True)

async def stream_sensor_data():
    buffer = []
    buffer_size = 1000  # flush every 1000 readings
    
    async for reading in sensor_stream():
        buffer.append(reading)
        
        if len(buffer) >= buffer_size:
            client.insert('sensor_readings', buffer)
            buffer = []
            
    # Final flush
    if buffer:
        client.insert('sensor_readings', buffer)

# Performance: 5,000-10,000 rows/second
# Low latency: data available for queries within 1 second
```

---

## 🚀 Query Optimization Techniques

### 1. Leverage Partitioning

```sql
-- BAD: Scans all partitions
SELECT * FROM sensor_readings
WHERE sensor_type = 'temperature';

-- GOOD: Only scans recent partition
SELECT * FROM sensor_readings
WHERE 
    timestamp >= toDateTime('2025-11-01')
    AND timestamp < toDateTime('2025-12-01')
    AND sensor_type = 'temperature';

-- Performance: 100x faster
```

### 2. Use Materialized Views

```sql
-- Instead of aggregating on every query
SELECT 
    toStartOfHour(timestamp) as hour,
    building_id,
    avg(value) as avg_temp
FROM sensor_readings
WHERE sensor_type = 'temperature'
GROUP BY hour, building_id;

-- Query pre-aggregated view
SELECT hour, building_id, avg_temp
FROM hourly_temperature_stats;

-- Performance: 50-100x faster
```

### 3. Sample for Approximate Results

```sql
-- When exact numbers aren't critical
SELECT 
    building_id,
    avg(value) as avg_energy
FROM sensor_readings SAMPLE 0.1  -- use 10% of data
WHERE sensor_type = 'energy';

-- Performance: 10x faster
-- Accuracy: ±1-2% (acceptable for most analytics)
```

### 4. Proper WHERE Clause Order

```sql
-- ClickHouse processes filters in order
-- Put most selective filters first

-- GOOD: Filters reduce data early
SELECT * FROM sensor_readings
WHERE 
    building_id = 'B001'  -- most selective
    AND timestamp >= now() - INTERVAL 1 HOUR
    AND sensor_type IN ('temperature', 'humidity');

-- BAD: Generic filters first
SELECT * FROM sensor_readings
WHERE 
    sensor_type IN ('temperature', 'humidity')
    AND timestamp >= now() - INTERVAL 1 HOUR
    AND building_id = 'B001';
```

---

## 📈 Advanced Features for Our Project

### 1. Window Functions (Anomaly Detection)

```sql
-- Calculate moving average for anomaly detection
SELECT 
    timestamp,
    building_id,
    value,
    avg(value) OVER (
        PARTITION BY building_id 
        ORDER BY timestamp 
        ROWS BETWEEN 100 PRECEDING AND CURRENT ROW
    ) as moving_avg,
    value - moving_avg as deviation
FROM sensor_readings
WHERE sensor_type = 'energy'
ORDER BY building_id, timestamp;
```

### 2. Array Functions (Multi-Sensor Analysis)

```sql
-- Collect all sensor readings in an hour
SELECT 
    toStartOfHour(timestamp) as hour,
    building_id,
    groupArray(value) as readings,
    arrayAvg(readings) as avg,
    arrayMax(readings) - arrayMin(readings) as range
FROM sensor_readings
GROUP BY hour, building_id;
```

### 3. JOIN Optimizations

```sql
-- Join sensor data with building metadata
SELECT 
    s.timestamp,
    b.name as building_name,
    b.city,
    s.value as energy_consumption,
    s.value / b.total_area as energy_per_sqm
FROM sensor_readings s
GLOBAL INNER JOIN buildings b 
    ON s.building_id = b.building_id
WHERE s.sensor_type = 'energy';

-- Note: GLOBAL keyword for distributed joins
```

### 4. User-Defined Functions

```sql
-- Create function for carbon footprint calculation
CREATE FUNCTION carbon_footprint AS (energy_kwh, grid_intensity)
-> energy_kwh * grid_intensity * 0.001;  -- kg CO2

-- Usage
SELECT 
    building_id,
    sum(value) as total_energy_kwh,
    carbon_footprint(total_energy_kwh, 0.5) as co2_kg
FROM sensor_readings
WHERE sensor_type = 'energy'
GROUP BY building_id;
```

---

## 🔐 Security Best Practices

### 1. User Management

```sql
-- Create read-only user for dashboard
CREATE USER dashboard_user 
IDENTIFIED BY 'strong_password'
SETTINGS readonly = 1;

-- Grant specific permissions
GRANT SELECT ON smartbuild.sensor_readings TO dashboard_user;
GRANT SELECT ON smartbuild.hourly_aggregates TO dashboard_user;

-- Create admin user for data ingestion
CREATE USER data_ingestion
IDENTIFIED BY 'another_strong_password';

GRANT INSERT, SELECT ON smartbuild.* TO data_ingestion;
```

### 2. Network Security

- Enable SSL/TLS (ClickHouse Cloud does this automatically)
- Use IP whitelisting
- Rotate passwords regularly
- Use environment variables for credentials (never commit!)

### 3. Data Privacy

```sql
-- Anonymize personal data if needed
SELECT 
    building_id,
    anonymize(room_id) as room_id,  -- hash function
    avg(value) as avg_temp
FROM sensor_readings
GROUP BY building_id, room_id;
```

---

## 📊 Monitoring & Observability

### ClickHouse System Tables

```sql
-- Monitor query performance
SELECT 
    query,
    type,
    query_duration_ms,
    read_rows,
    read_bytes
FROM system.query_log
WHERE query_duration_ms > 1000  -- slow queries
ORDER BY query_duration_ms DESC
LIMIT 10;

-- Check table sizes
SELECT 
    database,
    table,
    formatReadableSize(sum(bytes)) as size,
    sum(rows) as rows
FROM system.parts
WHERE active
GROUP BY database, table
ORDER BY sum(bytes) DESC;

-- Monitor ingestion rate
SELECT 
    toStartOfMinute(event_time) as minute,
    count() as inserts,
    sum(rows) as total_rows
FROM system.query_log
WHERE query_kind = 'Insert'
GROUP BY minute
ORDER BY minute DESC
LIMIT 60;
```

### ClickHouse Cloud Dashboard

- Real-time CPU/Memory usage
- Query metrics
- Storage consumption
- Cost tracking
- Alert configuration

---

## 🎓 Learning Resources

### Official Documentation
- ClickHouse Docs: https://clickhouse.com/docs
- ClickHouse Cloud: https://clickhouse.com/cloud
- GitHub: https://github.com/ClickHouse/ClickHouse

### Tutorials
- ClickHouse Academy: Free courses
- YouTube: Official ClickHouse channel
- Blog: https://clickhouse.com/blog

### Community
- Slack: ClickHouse Community
- Stack Overflow: #clickhouse tag
- GitHub Discussions

---

## 🛠️ Development Tools

### 1. CLI Client

```bash
# Install
pip install clickhouse-cli

# Connect
clickhouse-client \
  --host your-instance.clickhouse.cloud \
  --port 9440 \
  --secure \
  --user default \
  --password your-password

# Execute query
clickhouse-client --query "SELECT count() FROM sensor_readings"
```

### 2. Python Clients

**clickhouse-connect (Recommended)**
```python
import clickhouse_connect

client = clickhouse_connect.get_client(
    host='your-instance.clickhouse.cloud',
    port=8443,
    username='default',
    password='your-password',
    secure=True
)

# Execute query
result = client.query("SELECT * FROM sensor_readings LIMIT 10")
df = result.result_set  # Returns list of tuples

# As pandas DataFrame
df = client.query_df("SELECT * FROM sensor_readings LIMIT 10")
```

**clickhouse-driver (Alternative)**
```python
from clickhouse_driver import Client

client = Client(
    host='your-instance.clickhouse.cloud',
    port=9440,
    user='default',
    password='your-password',
    secure=True
)

# Execute query
result = client.execute("SELECT * FROM sensor_readings LIMIT 10")
```

### 3. GUI Tools

- **DBeaver**: Universal database tool (supports ClickHouse)
- **ClickHouse Playground**: Web-based query interface
- **Tabix**: Lightweight ClickHouse GUI
- **DataGrip**: JetBrains IDE (paid)

---

## 💡 Pro Tips for Our Project

### 1. Start Small, Scale Up

```
Day 1: 
- Create tables with 10K rows
- Test queries
- Validate schema

Day 2:
- Scale to 100K rows
- Test query performance
- Adjust indexes if needed

Day 3:
- Scale to 1M+ rows
- Benchmark performance
- Optimize slow queries

Day 4-5:
- Production data volume
- Final optimizations
```

### 2. Use Query Profiling

```sql
-- Enable detailed profiling
SET send_logs_level = 'trace';

-- Run query and analyze
SELECT ... FROM sensor_readings ...;

-- Check execution plan
EXPLAIN SELECT ... FROM sensor_readings ...;
```

### 3. Leverage ClickHouse for ML

```sql
-- Linear regression directly in SQL
SELECT 
    building_id,
    linearRegression(toHour(timestamp), value) as trend
FROM sensor_readings
WHERE sensor_type = 'energy'
GROUP BY building_id;

-- Correlation analysis
SELECT 
    building_id,
    corr(temperature, energy_consumption) as correlation
FROM (
    SELECT 
        building_id,
        timestamp,
        argMax(value, sensor_type = 'temperature') as temperature,
        argMax(value, sensor_type = 'energy') as energy_consumption
    FROM sensor_readings
    GROUP BY building_id, timestamp
)
GROUP BY building_id;
```

### 4. Automated Data Generation

```python
# Generate realistic time-series data
import numpy as np
from datetime import datetime, timedelta

def generate_energy_data(start_date, days=30):
    """Generate realistic energy consumption data"""
    timestamps = []
    values = []
    
    current = start_date
    base_consumption = 100  # kW
    
    for i in range(days * 24 * 60):  # minute-level data
        # Add daily seasonality
        hour_of_day = current.hour
        daily_factor = 1.0 + 0.3 * np.sin(2 * np.pi * hour_of_day / 24)
        
        # Add weekly seasonality (weekends lower)
        day_of_week = current.weekday()
        weekly_factor = 0.7 if day_of_week >= 5 else 1.0
        
        # Add noise
        noise = np.random.normal(0, 5)
        
        value = base_consumption * daily_factor * weekly_factor + noise
        
        timestamps.append(current)
        values.append(max(0, value))  # ensure non-negative
        
        current += timedelta(minutes=1)
    
    return timestamps, values
```

---

## 🎯 Project-Specific Schema

### Complete Schema for Smart Building Analytics

```sql
-- Database
CREATE DATABASE IF NOT EXISTS smartbuild;
USE smartbuild;

-- 1. Buildings table
CREATE TABLE buildings (
    building_id String,
    name String,
    address String,
    city String,
    country String,
    latitude Float64,
    longitude Float64,
    total_area Float64,  -- square meters
    floors Int32,
    year_built Int32,
    building_type LowCardinality(String),  -- residential, commercial, etc.
    certification LowCardinality(String),  -- LEED, BREEAM, etc.
    created_at DateTime DEFAULT now()
) ENGINE = MergeTree()
ORDER BY building_id;

-- 2. Sensors metadata
CREATE TABLE sensors (
    sensor_id String,
    building_id String,
    floor_id String,
    room_id String,
    sensor_type LowCardinality(String),
    manufacturer String,
    model String,
    installation_date Date,
    calibration_date Date,
    location_x Float32,  -- coordinates on floor plan
    location_y Float32,
    is_active Bool DEFAULT true
) ENGINE = MergeTree()
ORDER BY (building_id, sensor_id);

-- 3. Sensor readings (main table)
CREATE TABLE sensor_readings (
    timestamp DateTime64(3),
    building_id String,
    sensor_id String,
    sensor_type LowCardinality(String),
    value Float64,
    unit String,
    quality_score Float32 DEFAULT 1.0
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(timestamp)
ORDER BY (building_id, sensor_type, timestamp)
TTL timestamp + INTERVAL 2 YEAR;

-- 4. Energy costs
CREATE TABLE energy_costs (
    timestamp DateTime,
    building_id String,
    energy_kwh Float64,
    cost_usd Float64,
    rate_per_kwh Float64,
    time_of_use_category LowCardinality(String)  -- peak, off-peak, etc.
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(timestamp)
ORDER BY (building_id, timestamp);

-- 5. Weather data
CREATE TABLE weather (
    timestamp DateTime,
    city String,
    temperature Float32,
    humidity Float32,
    pressure Float32,
    wind_speed Float32,
    cloud_cover Int32,
    description String
) ENGINE = ReplacingMergeTree()
PARTITION BY toYYYYMM(timestamp)
ORDER BY (city, timestamp);

-- 6. Anomaly events
CREATE TABLE anomaly_events (
    event_id UUID DEFAULT generateUUIDv4(),
    timestamp DateTime64(3),
    building_id String,
    sensor_id String,
    anomaly_score Float64,
    anomaly_type LowCardinality(String),  -- spike, drop, drift, etc.
    description String,
    severity LowCardinality(String),  -- low, medium, high, critical
    is_resolved Bool DEFAULT false,
    resolved_at Nullable(DateTime)
) ENGINE = MergeTree()
ORDER BY (building_id, timestamp);

-- 7. Energy predictions
CREATE TABLE energy_predictions (
    prediction_id UUID DEFAULT generateUUIDv4(),
    prediction_timestamp DateTime,
    target_timestamp DateTime,
    building_id String,
    predicted_consumption Float64,
    confidence_lower Float64,
    confidence_upper Float64,
    model_version String,
    model_accuracy Float32
) ENGINE = MergeTree()
ORDER BY (building_id, target_timestamp);

-- 8. Optimization recommendations
CREATE TABLE recommendations (
    recommendation_id UUID DEFAULT generateUUIDv4(),
    timestamp DateTime DEFAULT now(),
    building_id String,
    category LowCardinality(String),  -- energy, comfort, maintenance, etc.
    title String,
    description String,
    potential_savings_usd Float64,
    potential_savings_kwh Float64,
    implementation_cost Float64,
    priority LowCardinality(String),  -- low, medium, high
    status LowCardinality(String) DEFAULT 'pending'  -- pending, implemented, rejected
) ENGINE = MergeTree()
ORDER BY (building_id, timestamp);

-- Materialized Views for Performance

-- Hourly energy aggregates
CREATE MATERIALIZED VIEW hourly_energy_stats
ENGINE = SummingMergeTree()
ORDER BY (building_id, hour)
AS SELECT
    toStartOfHour(timestamp) as hour,
    building_id,
    sum(value) as total_energy_kwh,
    avg(value) as avg_power_kw,
    max(value) as peak_power_kw,
    min(value) as min_power_kw,
    count() as reading_count
FROM sensor_readings
WHERE sensor_type = 'energy'
GROUP BY hour, building_id;

-- Daily temperature/humidity stats
CREATE MATERIALIZED VIEW daily_comfort_stats
ENGINE = SummingMergeTree()
ORDER BY (building_id, day)
AS SELECT
    toDate(timestamp) as day,
    building_id,
    sensor_type,
    avg(value) as avg_value,
    min(value) as min_value,
    max(value) as max_value,
    stddevPop(value) as stddev_value
FROM sensor_readings
WHERE sensor_type IN ('temperature', 'humidity', 'co2')
GROUP BY day, building_id, sensor_type;

-- Real-time dashboard view (last 24 hours)
CREATE MATERIALIZED VIEW realtime_dashboard
ENGINE = AggregatingMergeTree()
ORDER BY (building_id, sensor_type, hour)
AS SELECT
    toStartOfHour(timestamp) as hour,
    building_id,
    sensor_type,
    avgState(value) as avg_value,
    maxState(value) as max_value,
    countState() as count_value
FROM sensor_readings
WHERE timestamp >= now() - INTERVAL 24 HOUR
GROUP BY hour, building_id, sensor_type;
```

---

## 🎬 Next Steps

1. ✅ Sign up for ClickHouse Cloud
2. ✅ Create database using above schema
3. ✅ Test with sample data (1000 rows)
4. ✅ Validate query performance
5. ✅ Scale to production data
6. ✅ Implement application layer

---

**Ready to build!** 🚀
