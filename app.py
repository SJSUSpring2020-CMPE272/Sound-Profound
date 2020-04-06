import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

from model_test import Predict

#get current directory path
path = os.getcwd()
#get the path to save the uploaded audio file
upload_folder = path + "/uploads"

#only allowed extensions are .wav audio files
EXTENSIONS_ALLOWED = set(['wav'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_folder

#function to get check if the file uploaded is of correct extention
def verify_extention(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in EXTENSIONS_ALLOWED


#route, currently / has to be changed
#POST method to get the uploaded file information
@app.route("/", methods=['POST'])
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
            #result = Predict(filename,UPLOAD_FOLDER)


            #return redirect(url_for('uploaded_file',filename=filename))
            return {"message":"File saved at path "}, 200
    return {"message":"File upload failed, reupload file "}, 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
