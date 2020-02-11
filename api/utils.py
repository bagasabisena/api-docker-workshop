from polyglot.text import Text


with open('../data/020101bus01.txt', 'r', encoding='utf-8') as f:
    raw_string = f.read()

text = Text(raw_string)

print(text.entities)
