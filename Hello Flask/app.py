import os
from flask import Flask, request, jsonify

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        image = request.files['image']
        if image.filename == '':
            return jsonify({'error': 'No selected image file'}), 400
        
        # Check if the uploaded file has an allowed extension
        if not allowed_file(image.filename):
            return jsonify({'error': 'Invalid image file format'}), 400
        
        # Set the path to the directory where the image should be saved
        save_dir = r'C:\Users\Zizou\Desktop\mrz-detection-master\img'
        
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        # Save the image to the specified directory
        image_path = os.path.join(save_dir, image.filename)
        image.save(image_path)
        
        return jsonify({'image_path': image_path})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)