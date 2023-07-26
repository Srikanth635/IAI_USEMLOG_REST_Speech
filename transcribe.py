import whisper
import torch
import time
# import nltk
# nltk.download('punkt')
# from nltk.tokenize import sent_tokenize
from datetime import datetime,timedelta
import rasa
def prints(result):
    for k,v in dict(result).items():
        if ((str(k)=='entities')and(len(v) > 1)):
            for ele in v:
                print(str(k)+":"+str(ele)+"\n")
        else:
            print(str(k)+":"+str(v)+"\n")

# import spacy
# sp = spacy.load('en_core_web_lg')
# sen = sp(u"Move the cup from the table")
# verbs = []
# for word in sen:
#     print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
#     if word.pos_ == "VERB":
#         verbs.append((word.text,word.pos_))
#
# print("VERBS: ",verbs)
#
# for entity in sen.ents:
#     print("FIRST ENTS : ",entity.text + ' - ' + entity.label_ + ' - ' + str(spacy.explain(entity.label_)))
#
# from spacy.tokens import Span
#
# ORG = sen.vocab.strings[u'PRODUCT']
# new_entity = Span(sen, 2, 3, label=ORG)
# sen.ents = list(sen.ents) + [new_entity]
#
# for entity in sen.ents:
#     print("Second ENTS : ",entity.text + ' - ' + entity.label_ + ' - ' + str(spacy.explain(entity.label_)))


#####################################################     RASA      ####################################################
# rasa run --enable-api --debug
# pick_up, put_down, drop, move
import requests
# text = requests.form.get('query')
# payload = {"sender": "Rasa", "text": "can you take the cutting board present on top of the fridge"}
# payload = {"sender": "Rasa", "text": "on top of the oven there is a cup, can you take hold of it"}
payload = {"sender": "Rasa", "text": "fetch the cup from the drawer"}
headers = {'content-type': 'application/json'}
response = requests.post('http://localhost:5005/model/parse', json=payload, headers=headers)
result = response.json()
prints(result)