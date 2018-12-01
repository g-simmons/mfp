import numpy as np
import sklearn

MAX_CV_FOLDS = 5
NUM_THREADS = 1


class SVMClassifier(object):
    def __init__(self):
        from sklearn.preprocessing import LabelEncoder

        self.le = LabelEncoder()
        self.clf = None

    def train(self, train_set):
        from sklearn.svm import SVC
        from sklearn.model_selection import GridSearchCV

        labels = [user["label"] for user in train_set]
        X = [np.array(user["feature"]) for user in train_set]
        y = self.le.fit_transform(labels)
        #self.clf = SVC(C=1, probability=True, class_weight='balanced', kernel='linear')
        C = [1, 2, 5, 10, 20, 100]
        kernel = "linear"
        tuned_parameters = [{"C": C, "kernel": [str(kernel)]}]
        cv_splits = max(2, min(MAX_CV_FOLDS, np.min(np.bincount(y)) // 5))
        self.clf = GridSearchCV(SVC(C=1, probability=True, class_weight='balanced'),
                                param_grid=tuned_parameters, n_jobs=NUM_THREADS,
                                cv=cv_splits, scoring='f1_weighted', verbose=1)
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
