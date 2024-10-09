import sqlite3

# Create SQLite database and table
conn = sqlite3.connect('health_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS health_metrics
             (timestamp TEXT, heart_rate INTEGER, temperature REAL, activity_level TEXT)''')

# Load data from CSV and insert into the database
df = pd.read_csv('wearable_data.csv')
df.to_sql('health_metrics', conn, if_exists='append', index=False)

conn.commit()
conn.close()
