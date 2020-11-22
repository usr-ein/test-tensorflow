FROM tensorflow/tensorflow:nightly-gpu

LABEL maintainer samuel.prevost@pm.me

WORKDIR /app

ENV TF_CPP_MIN_LOG_LEVEL 3
COPY . /app

RUN pip3 install -r /app/requirements.txt

# https://aws.amazon.com/blogs/opensource/demystifying-entrypoint-cmd-docker/
ENTRYPOINT ["python3"]
CMD ["/app/main.py"]
