from ubuntu

MAINTAINER guneet "guneet@dal.ca"

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

WORKDIR /ret_app

COPY . /ret_app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5002

ENTRYPOINT ["python3"]
CMD ["ret.py"]
