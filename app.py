# app.py
from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('house_price_model_1.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    try:
        bedrooms = float(data.get('bedrooms'))
        bathrooms = float(data.get('bathrooms'))
        size_sqft = float(data.get('size_sqft'))
        
        # Prepare features for the model
        features = np.array([[bedrooms, bathrooms, size_sqft]])
        
        # Predict using the loaded model
        prediction = model.predict(features)
        
        return jsonify({'predicted_price': prediction[0]})
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'})

if __name__ == '__main__':
    app.run(debug=True)
