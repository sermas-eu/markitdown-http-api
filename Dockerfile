FROM python:3

WORKDIR /app

RUN apt update -q && apt install -y exiftool

RUN python3 -m venv .venv

ADD requirements.txt .
RUN ./.venv/bin/pip3 install -r requirements.txt

ADD markitdown_http_api ./markitdown_http_api

RUN mkdir /data

EXPOSE 5012

ENV CACHE_DIR=/cache
ENV TORCH_HOME=/cache/torch
ENV HF_HOME=/cache/hf
ENV SPEECHBRAIN_CACHE_DIR=/cache/speechbrain

ENTRYPOINT [ "./.venv/bin/python3" ]
CMD ["-m", "flask", "--app", "markitdown_http_api.api:app", "run", "--host=0.0.0.0", "--port=5012"]
