import spacy

nlp = spacy.load("de_core_news_sm")
text = 'Spile Russischer Hardbass in meinem Zimmer!'
doc = nlp(text)
print(doc.ents)
for entity in doc.ents:
    print(entity.text, '--- ', entity.label_)

for i in doc:
    print(i.text, "---", i.pos_, "---", i.dep_,)