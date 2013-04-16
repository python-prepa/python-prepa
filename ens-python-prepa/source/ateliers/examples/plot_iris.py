""" Affichage de la classes d'iris en fonction des different attributs
"""

from matplotlib import pyplot as plt

from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
target = iris.target

for feature_index1, feature_name1 in enumerate(iris.feature_names):
    for feature_index2, feature_name2 in enumerate(iris.feature_names):
        if feature_index1 >= feature_index2:
            continue
        # Une nouvelle figure
        plt.figure(figsize=(4, 3))
        plt.scatter(data[:, feature_index1], data[:, feature_index2],
                    c=target)
        plt.xlabel(feature_name1)
        plt.ylabel(feature_name2)

        # Mise en page de la figure
        plt.tight_layout()

plt.show()
