from fastapi import FastAPI
from polyglot.text import Text

from schema import Sentence

app = FastAPI()


@app.get('/health')
def health_check():
    return {'status': 'ok'}


@app.post('/entity')
def extract_entity(sentence: Sentence):
    text = Text(sentence.text)
    entities = {
        "per": [],
        "org": [],
        "loc": []
    }

    for ent in text.entities:
        if ent.tag == 'I-PER':
            entities['per'].append(' '.join(ent))
        elif ent.tag == 'I-LOC':
            entities['loc'].append(' '.join(ent))
        elif ent.tag == 'I-ORG':
            entities['org'].append(' '.join(ent))

    return entities
