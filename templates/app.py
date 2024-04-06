from flask import Flask, render_template, request, jsonify
import cv2
import pytesseract

app = Flask(__name__)

def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Preprocess the image (e.g., resize, convert to grayscale)
    # Your preprocessing steps here

    # Apply OCR to extract the text from the number plate
    text = pytesseract.image_to_string(image)

    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        file_path = 'uploads/' + file.filename
        file.save(file_path)
        number_plate_text = process_image(file_path)
        # Implement your logic to determine car company and state here
        result = "Car Company: XYZ, State: ABC"
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
