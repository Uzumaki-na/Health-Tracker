import random
import pandas as pd
from datetime import datetime, timedelta

# Simulate wearable data
def generate_data():
    start_time = datetime.now() - timedelta(days=30)
    data = []
    for _ in range(1440):  # Simulate data for 30 days (minute interval)
        data.append({
            'timestamp': start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'heart_rate': random.randint(60, 100),
            'temperature': round(random.uniform(36.0, 37.5), 1),
            'activity_level': random.choice(['low', 'medium', 'high'])
        })
        start_time += timedelta(minutes=1)
    return pd.DataFrame(data)

# Save to CSV
df = generate_data()
df.to_csv('wearable_data.csv', index=False)
