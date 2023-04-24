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
        if filename not in os.listdir('files'):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded'
        else:
            return render_template('index.html', msg = 'File already Exists')
    else:
        return render_template('upload.html')

@app.route('/view', methods=['POST', 'GET'])
def view():
    data_list = os.listdir('files')
    return render_template('view.html', files=data_list)    
    


if __name__=='__main__':
    app.run(debug=True)