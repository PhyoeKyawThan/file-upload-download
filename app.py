from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'files'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'file uploaded'
    else:
        return redirect(url_for('index'))

@app.route('/view/<filename>', methods=['POST', 'GET'])
def view_file(filename):
    if request.method == 'GET':
        path = f'files/{filename}'
        return send_file(path, as_attachment=False)
    else:
        return 'Something '
@app.route('/download/<filename>', methods=['POST', 'GET'])
def download(filename):
    if request.method == 'GET':
        # try:
        #     with open(f'files/{filename}', 'rb') as selectFile:
        #         fileData = selectFile.read()
        #     with open(os.getcwd())
        # except FileNotFoundError as f:
        #     return 'Requested File not found on the server'
        path = f'files/{filename}'
        return send_file(path, as_attachment=False)


if __name__=='__main__':
    app.run(debug=True)