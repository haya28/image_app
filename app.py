import os
import cv2
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from processing.resize import resize_image
from processing.contrast import adjust_contrast
from processing.gamma import gamma_correction
from processing.negative import negative_image
from processing.binarization import binarize_image
from processing.morphology import morphology_operation
from processing.edge_detection import sobel_edge_detection
from processing.inpainting import inpaint_image

# Flaskアプリの設定
app = Flask(__name__)

# 画像のアップロード先ディレクトリ
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

# アップロードフォルダの設定
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# アップロードされたファイルの拡張子チェック
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ルートページ（画像アップロード画面）
@app.route('/')
def index():
    return render_template('index.html')

# 画像アップロード処理
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return redirect(url_for('process', filename=filename))

    return redirect(request.url)

# 画像処理メニュー（処理を選択する画面）
@app.route('/process/<filename>')
def process(filename):
    return render_template('process.html', filename=filename)

# 画像の提供（アップロード画像を表示するため）
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# 画像処理API
@app.route('/process/<filename>/<operation>', methods=['GET'])
def process_image(filename, operation):
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output_path = os.path.join(app.config['PROCESSED_FOLDER'], filename)

    if operation == "resize":
        processed = resize_image(input_path, 200, 200)
    elif operation == "contrast":
        processed = adjust_contrast(input_path, 1.5)
    elif operation == "gamma":
        processed = gamma_correction(input_path, 2.2)
    elif operation == "negative":
        processed = negative_image(input_path)
    elif operation == "binarize":
        processed = binarize_image(input_path)
    elif operation == "morphology":
        processed = morphology_operation(input_path, "dilate", 3)
    elif operation == "edge":
        processed = sobel_edge_detection(input_path)
    else:
        return "Invalid operation", 400

    cv2.imwrite(output_path, processed)
    return redirect(url_for('processed_file', filename=filename))

@app.route('/processed/<filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == '__main__':
    # アップロードフォルダがなければ作成
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)
    app.run(debug=True)
