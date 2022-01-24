import spacy

nlp = spacy.load("de_core_news_sm")
text = 'Schalte den Computer aus'
doc = nlp(text)

#print(doc.ents)
#for entity in doc.ents:
#    print(entity.text, '--- ', entity.label_)

for i in doc:
    #print(i.text, "---", i.pos_, "---", i.dep_,)
    if i.dep_ == 'ROOT':
        print("Action: ", i.head.text)
    if i.pos_ == 'NOUN' and not i.dep_ == 'ROOT':
        if i.dep_ == 'nk':
           print("Wo: ", i.text)
        elif i.dep_ == 'sb' or i.dep_ == 'oa':
            print("Was: ", i.text)
    if i.pos_ == 'ADV' or i.dep_ == 'svp':
        print("Wie: ", i.text)