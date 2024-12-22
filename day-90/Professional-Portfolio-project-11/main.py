from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from PIL import Image
import numpy as np
from collections import Counter
import webcolors

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def get_top_colors(image_path, top_n=10):
    """Extract top N colors from the image."""
    image = Image.open(image_path).convert('RGB')
    image = image.resize((100, 100))  # Resize to reduce processing time
    np_image = np.array(image)
    colors = np_image.reshape((-1, 3))

    # Count unique colors
    color_counts = Counter(map(tuple, colors))
    top_colors = color_counts.most_common(top_n)

    hex_colors = [webcolors.rgb_to_hex(color) for color, _ in top_colors]
    return hex_colors


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Process the image and get top colors
        top_colors = get_top_colors(file_path)

        return render_template('result.html', colors=top_colors)

    return "File type not allowed"


if __name__ == '__main__':
    app.run(debug=True)
