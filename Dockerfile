from alpine:latest
RUN apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev python3-dev libffi-dev openssl-dev make \
         && pip3 install --upgrade pip



WORKDIR /myapp
COPY . /myapp

RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["run.py"]