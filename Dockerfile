FROM python:3.8.10

WORKDIR /app

# ADD handtracking.py .

COPY . /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirement.txt

CMD ["python", "./test.py"]