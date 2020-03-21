from ubuntu

MAINTAINER guneet "guneet@dal.ca"

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

WORKDIR /add_app

COPY . /add_app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5001

ENTRYPOINT ["python3"]
CMD ["add.py"]
