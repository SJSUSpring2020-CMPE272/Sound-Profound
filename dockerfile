FROM modified_python_image:v01
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

EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
