FROM python:3.4.9-slim-jessie

MAINTAINER mayankkapoormail@gmail.com, dineshkumar13506@gmail.com
# Update aptitude with new repo
ENV LC_ALL=C

# Create app directory
WORKDIR /usr/src/app

# Install required software
RUN    apt-get update \
    && apt-get install -y putty-tools
RUN    pip install pathlib \ 
    && pip install Flask \
    && pip install flask_json \
    && pip install keystoneauth1 \
    && pip install python-keystoneclient

# Bundle app source code

COPY . .

EXPOSE 5000
ENTRYPOINT ["python", "/usr/src/app/app.py"] 
