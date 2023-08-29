from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Check if the file is an image
        file = request.files['image']
        if file and allowed_file(file.filename):
            # Move the file to the upload directory
            filename = file.filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))

            print('The image has been uploaded successfully!')

            return redirect(url_for('upload_image'))

    return '''
        <form action="" method="post" enctype="multipart/form-data">
            <input type="file" name="image">
            <input type="submit" value="Upload">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)