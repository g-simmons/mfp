import json
import numpy as np


def onehot_feature():
    with open("users_shuffled.json", 'r') as f:
        users = json.load(f)
    with open("token_list.json", 'r') as f:
        token_list = json.load(f)
    with open("token_dict.json", 'r') as f:
        token_dict = json.load(f)
    dim = len(token_list)
    lb2num = {"below": 0, "above": 1, "target": 2}
    f.close()
    for id in users:
        feature = list(np.zeros(dim))
        for token in id["tokens"]:
            feature[token_list.index(token)] += 1
        id["feature"] = feature
        id["label"] = lb2num[id["label"]]
        del id["tokens"]
    i = 0
    for id in users:
        print(id)
        if i > 10:
            break
        i += 1
    with open('onehot_feature.json', 'w') as f:
        json.dump(users, f)

if __name__ == '__main__':
    onehot_feature()
