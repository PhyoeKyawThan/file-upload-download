from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
# from db import db

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'files'

# db = db.DB()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        org_filename, fileExten = os.path.splitext(file.filename)
        _filename = request.form['filename']
        if file.filename != '':
            filename = f'{secure_filename(_filename)}{fileExten}'
            if filename not in os.listdir('files'):
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # data = {
                #     'fileName': secure_filename(_filename),
                #     'filePath': os.path.join(app.config['UPLOAD_FOLDER'], filename)
                # }
                # db.insert(data)
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

@app.route('/preview/<filename>')
def preview(filename):
    path = f'files/{filename}'
    return send_file(path, as_attachment=False)

if __name__=='__main__':
    app.run(debug=True)