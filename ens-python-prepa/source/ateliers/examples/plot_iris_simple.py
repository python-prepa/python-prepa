""" Affichage de la classes d'iris en fonction de la largeur et longueur
du sepal
"""

from matplotlib import pyplot as plt

from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
target = iris.target

# Une nouvelle figure
plt.figure(figsize=(4, 3))
plt.scatter(data[:, 0], data[:, 1], c=target)
plt.xlabel('Longueur du sepal (cm)')
plt.ylabel('Largueur du sepal (cm)')

# Mise en page de la figure
plt.tight_layout()

plt.show()
