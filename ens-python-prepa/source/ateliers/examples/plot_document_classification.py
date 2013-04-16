"""
Example de classification de documents texte
=============================================
"""

import numpy as np
import pylab as pl

from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import RidgeClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


###############################################################################
# Load some categories from the training set
categories = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]

data_train = datasets.fetch_20newsgroups(subset='train', categories=categories)

data_test = datasets.fetch_20newsgroups(subset='test', categories=categories)

categories = data_train.target_names    # for case categories == None

# split a training set and a test set
y_train, y_test = data_train.target, data_test.target

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
X_train = vectorizer.fit(data_train.data)
X_train = vectorizer.transform(data_train.data)

X_test = vectorizer.transform(data_test.data)

feature_names = np.asarray(vectorizer.get_feature_names())


###############################################################################
# Benchmark classifiers
def benchmark(clf):
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)

    print

    score = 1 - metrics.f1_score(y_test, pred)
    print "error:   %0.3f" % score

    if hasattr(clf, 'coef_'):
        print "top 10 keywords per class:"
        for i, category in enumerate(categories):
            top10 = np.argsort(clf.coef_[i])[-10:]
            print "%s: %s" % (category, " ".join(feature_names[top10]))
        print

    print metrics.classification_report(y_test, pred,
                                        target_names=categories)

    print "confusion matrix:"
    print metrics.confusion_matrix(y_test, pred)

    print
    clf_descr = str(clf).split('(')[0]
    return clf_descr, score


results = []
for clf, name in (
        (RidgeClassifier(tol=1e-2, solver="lsqr"), "Ridge Classifier"),
        (KNeighborsClassifier(n_neighbors=10), "kNN")):
    print '_' * 80
    print name
    results.append(benchmark(clf))

results.append(benchmark(BernoulliNB(alpha=.01)))


# make some plots

clf_names = [r[0] for r in results]
score = [r[1] for r in results]

pl.title("Score (mesure de l'erreur)")
pl.bar([0, 1, 2], score, .6, label="score", color='r')
pl.xticks([0, 1, 2], clf_names)

pl.show()
