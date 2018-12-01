import json
import numpy as np
import mitie
import gensim
from gensim.models import FastText

def food2vec():
    with open("users_shuffled.json", 'r') as f:
        users = json.load(f)
    with open("token_list.json", 'r') as f:
        token_list = json.load(f)
    with open("token_dict.json", 'r') as f:
        token_dict = json.load(f)
    model = FastText.load("model_foods_as_sentences_full_fasttext_lower.model")
    lb2num = {"below": 0, "above": 1, "target": 2}
    #extractor = mitie.total_word_feature_extractor("total_word_feature_extractor.dat")
    #dim = extractor.num_dimensions
    #print(dim)
    dim = 100
    f.close()
    for id in users:
        feature = np.zeros(dim)
        llen = len(id["tokens"])
        if len(id["tokens"]) == 0:
            print id, id["tokens"]
        for token in id["tokens"]:
            if model.wv[token][0] != float("nan"):
                feature += model.wv[token]
            else:
                llen =llen - 1
        feature = feature / llen if llen > 0 else feature
        id["feature"] = list(feature)
        id["label"] = lb2num[id["label"]]
        del id["tokens"]
    i = 0
    for id in users:
        print(id)
        if i > 10:
            break
        i += 1
    with open('embedding_feature.json', 'w') as f:
            json.dump(users, f)

if __name__ == '__main__':
    food2vec()
