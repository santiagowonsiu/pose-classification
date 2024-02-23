from flask import Flask, request, jsonify
import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

with open('body_language.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/process', methods=['POST'])
def process_image():
    # Your image processing code here
    # You might receive an image through the request and then process it
    # For example, if you're receiving the image as a file:
    image_file = request.files.get('image')
    if not image_file:
        return jsonify({'error': 'No image provided'}), 400

    image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # Now you can use your existing code to process the image
    # However, you'll need to modify it to work with a single image
    # And return the results instead of displaying them

    # ...

    return jsonify({'result': 'Your result here'})

if __name__ == '__main__':
    app.run(debug=True)