# 🚀 Quick Start Implementation Guide

## 5-Day Action Plan with Ready-to-Use Resources

This guide provides immediate actionable steps with code templates, dataset sources, and tool recommendations to build your Smart Building Analytics platform in 5 days.

---

## 📋 Day-by-Day Breakdown

### 🗓️ DAY 1: Setup & Foundation (8 hours)

#### Morning Session (4 hours)

**Hour 1-2: ClickHouse Setup**

1. **Sign up for ClickHouse Cloud**
   - Go to: https://clickhouse.com/cloud
   - Click "Start Free Trial"
   - Use your student email
   - Get $300 in credits

2. **Create your first database**
   ```sql
   CREATE DATABASE smartbuild;
   USE smartbuild;
   
   -- Test connection
   SELECT 'Hello, ClickHouse!' as message;
   ```

3. **Install Python client**
   ```bash
   pip install clickhouse-connect pandas numpy
   ```

4. **Test connection**
   ```python
   import clickhouse_connect
   
   client = clickhouse_connect.get_client(
       host='YOUR_INSTANCE.clickhouse.cloud',
       port=8443,
       username='default',
       password='YOUR_PASSWORD',
       secure=True
   )
   
   result = client.query("SELECT 'Connected!' as status")
   print(result.result_set)
   ```

**Hour 3-4: Project Structure & Environment**

1. **Create project structure**
   ```bash
   mkdir smartbuild-analytics
   cd smartbuild-analytics
   
   mkdir -p {src,data,docs,tests,notebooks,assets}
   mkdir -p src/{data_generation,ingestion,analytics,visualization,utils}
   mkdir -p data/{raw,processed,schemas,sample_data}
   mkdir -p assets/{images,autodesk,videos}
   
   touch README.md requirements.txt .env.example .gitignore
   ```

2. **Create requirements.txt**
   ```text
   # Database
   clickhouse-connect==0.7.0
   
   # Data Processing
   pandas==2.1.0
   numpy==1.24.0
   
   # ML/AI
   scikit-learn==1.3.0
   prophet==1.1.4
   
   # Visualization
   streamlit==1.28.0
   plotly==5.17.0
   matplotlib==3.8.0
   seaborn==0.13.0
   
   # Utilities
   python-dotenv==1.0.0
   faker==20.0.0
   requests==2.31.0
   schedule==1.2.0
   pyyaml==6.0.1
   ```

3. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Create .env file**
   ```bash
   CLICKHOUSE_HOST=your-instance.clickhouse.cloud
   CLICKHOUSE_PORT=8443
   CLICKHOUSE_USER=default
   CLICKHOUSE_PASSWORD=your-password
   CLICKHOUSE_DATABASE=smartbuild
   
   WEATHER_API_KEY=your-openweathermap-key
   ```

#### Afternoon Session (4 hours)

**Hour 5-6: Database Schema Creation**

Create `data/schemas/01_create_tables.sql`:

```sql
-- Buildings
CREATE TABLE IF NOT EXISTS smartbuild.buildings (
    building_id String,
    name String,
    city String,
    total_area Float64,
    floors Int32,
    year_built Int32,
    building_type String
) ENGINE = MergeTree()
ORDER BY building_id;

-- Sensor Readings
CREATE TABLE IF NOT EXISTS smartbuild.sensor_readings (
    timestamp DateTime64(3),
    building_id String,
    sensor_id String,
    sensor_type String,
    value Float64,
    unit String
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(timestamp)
ORDER BY (building_id, sensor_type, timestamp);

-- Hourly Aggregates (Materialized View)
CREATE MATERIALIZED VIEW IF NOT EXISTS smartbuild.hourly_stats
ENGINE = SummingMergeTree()
ORDER BY (building_id, sensor_type, hour)
AS SELECT
    toStartOfHour(timestamp) as hour,
    building_id,
    sensor_type,
    avg(value) as avg_value,
    max(value) as max_value,
    min(value) as min_value,
    count() as count_value
FROM smartbuild.sensor_readings
GROUP BY hour, building_id, sensor_type;
```

Run the schema:
```python
# src/utils/setup_db.py
import clickhouse_connect
from dotenv import load_dotenv
import os

load_dotenv()

client = clickhouse_connect.get_client(
    host=os.getenv('CLICKHOUSE_HOST'),
    port=int(os.getenv('CLICKHOUSE_PORT')),
    username=os.getenv('CLICKHOUSE_USER'),
    password=os.getenv('CLICKHOUSE_PASSWORD')
)

with open('data/schemas/01_create_tables.sql', 'r') as f:
    sql = f.read()
    
for statement in sql.split(';'):
    if statement.strip():
        client.command(statement)
        
print("✅ Database schema created successfully!")
```

**Hour 7-8: Data Generation Framework**

Create `src/data_generation/sensor_simulator.py`:

```python
import random
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict

class SensorSimulator:
    """Generate realistic IoT sensor data"""
    
    def __init__(self, building_id: str, start_date: datetime):
        self.building_id = building_id
        self.current_time = start_date
        
    def generate_temperature(self, hour: int, base_temp: float = 22.0) -> float:
        """Generate realistic temperature with daily pattern"""
        # Daily pattern (cooler at night, warmer during day)
        daily_variation = 3.0 * np.sin(2 * np.pi * (hour - 6) / 24)
        # Random noise
        noise = random.gauss(0, 0.5)
        return base_temp + daily_variation + noise
    
    def generate_humidity(self, temperature: float) -> float:
        """Generate humidity inversely correlated with temperature"""
        base_humidity = 55.0
        temp_effect = -(temperature - 22.0) * 2.0
        noise = random.gauss(0, 3)
        return np.clip(base_humidity + temp_effect + noise, 20, 80)
    
    def generate_co2(self, hour: int, is_occupied: bool) -> float:
        """Generate CO2 levels based on occupancy"""
        base_co2 = 400.0  # ppm outdoor air
        
        if is_occupied:
            # Occupied spaces have higher CO2
            occupancy_effect = random.uniform(200, 600)
        else:
            occupancy_effect = 0
            
        return base_co2 + occupancy_effect
    
    def generate_energy(self, hour: int, temperature: float) -> float:
        """Generate energy consumption"""
        # Base load
        base_load = 10.0  # kW
        
        # HVAC load (higher when temp deviates from 22°C)
        hvac_load = abs(temperature - 22.0) * 2.0
        
        # Occupancy-based load (higher during business hours)
        if 8 <= hour <= 18:
            occupancy_load = random.uniform(20, 40)
        else:
            occupancy_load = random.uniform(5, 15)
        
        return base_load + hvac_load + occupancy_load
    
    def is_occupied(self, hour: int, day_of_week: int) -> bool:
        """Determine if building is occupied"""
        # Weekday business hours
        if day_of_week < 5:  # Monday-Friday
            return 7 <= hour <= 19
        else:  # Weekend
            return 9 <= hour <= 17
    
    def generate_batch(self, 
                      num_readings: int = 1000,
                      sensors_per_floor: int = 10,
                      floors: int = 3) -> List[Dict]:
        """Generate a batch of sensor readings"""
        readings = []
        
        for _ in range(num_readings):
            hour = self.current_time.hour
            day_of_week = self.current_time.weekday()
            occupied = self.is_occupied(hour, day_of_week)
            
            # Generate readings for all sensors
            for floor in range(1, floors + 1):
                for sensor_num in range(1, sensors_per_floor + 1):
                    # Temperature sensor
                    temp = self.generate_temperature(hour)
                    readings.append({
                        'timestamp': self.current_time,
                        'building_id': self.building_id,
                        'sensor_id': f'{self.building_id}_F{floor}_S{sensor_num}_TEMP',
                        'sensor_type': 'temperature',
                        'value': round(temp, 2),
                        'unit': 'celsius'
                    })
                    
                    # Humidity sensor
                    humidity = self.generate_humidity(temp)
                    readings.append({
                        'timestamp': self.current_time,
                        'building_id': self.building_id,
                        'sensor_id': f'{self.building_id}_F{floor}_S{sensor_num}_HUM',
                        'sensor_type': 'humidity',
                        'value': round(humidity, 2),
                        'unit': 'percent'
                    })
                    
                    # CO2 sensor (fewer sensors, only in main areas)
                    if sensor_num % 3 == 0:
                        co2 = self.generate_co2(hour, occupied)
                        readings.append({
                            'timestamp': self.current_time,
                            'building_id': self.building_id,
                            'sensor_id': f'{self.building_id}_F{floor}_S{sensor_num}_CO2',
                            'sensor_type': 'co2',
                            'value': round(co2, 2),
                            'unit': 'ppm'
                        })
            
            # Energy meter (one per building)
            temp_avg = self.generate_temperature(hour)
            energy = self.generate_energy(hour, temp_avg)
            readings.append({
                'timestamp': self.current_time,
                'building_id': self.building_id,
                'sensor_id': f'{self.building_id}_ENERGY_MAIN',
                'sensor_type': 'energy',
                'value': round(energy, 2),
                'unit': 'kW'
            })
            
            # Advance time by 5 minutes
            self.current_time += timedelta(minutes=5)
        
        return readings

# Example usage
if __name__ == "__main__":
    simulator = SensorSimulator(
        building_id='B001',
        start_date=datetime(2025, 11, 1)
    )
    
    readings = simulator.generate_batch(num_readings=100)
    print(f"Generated {len(readings)} sensor readings")
    print(f"Sample: {readings[0]}")
```

---

### 🗓️ DAY 2: Data Pipeline & Autodesk (8 hours)

#### Morning Session (4 hours)

**Hour 1-2: Batch Data Loading**

Create `src/ingestion/batch_loader.py`:

```python
import clickhouse_connect
import pandas as pd
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import sys
sys.path.append('src')
from data_generation.sensor_simulator import SensorSimulator

load_dotenv()

class BatchLoader:
    def __init__(self):
        self.client = clickhouse_connect.get_client(
            host=os.getenv('CLICKHOUSE_HOST'),
            port=int(os.getenv('CLICKHOUSE_PORT')),
            username=os.getenv('CLICKHOUSE_USER'),
            password=os.getenv('CLICKHOUSE_PASSWORD')
        )
    
    def load_buildings(self):
        """Load building metadata"""
        buildings = [
            {
                'building_id': f'B{str(i).zfill(3)}',
                'name': f'Building {i}',
                'city': 'São Paulo',
                'total_area': 5000 + i * 500,
                'floors': 3,
                'year_built': 2010 + i,
                'building_type': 'commercial'
            }
            for i in range(1, 11)  # 10 buildings
        ]
        
        df = pd.DataFrame(buildings)
        self.client.insert_df('smartbuild.buildings', df)
        print(f"✅ Loaded {len(buildings)} buildings")
    
    def load_sensor_data(self, days: int = 30):
        """Load historical sensor data"""
        start_date = datetime.now() - timedelta(days=days)
        
        # Generate data for each building
        for building_num in range(1, 11):
            building_id = f'B{str(building_num).zfill(3)}'
            print(f"Generating data for {building_id}...")
            
            simulator = SensorSimulator(building_id, start_date)
            
            # Generate data in chunks
            readings_per_day = 288  # 5-min intervals = 288 per day
            chunk_size = 1000
            
            all_readings = []
            for day in range(days):
                daily_readings = simulator.generate_batch(
                    num_readings=readings_per_day
                )
                all_readings.extend(daily_readings)
                
                # Insert in chunks
                if len(all_readings) >= chunk_size:
                    df = pd.DataFrame(all_readings)
                    self.client.insert_df('smartbuild.sensor_readings', df)
                    print(f"  Inserted {len(all_readings)} readings")
                    all_readings = []
            
            # Insert remaining
            if all_readings:
                df = pd.DataFrame(all_readings)
                self.client.insert_df('smartbuild.sensor_readings', df)
                print(f"  Inserted {len(all_readings)} readings")
        
        print("✅ Data loading complete!")
    
    def verify_data(self):
        """Verify loaded data"""
        # Count total readings
        result = self.client.query(
            "SELECT count() as count FROM smartbuild.sensor_readings"
        )
        total_count = result.result_set[0][0]
        print(f"Total sensor readings: {total_count:,}")
        
        # Count by sensor type
        result = self.client.query("""
            SELECT sensor_type, count() as count
            FROM smartbuild.sensor_readings
            GROUP BY sensor_type
            ORDER BY count DESC
        """)
        print("\nReadings by sensor type:")
        for row in result.result_set:
            print(f"  {row[0]}: {row[1]:,}")

if __name__ == "__main__":
    loader = BatchLoader()
    
    print("Loading buildings...")
    loader.load_buildings()
    
    print("\nLoading sensor data (30 days)...")
    loader.load_sensor_data(days=30)
    
    print("\nVerifying data...")
    loader.verify_data()
```

**Hour 3-4: AutoCAD Floor Plan**

1. **Install AutoCAD** (if not already done)
   - Download from Autodesk Education
   - Install (takes 20-30 minutes)

2. **Create simple floor plan** (2 hours)
   - Open AutoCAD
   - Use architectural template
   - Draw 3 floor levels
   - Add sensor locations
   - Export as PNG and PDF

3. **Quick AutoCAD commands:**
   ```
   RECTANG - Draw rectangle (building outline)
   LINE - Draw walls
   CIRCLE - Draw sensor locations
   TEXT - Add labels
   LAYER - Organize by layers (walls, sensors, labels)
   PLOT - Export to PDF/PNG
   ```

#### Afternoon Session (4 hours)

**Hour 5-6: Weather Data Integration**

Create `src/data_generation/weather_fetcher.py`:

```python
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class WeatherFetcher:
    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.base_url = "http://api.openweathermap.org/data/2.5"
    
    def get_current_weather(self, city: str = "São Paulo"):
        """Fetch current weather"""
        url = f"{self.base_url}/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        return {
            'timestamp': datetime.now(),
            'city': city,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'cloud_cover': data['clouds']['all'],
            'description': data['weather'][0]['description']
        }

# Get free API key at: https://openweathermap.org/api
# Free tier: 60 calls/minute, 1,000,000 calls/month
```

**Hour 7-8: Initial Testing & Verification**

Create `notebooks/01_data_exploration.ipynb`:

```python
# Jupyter notebook for data exploration

import clickhouse_connect
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to ClickHouse
client = clickhouse_connect.get_client(
    host=os.getenv('CLICKHOUSE_HOST'),
    port=int(os.getenv('CLICKHOUSE_PORT')),
    username=os.getenv('CLICKHOUSE_USER'),
    password=os.getenv('CLICKHOUSE_PASSWORD')
)

# Query recent data
query = """
    SELECT 
        toStartOfHour(timestamp) as hour,
        sensor_type,
        avg(value) as avg_value
    FROM smartbuild.sensor_readings
    WHERE timestamp >= now() - INTERVAL 7 DAY
    GROUP BY hour, sensor_type
    ORDER BY hour, sensor_type
"""

df = client.query_df(query)

# Visualize temperature trends
temp_df = df[df['sensor_type'] == 'temperature']
fig = px.line(temp_df, x='hour', y='avg_value', 
              title='Average Temperature Over Last 7 Days')
fig.show()

# Check data quality
print(f"Total rows: {len(df)}")
print(f"Date range: {df['hour'].min()} to {df['hour'].max()}")
print(f"\nSensor types: {df['sensor_type'].unique()}")
```

---

### 🗓️ DAY 3: AI & Analytics (8 hours)

#### Morning Session (4 hours)

**Hour 1-2: Anomaly Detection**

Create `src/analytics/anomaly_detector.py`:

```python
from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np
import clickhouse_connect
from dotenv import load_dotenv
import os

load_dotenv()

class AnomalyDetector:
    def __init__(self):
        self.client = clickhouse_connect.get_client(
            host=os.getenv('CLICKHOUSE_HOST'),
            port=int(os.getenv('CLICKHOUSE_PORT')),
            username=os.getenv('CLICKHOUSE_USER'),
            password=os.getenv('CLICKHOUSE_PASSWORD')
        )
        self.model = IsolationForest(
            contamination=0.1,  # Expect 10% anomalies
            random_state=42
        )
    
    def fetch_training_data(self, building_id: str, days: int = 7):
        """Fetch recent data for training"""
        query = f"""
            SELECT 
                toHour(timestamp) as hour,
                toDayOfWeek(timestamp) as day_of_week,
                sensor_type,
                avg(value) as avg_value,
                stddevPop(value) as std_value
            FROM smartbuild.sensor_readings
            WHERE 
                building_id = '{building_id}'
                AND timestamp >= now() - INTERVAL {days} DAY
            GROUP BY hour, day_of_week, sensor_type
        """
        
        return self.client.query_df(query)
    
    def prepare_features(self, df: pd.DataFrame):
        """Prepare features for anomaly detection"""
        # Pivot to get sensor types as columns
        features = df.pivot_table(
            index=['hour', 'day_of_week'],
            columns='sensor_type',
            values='avg_value',
            fill_value=0
        ).reset_index()
        
        return features
    
    def train(self, building_id: str):
        """Train anomaly detection model"""
        df = self.fetch_training_data(building_id)
        features = self.prepare_features(df)
        
        X = features.drop(['hour', 'day_of_week'], axis=1)
        self.model.fit(X)
        
        return self.model
    
    def detect(self, building_id: str):
        """Detect anomalies in recent data"""
        df = self.fetch_training_data(building_id, days=1)
        features = self.prepare_features(df)
        
        X = features.drop(['hour', 'day_of_week'], axis=1)
        predictions = self.model.predict(X)
        scores = self.model.score_samples(X)
        
        # -1 indicates anomaly
        anomalies = features[predictions == -1].copy()
        anomalies['anomaly_score'] = scores[predictions == -1]
        
        return anomalies

if __name__ == "__main__":
    detector = AnomalyDetector()
    detector.train('B001')
    anomalies = detector.detect('B001')
    print(f"Found {len(anomalies)} anomalies")
    print(anomalies)
```

**Hour 3-4: Energy Prediction**

Create `src/analytics/energy_predictor.py`:

```python
from prophet import Prophet
import pandas as pd
import clickhouse_connect
from dotenv import load_dotenv
import os

load_dotenv()

class EnergyPredictor:
    def __init__(self):
        self.client = clickhouse_connect.get_client(
            host=os.getenv('CLICKHOUSE_HOST'),
            port=int(os.getenv('CLICKHOUSE_PORT')),
            username=os.getenv('CLICKHOUSE_USER'),
            password=os.getenv('CLICKHOUSE_PASSWORD')
        )
        self.model = None
    
    def fetch_historical_data(self, building_id: str, days: int = 30):
        """Fetch historical energy data"""
        query = f"""
            SELECT 
                toStartOfHour(timestamp) as ds,
                avg(value) as y
            FROM smartbuild.sensor_readings
            WHERE 
                building_id = '{building_id}'
                AND sensor_type = 'energy'
                AND timestamp >= now() - INTERVAL {days} DAY
            GROUP BY ds
            ORDER BY ds
        """
        
        df = self.client.query_df(query)
        return df
    
    def train(self, building_id: str):
        """Train Prophet model"""
        df = self.fetch_historical_data(building_id)
        
        self.model = Prophet(
            yearly_seasonality=False,
            weekly_seasonality=True,
            daily_seasonality=True
        )
        
        self.model.fit(df)
        return self.model
    
    def predict(self, hours: int = 168):  # 7 days
        """Generate predictions"""
        future = self.model.make_future_dataframe(
            periods=hours,
            freq='H'
        )
        
        forecast = self.model.predict(future)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    
    def calculate_accuracy(self, building_id: str):
        """Calculate model accuracy (MAPE)"""
        df = self.fetch_historical_data(building_id, days=7)
        
        # Split into train and test
        train_size = int(len(df) * 0.8)
        train = df[:train_size]
        test = df[train_size:]
        
        # Train on subset
        model = Prophet()
        model.fit(train)
        
        # Predict on test
        forecast = model.predict(test[['ds']])
        
        # Calculate MAPE
        mape = np.mean(np.abs(
            (test['y'].values - forecast['yhat'].values) / test['y'].values
        )) * 100
        
        return mape

if __name__ == "__main__":
    predictor = EnergyPredictor()
    predictor.train('B001')
    forecast = predictor.predict(hours=168)
    print("Next 7 days forecast:")
    print(forecast.tail(10))
    
    accuracy = predictor.calculate_accuracy('B001')
    print(f"\nModel accuracy (MAPE): {accuracy:.2f}%")
```

#### Afternoon Session (4 hours)

**Hour 5-6: Carbon Footprint Calculator**

Create `src/analytics/carbon_calculator.py`:

```python
import pandas as pd
import clickhouse_connect
from dotenv import load_dotenv
import os

load_dotenv()

class CarbonCalculator:
    def __init__(self):
        self.client = clickhouse_connect.get_client(
            host=os.getenv('CLICKHOUSE_HOST'),
            port=int(os.getenv('CLICKHOUSE_PORT')),
            username=os.getenv('CLICKHOUSE_USER'),
            password=os.getenv('CLICKHOUSE_PASSWORD')
        )
        
        # Grid carbon intensity (kg CO2 per kWh)
        # Brazil average: ~0.05 kg/kWh (clean grid)
        # US average: ~0.4 kg/kWh
        # Europe average: ~0.3 kg/kWh
        self.grid_intensity = 0.05
    
    def calculate_building_footprint(self, building_id: str, days: int = 30):
        """Calculate carbon footprint for a building"""
        query = f"""
            SELECT 
                toDate(timestamp) as date,
                sum(value) as daily_energy_kwh
            FROM smartbuild.sensor_readings
            WHERE 
                building_id = '{building_id}'
                AND sensor_type = 'energy'
                AND timestamp >= now() - INTERVAL {days} DAY
            GROUP BY date
            ORDER BY date
        """
        
        df = self.client.query_df(query)
        df['carbon_kg'] = df['daily_energy_kwh'] * self.grid_intensity
        df['carbon_tons'] = df['carbon_kg'] / 1000
        
        return df
    
    def calculate_savings_potential(self, building_id: str):
        """Calculate potential savings from optimization"""
        # Typical building can save 15-30% energy through optimization
        df = self.calculate_building_footprint(building_id, days=365)
        
        total_energy = df['daily_energy_kwh'].sum()
        total_carbon = df['carbon_kg'].sum()
        
        # Conservative 20% savings estimate
        potential_energy_savings = total_energy * 0.20
        potential_carbon_savings = total_carbon * 0.20
        
        # Assuming $0.12 per kWh
        potential_cost_savings = potential_energy_savings * 0.12
        
        return {
            'current_annual_energy_kwh': total_energy,
            'current_annual_carbon_kg': total_carbon,
            'potential_energy_savings_kwh': potential_energy_savings,
            'potential_carbon_savings_kg': potential_carbon_savings,
            'potential_cost_savings_usd': potential_cost_savings,
            'savings_percentage': 20.0
        }

if __name__ == "__main__":
    calculator = CarbonCalculator()
    
    footprint = calculator.calculate_building_footprint('B001', days=30)
    print("Last 30 days carbon footprint:")
    print(footprint)
    
    savings = calculator.calculate_savings_potential('B001')
    print("\nOptimization potential:")
    for key, value in savings.items():
        print(f"{key}: {value:,.2f}")
```

**Hour 7-8: Integration Testing**

Create `tests/test_analytics.py`:

```python
import unittest
from src.analytics.anomaly_detector import AnomalyDetector
from src.analytics.energy_predictor import EnergyPredictor
from src.analytics.carbon_calculator import CarbonCalculator

class TestAnalytics(unittest.TestCase):
    
    def test_anomaly_detection(self):
        detector = AnomalyDetector()
        detector.train('B001')
        anomalies = detector.detect('B001')
        self.assertIsNotNone(anomalies)
        print(f"✅ Anomaly detection: {len(anomalies)} anomalies found")
    
    def test_energy_prediction(self):
        predictor = EnergyPredictor()
        predictor.train('B001')
        forecast = predictor.predict(hours=24)
        self.assertEqual(len(forecast), 24)
        print(f"✅ Energy prediction: {len(forecast)} hours forecasted")
    
    def test_carbon_calculation(self):
        calculator = CarbonCalculator()
        footprint = calculator.calculate_building_footprint('B001', days=7)
        self.assertGreater(len(footprint), 0)
        print(f"✅ Carbon calculation: {len(footprint)} days calculated")

if __name__ == "__main__":
    unittest.main()
```

---

### 🗓️ DAY 4: Visualization & UI (8 hours)

*Full Streamlit dashboard code coming in Day 4 implementation...*

---

## 📦 Ready-to-Use Datasets

### Option 1: Simulated Data (Recommended - Full Control)
Use the `SensorSimulator` class provided above. Benefits:
- ✅ Complete control over patterns
- ✅ No data privacy concerns
- ✅ Can generate unlimited data
- ✅ Realistic patterns built-in

### Option 2: Public Datasets

**Smart Building Datasets:**

1. **Building Data Genome Project 2**
   - Source: https://github.com/buds-lab/building-data-genome-project-2
   - 3,053 buildings, 2 years of hourly data
   - Format: CSV
   - Size: ~2GB

2. **ECO Dataset (Swiss Residential)**
   - Source: http://vs.inf.ethz.ch/res/show.html?what=eco-data
   - 6 households, electrical consumption
   - 1-second granularity

3. **UK-DALE (UK Domestic Appliance-Level Electricity)**
   - Source: https://jack-kelly.com/data/
   - 5 UK houses, 2+ years
   - Power consumption per appliance

4. **AMPds2 (Almanac of Minutely Power dataset)**
   - Source: http://ampds.org/
   - 2-year electricity, water, gas data
   - 1-minute intervals

**Weather Data:**
- OpenWeatherMap API (free tier)
- NOAA Climate Data
- Weather Underground

---

## 🛠️ Essential Tools & Software

### Must-Have (Day 1)
- [ ] Python 3.9+
- [ ] VS Code or PyCharm
- [ ] Git
- [ ] ClickHouse Cloud account
- [ ] OpenWeatherMap API key

### Important (Day 2-3)
- [ ] Jupyter Notebook
- [ ] AutoCAD (Autodesk student)
- [ ] Postman (API testing)

### Nice-to-Have (Day 4-5)
- [ ] Fusion 360 (Autodesk student)
- [ ] Figma (UI design)
- [ ] OBS Studio (screen recording)

---

## ⚡ Time-Saving Tips

1. **Use Templates**
   - Start with provided code templates
   - Don't write from scratch
   - Copy-paste-modify approach

2. **Focus on Core Features**
   - Prioritize: Data ingestion → Analytics → Visualization
   - Skip: Authentication, advanced UI, mobile app

3. **Leverage Free Resources**
   - Pre-built AutoCAD blocks
   - Streamlit templates
   - ClickHouse examples

4. **Automated Testing**
   - Write tests early
   - Run frequently
   - Catch issues quickly

5. **Documentation as You Go**
   - Document while building
   - Take screenshots immediately
   - Write README sections daily

---

## 🎯 Success Checklist

By end of Day 5, you should have:

**Technical Deliverables:**
- [ ] ClickHouse database with 1M+ rows
- [ ] Data ingestion pipeline
- [ ] 3 ML models (anomaly, prediction, optimization)
- [ ] Interactive Streamlit dashboard
- [ ] AutoCAD floor plan
- [ ] Fusion 360 sensor model

**Documentation:**
- [ ] Comprehensive README
- [ ] Architecture diagrams
- [ ] API documentation
- [ ] Setup instructions

**Portfolio:**
- [ ] GitHub repository (public)
- [ ] Demo video (5-10 minutes)
- [ ] LinkedIn post
- [ ] Live demo (Streamlit Cloud)

**Impact Metrics:**
- [ ] Query performance < 100ms
- [ ] ML accuracy > 85%
- [ ] Professional visuals
- [ ] Clear value proposition

---

**You've got this! Let's build something amazing! 🚀**
