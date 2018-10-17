FROM python:3.4.9-slim-jessie

MAINTAINER mayankkapoormail@gmail.com
# Update aptitude with new repo
ENV LC_ALL=C

# Create app directory
WORKDIR /usr/src/app

# Install required software
RUN    apt-get update \
    && apt-get install -y putty
RUN    pip install pathlib \ 
    && pip install Flask \
    && pip install flask_json

# Bundle app source code
COPY app.py .

EXPOSE 5000
ENTRYPOINT ["python", "/usr/src/app/app.py"] 
