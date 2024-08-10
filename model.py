# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def train_and_save_model():
    # Load dataset
    df = pd.read_csv('train.csv')
    
    # Define features and target
    X = df[['bedrooms', 'bathrooms', 'size_sqft']]
    y = df['price']

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'house_price_model_1.pkl')
    print("Model trained and saved as 'house_price_model_1.pkl'.")

if __name__ == "__main__":
    train_and_save_model()
