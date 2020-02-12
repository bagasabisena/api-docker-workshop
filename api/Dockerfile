FROM python:3.7

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        gcc build-essential libicu-dev

RUN pip install numpy fastapi pytest uvicorn \
    requests pytest polyglot pycld2 morfessor pyicu

RUN polyglot download --quiet embeddings2.id ner2.id

COPY . /app
WORKDIR /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
