import numpy as np
from flask import Flask, request, render_template
import pickle

# Initialize the flask app
app = Flask(__name__)

# Load the model from the specified path
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives input from the form, makes a prediction,
    and renders the result on the home page.
    """
    # Get all the feature values from the form as a list of strings
    features_str = [x for x in request.form.values()]

    # Convert the string features to a list of floats
    features_float = [float(x) for x in features_str]

    # Convert the list to a numpy array and reshape for a single prediction
    final_features = np.array(features_float).reshape(1, -1)

    # Make the prediction
    prediction = model.predict(final_features)

    # Get the predicted quality score (it's the first and only item in the array)
    output = int(prediction[0])

    # Create the output text
    prediction_text = f'Predicted Wine Quality: {output}'

    # Render the main page again, but this time with the prediction result
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)