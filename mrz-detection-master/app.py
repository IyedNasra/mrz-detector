from flask import Flask, request, redirect, url_for
import os
from imagetomrz import ExtractData
from parsemrz import parse

app = Flask(__name__)

UPLOAD_FOLDER = 'img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_image():
    ima_path = None  # Initialize the variable
    if request.method == 'POST':
        # Check if the file is an image
        file = request.files['image']
        if file and allowed_file(file.filename):
            # Move the file to the upload directory
            filename = file.filename
            relative_path = os.path.join(UPLOAD_FOLDER, filename)
            absolute_path = os.path.abspath(relative_path)
            file.save(absolute_path)
            ima_path = absolute_path
            list = ExtractData(ima_path)
            l = parse(list)
            return l
    else:
        data = {"error","Bad Request - Must use POST"}
        return data

if __name__ == '__main__':
    app.run(debug=True)
