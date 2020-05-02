#FROM python:3.7-slim
FROM modified_python_image:v01
#FROM continuumio/anaconda3
COPY ./app.py /deploy/
COPY ./model_test.py /deploy/
COPY ./sms.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./SoundPredict_91acu_35epochs.model /deploy/
COPY ./SoundPredict_aug_95.model /deploy/
COPY ./uploads /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install libsndfile1
#RUN apt-get install libsndfile1
#RUN apt-get install libsndfile1
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]


#FROM python:3.7-slim
# FROM continuumio/anaconda3
# COPY ./app.py /deploy/
# COPY ./model_test.py /deploy/
# COPY ./sms.py /deploy/
# COPY ./requirements.txt /deploy/
# COPY ./SoundPredict_91acu_35epochs.model /deploy/
# COPY ./SoundPredict_aug_95.model /deploy/
# COPY ./uploads /deploy/
# WORKDIR /deploy/
# RUN conda create -n sound_env python=3.7
# RUN conda install --file requirements.txt
# RUN conda activate sound_env
# EXPOSE 5000
# ENTRYPOINT ["python3", "app.py"]