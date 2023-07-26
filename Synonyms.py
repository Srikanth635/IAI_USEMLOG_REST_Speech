# from nltk.corpus import wordnet
#
# synonyms = []
#
# for syn in wordnet.synsets("serve"):
#     for lm in syn.lemmas():
#         synonyms.append(lm.name())
# print(set(synonyms))

# wordhoard
from wordhoard import Synonyms
word = 'hold'
results = Synonyms(search_string=word, output_format='json').find_synonyms()
print(results)