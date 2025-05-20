# Professional Portfolio Project - Image Processing & Data Science
# Image Colour Palette Generator
# Author : Abraham
from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import numpy as np
from collections import Counter
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def get_top_colors(image_path, num_colors=10):
    image = Image.open(image_path).convert('RGB')
    image = image.resize((150, 150))  # resize to speed up processing
    data = np.array(image)
    pixels = data.reshape(-1, 3)
    counts = Counter(tuple(color) for color in pixels)
    most_common = counts.most_common(num_colors)
    return [(rgb_to_hex(color), count) for color, count in most_common]

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file part", 400
        file = request.files['image']
        if file.filename == '':
            return "No selected file", 400
        
        filename = file.filename
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(save_path)

        colors = get_top_colors(save_path)
        return render_template('results.html', colors=colors)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050)
