import joblib
import numpy as np
import pytest

def test_model_loading():
    """Ensure the model file exists and can be loaded."""
    model = joblib.load('models/random_forest_model.pkl')
    assert model is not None

def test_model_prediction():
    """Ensure the model accepts dummy input and returns a numerical price."""
    model = joblib.load('models/random_forest_model.pkl')
    # Use dummy values matching your feature count (e.g., 4 features)
    dummy_input = np.array([[1500, 3, 2, 10]]) 
    prediction = model.predict(dummy_input)
    assert isinstance(prediction[0], (int, float, np.float64))