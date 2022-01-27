import spacy

nlp = spacy.load("de_core_news_sm")


def make_first_nlp(text):
    time = False
    returnvalue = {"Action": "", "Wo": "", "Was": "", "Wie": "", "Wann": ""}
    doc = nlp(text)

    for i in doc:
        #print(i.text, i.pos_, i.dep_)
        if i.dep_ == 'ROOT':
            returnvalue["Action"] = i.head.text
            #print("Action: ", i.head.text)
        if i.pos_ == 'NOUN' and not i.dep_ == 'ROOT':
            if i.dep_ == 'nk':
                if i.text != "Uhr":
                    returnvalue["Wo"] = i.text
                    #print("Wo: ", i.text)
            elif i.dep_ == 'sb' or i.dep_ == 'oa' or i.dep_ == 'da':
                #print("Was: ", i.text)
                returnvalue["Was"] = i.text
        if i.pos_ == 'ADV' or i.dep_ == 'svp':
            #print("Wie: ", i.text)
            returnvalue["Wie"] = i.text
        if i.pos_ == "ADP":
            time = True
        if i.pos_ == "NUM" and time:
            #print("Zeit: ", i.text)
            returnvalue["Wann"] = i.text
    return returnvalue
