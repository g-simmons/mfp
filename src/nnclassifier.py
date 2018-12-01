import numpy as np
import sklearn
from sklearn.neural_network import MLPClassifier


class NNClassifier(object):
    def __init__(self):
        from sklearn.preprocessing import LabelEncoder

        self.le = LabelEncoder()
        self.clf = None

    def train(self, train_set):

        labels = [user["label"] for user in train_set]
        X = [np.array(user["feature"]) for user in train_set]
        y = self.le.fit_transform(labels)
        self.clf = MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto', beta_1=0.9,
                             beta_2=0.999, early_stopping=False, epsilon=1e-08,
                             hidden_layer_sizes=(600), learning_rate='constant',
                             learning_rate_init=0.001, max_iter=200, momentum=0.9,
                             nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
                             solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
                             warm_start=False)
        self.clf.fit(X, y)

    def test(self, test_set):
        acc = float(0)
        tp = float(0)
        fn = float(0)
        fp = float(0)

        for user in test_set:
            feature = user["feature"]
            label = user["label"]
            y = self.le.inverse_transform(self.clf.predict([feature]))
            if y == label:
                acc += 1
            if y == 1 and label == 1:
                tp += 1
            if y == 1 and label == 0:
                fp += 1
            if y == 0 and label == 1:
                fn += 1
        acc = acc / len(test_set)
        prec = tp / (tp + fp)
        recall = tp / (tp + fn)
        print("positive: " + str(tp + fp))
        return [acc, prec, recall]
