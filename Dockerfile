FROM python:2-alpine
MAINTAINER Denny R S Vriesman
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "./main.py" ]
