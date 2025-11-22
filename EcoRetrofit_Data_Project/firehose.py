import time
import json
import random
import uuid
import os
from datetime import datetime

# Try importing boto3, but handle failure if not installed (simulation mode)
try:
    import boto3
    from botocore.exceptions import NoCredentialsError
    BOTO3_AVAILABLE = True
except ImportError:
    BOTO3_AVAILABLE = False

class FirehoseGenerator:
    def __init__(self, num_homes=1000, s3_bucket=None, s3_folder='data/'):
        self.num_homes = num_homes
        self.homes = [str(uuid.uuid4()) for _ in range(num_homes)]
        self.s3_bucket = s3_bucket
        self.s3_folder = s3_folder
        self.s3_client = None

        if BOTO3_AVAILABLE and s3_bucket:
            try:
                self.s3_client = boto3.client('s3')
            except Exception as e:
                print(f"Warning: AWS S3 Client could not be initialized: {e}")

    def generate_batch(self):
        """Generates a batch of 1000 events (1 per home)."""
        events = []
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        for home_id in self.homes:
            # Simulate physics: High energy if temp is low (heating) or high (cooling)
            temp = random.uniform(-5, 35)
            energy_base = 0.5
            if temp < 10:
                energy_base += (10 - temp) * 0.2 # Heating
            elif temp > 25:
                energy_base += (temp - 25) * 0.3 # Cooling

            event = {
                "timestamp": timestamp,
                "home_id": home_id,
                "temperature": round(temp, 2),
                "humidity": round(random.uniform(30, 70), 2),
                "energy_kwh": round(energy_base + random.uniform(-0.1, 0.1), 4),
                "voltage": round(random.uniform(210, 230), 1)
            }
            events.append(event)
        return events

    def upload_to_s3(self, data):
        if not self.s3_client:
            print(f"[SIMULATION] Would upload {len(data)} records to s3://{self.s3_bucket}/{self.s3_folder}")
            return

        file_name = f"{self.s3_folder}batch_{int(time.time())}.json"
        json_data = "\n".join([json.dumps(record) for record in data]) # JSONEachRow format

        try:
            self.s3_client.put_object(Body=json_data, Bucket=self.s3_bucket, Key=file_name)
            print(f"Uploaded {file_name} to S3.")
        except NoCredentialsError:
            print("Error: AWS Credentials not found.")
        except Exception as e:
            print(f"Upload failed: {e}")

    def run(self, interval=5):
        print(f"Starting Firehose for {self.num_homes} homes. Interval: {interval}s")
        print("Press Ctrl+C to stop.")
        try:
            while True:
                batch = self.generate_batch()
                self.upload_to_s3(batch)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nFirehose stopped.")

if __name__ == "__main__":
    # Load config from env or defaults
    BUCKET = os.getenv("S3_BUCKET_NAME", "ecoretrofit-datalake-demo")

    generator = FirehoseGenerator(num_homes=1000, s3_bucket=BUCKET)
    generator.run(interval=2)
