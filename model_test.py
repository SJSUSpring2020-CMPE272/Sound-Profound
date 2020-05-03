import librosa
import librosa.display
import numpy as np
import wave
import contextlib
import scipy.io.wavfile as wav
import os
import tensorflow as tf
from sms import send_email, send_msg
from flask import jsonify

modileNo = 3136525478
receiver_email = 'apoorv.mehrotra@sjsu.edu'

#get current directory path
path = os.getcwd()
#get the path to save the uploaded audio file
#model_path = path + "/model5_unshuf_aug_accu96.model"
#model_path1 = path + "/model4_shuf_aug_accu_97.model"
model_path2= path + "/SoundPredict_91acu_35epochs.model"
model_path3 = path + "/SoundPredict_aug_95.model"

model1=tf.keras.models.load_model(model_path2)
model2=tf.keras.models.load_model(model_path3)

def PredictVersion2(filename,path):
    file_path = path + '/' + filename
    categories = ['air_conditioner','car_horn','children_playing','dog_bark','drilling','engine_idling','gun_shot','jackhammer','siren','street_music']
    try:
        #Verify the video duration, should be greater than equal 
        # to 2.97 sec for good audio recognition
        (source_rate, source_sig) = wav.read(file_path)
        duration_seconds = len(source_sig) / float(source_rate)
        print(duration_seconds)
        if duration_seconds >= 2.97:
            #If required file size met, reshape the audio file to process through the model
            y, sr = librosa.load(path + '/' + filename, duration=2.97)
            ps = librosa.feature.melspectrogram(y=y, sr=sr)
            re_shape=np.array([ps.reshape( (128, 128, 1))])
            print(re_shape)
        else:
            response = jsonify({"status": "small_size", "message": "File size is small, should be greater than 3 seconds"})
            #print("Internal Server error: {}".format(err))
            response.status_code=200
            return response
        model_list = []
        model_list.append(model1)
        model_list.append(model2)
        index = 0
        percentage = 0
        for model in model_list:
            prediction = model.predict([re_shape]) 
            #prediction.shape
            index = 0
            percentage = 0
            for i in range(10):
                print(prediction[0][i])
                if(prediction[0][i]*100 > percentage):
                    index = i
                    percentage = prediction[0][i]*100
            if index == 6:
                percent = np.float64(percentage).item()
                percent=round(percent,2)
                type(percentage)
                type(percent)
                send_email(receiver_email,percent)
                send_msg(modileNo,percent)
                response = jsonify({"status":200, "sound_source":categories[index].capitalize(),
                 "surety":percent, "notification":"Sent"})
                return response
        return jsonify({"status":200, "sound_source":categories[index].capitalize(), "surety":percentage})
    except ValueError as err:
        response = jsonify({"status": 500, "message": str(err)})
        #print("Internal Server error: {}".format(err))
        response.status_code=500
        return response



def Predict(filename,path):
    file_path = path + '/' + filename
    categories = ['air_conditioner','car_horn','children_playing','dog_bark','drilling','engine_idling','gun_shot','jackhammer','siren','street_music']
    try:
        #Verify the video duration, should be greater than equal 
        # to 2.97 sec for good audio recognition
        (source_rate, source_sig) = wav.read(file_path)
        duration_seconds = len(source_sig) / float(source_rate)
        print(duration_seconds)
        if duration_seconds >= 2.97:
            #If required file size met, reshape the audio file to process through the model
            y, sr = librosa.load(path + '/' + filename, duration=2.97)
            ps = librosa.feature.melspectrogram(y=y, sr=sr)
            re_shape=np.array([ps.reshape( (128, 128, 1))])
            print(re_shape)
            model = tf.keras.models.load_model(model1)
            #Now, we can make a prediction:

            prediction = model.predict([re_shape]) 
            prediction.shape
            print(prediction)
            index = 0
            percentage = 0
            for i in range(10):
                print(prediction[0][i])
                if(prediction[0][i]*100 > percentage):
                    index = i
                    percentage = prediction[0][i]*100
            #if index == 6:
                #send_email(receiver_email)
                #send_msg(modileNo)
            #if(percentage > 75):
            return {"status":200, "sound_source":categories[index], "surety":percentage}
            #else:
            #    return {"status":"200","message":"Sound can't be predicted, Too much disturbance"}
        else:
            return {"status":"401","message":"File is to short"}, 401
    except ValueError as err:
        #print("Internal Server error: {}".format(err))
        return {"status": 500, "message": str(err)}, 500
            