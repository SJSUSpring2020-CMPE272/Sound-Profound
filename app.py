import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
from model_test import Predict,PredictVersion2

#get current directory path
path = os.getcwd()
#get the path to save the uploaded audio file
upload_folder = path + "/uploads"

#only allowed extensions are .wav audio files
EXTENSIONS_ALLOWED = set(['wav'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_folder
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
CORS(app)
#function to get check if the file uploaded is of correct extention
def verify_extention(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in EXTENSIONS_ALLOWED


#route, currently / has to be changed
#POST method to get the uploaded file information
@app.route("/upload", methods=['POST'])
def file_upload():
    if request.method == 'POST':
        #check if data recieved is of file type
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)      
        #retrieve file from request
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file and verify_extention(file.filename):
            filename = secure_filename(file.filename)

            #save file to the upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #Function call to predict the sound type
            response = PredictVersion2(filename,upload_folder)


            #return redirect(url_for('uploaded_file',filename=filename))
            return response
        else:
            response = jsonify({"message":"File upload failed, extention not supported "})
            response.status_code=500
            return response
    return jsonify({"message":"File upload failed, reupload file "}), 500

@app.route('/')
def success():
  return "Success"

if __name__ == '__main__':

    #sess.init_app(app)
    app.run(host="0.0.0.0",port=5000, debug=True)