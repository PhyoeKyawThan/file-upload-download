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
        if file.filename != '':
            filename = secure_filename(file.filename)
            if filename not in os.listdir('files'):
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return render_template('index.html', success='Successfully File Uploaded')
            else:
                return render_template('index.html', msg = 'File already Exists')
        else:
            return render_template('upload.html', msg='File must not be empty to upload')
    else:
        return render_template('upload.html')

@app.route('/view', methods=['POST', 'GET'])
def view():
    data_list = os.listdir('files')
    return render_template('view.html', files=data_list)    
    
@app.route('/download/<filename>', methods=['POST', 'GET'])
def download(filename):
    if request.method == 'GET':
        download_path = f'files/{filename}'
        return send_file(download_path, as_attachment=True)
    else:
        return render_template('view.html')


if __name__=='__main__':
    app.run(debug=True)