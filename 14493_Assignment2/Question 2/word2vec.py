import gensim
import os
from gensim.models import Word2Vec

# Memory efficient way of handling sentences
#taken from https://rare-technologies.com/word2vec-tutorial/
 
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
 
sentences = MySentences('/home/pratik/Desktop/nlp/Brown-data/Brown_no_tags/')
model=gensim.models.Word2Vec(sentences,min_count=2,size=300,window=4)
vocab=list(model.vocab.keys())
print vocab[:5]


