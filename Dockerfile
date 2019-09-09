FROM python:3.5.3

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip
RUN apt-get install -y libffi6
RUN apt-get install -y libffi-dev
RUN apt-get install -y build-essential
RUN pip3 install flask_sqlalchemy
RUN pip3 install psycopg2-binary
RUN pip3 install cmake
RUN pip3 install dlib
RUN pip3 install face_recognition
RUN pip3 install flask_bcrypt flask_login pycronofy 
RUN pip3 install opencv-python
WORKDIR .
COPY . .
RUN pip3 install -r /IntellFRS/requirements.txt
RUN pip3 install flask_wtf pandas
EXPOSE 5000
EXPOSE 15432
ENTRYPOINT ["python3","run.py"]
