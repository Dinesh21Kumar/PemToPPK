FROM python:3.4.9-slim-jessie

MAINTAINER Dinesh Kumar "RJIL"
# Update aptitude with new repo
ENV LC_ALL=C

# Install software
RUN    apt-get update \
    && apt-get install -y git \
    && apt-get install -y putty
RUN git clone https://github.com/Dinesh21Kumar/PemToPPK.git \
    && pip install pathlib \ 
    && pip install Flask \
    && pip install flask_json 

EXPOSE 5000
CMD python /PemToPPK/app.py &
