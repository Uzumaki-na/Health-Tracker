from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('health_model.pkl')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    metrics = np.array([data['heart_rate'], data['temperature']]).reshape(1, -1)
    prediction = model.predict(metrics)
    result = 'Anomaly Detected' if prediction[0] == -1 else 'All Good'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
