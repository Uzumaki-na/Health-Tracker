from sklearn.ensemble import IsolationForest
import joblib

# Load data
conn = sqlite3.connect('health_data.db')
df = pd.read_sql_query("SELECT * FROM health_metrics", conn)
conn.close()

# Feature extraction
X = df[['heart_rate', 'temperature']]

# Train Isolation Forest model
model = IsolationForest(contamination=0.01)
model.fit(X)

# Save the model
joblib.dump(model, 'health_model.pkl')
