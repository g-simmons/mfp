import json
import numpy as np
import random
from svmclassifier import SVMClassifier
from nnclassifier import NNClassifier

def crossval(k=10, size=1000):

    with open("embedding_feature.json", 'r') as f:
        users = json.load(f)
    f.close()
    #users = [temp[user] for user in temp]
    users = [user for user in users if user["label"] != 2]
    #random.shuffle(users)

    print(len(users))
    acc = np.zeros(k)
    prec = np.zeros(k)
    recall = np.zeros(k)
    step = int(size / k)
    for i in range(k):
        print("Loop: %d" % (i+1))
        test_set = users[i*step:i*step+step]
        train_set = users[0:i*step] + users[i*step+step:size]
        print("train set size: %d" % (len(train_set)))
        print("test set size: %d" % (len(test_set)))
        #ic = SVMClassifier()
        ic = NNClassifier()
        ic.train(train_set)
        print("Finish training %d" % (i+1))
        [acc[i], prec[i], recall[i]] = ic.test(test_set)
        print acc[i], prec[i], recall[i]

    avg = np.mean(acc)
    std = np.std(acc)
    print "accuracy:", avg, std
    prec_avg = np.mean(prec)
    prec_std = np.std(prec)
    recall_avg = np.mean(recall)
    recall_std = np.std(recall)
    print "precision:", prec_avg, prec_std
    print "recall:", recall_avg, recall_std
    #with open('users_shuffled.json', 'w') as f:
    #        json.dump(users, f)

if __name__ == '__main__':
    crossval(k=5, size=1000)