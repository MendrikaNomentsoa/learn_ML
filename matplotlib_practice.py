#Matplotlib sert à visualiser les données — créer des graphiques. En ML on l'utilises pour explorer les données et comprendre les résultats.

import matplotlib
matplotlib.use('TkAgg')#dit à Matplotlib quel moteur utiliser pour afficher les graphiques.
import matplotlib.pyplot as plt
import numpy as np

"""
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y) # trace une ligne qui relie les points x et y
plt.title('Mon premier graphique') # ajoute un titre au graphique.
plt.xlabel('x') #  étiquettent les axes horizontal
plt.ylabel('y') #  étiquettent les axes vertical

plt.show() # affiche la fenêtre avec le graphique

plt.savefig('graphique.png') # telecharge une image du graphique dans le dossier grace au backend Agg

"""

"""
x = np.random.rand(50)
y = np.random.rand(50)  #  rand() — nombres décimaux entre 0 et 1


plt.scatter(x, y) # affiche juste des points sans les relier. Il montre la relation entre deux variables sans supposer d'ordre.
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""

#Histogram : Pour voir la distribution des valeurs — combien d'éléments sont dans chaque intervalle.
"""
ages = np.random.randint(18, 80, 200) # génère 200 nombres entiers aléatoires entre 18 et 80.

plt.hist(ages, bins=50) # bins=10 dit à Matplotlib de diviser les valeurs en 10 intervalles. Plus tu augmentes bins, plus les intervalles sont petits et précis.
plt.title('Distribution des ages')
plt.xlabel('Age')
plt.ylabel('Nombre de personnes')
plt.show()

"""

#Bar chart : Pour comparer des valeurs entre différentes catégories.
"""
categories = ['Alice', 'Bob', 'Charlie', 'David']
scores = [90, 85, 92, 78]

plt.bar(categories, scores)
plt.title('Scores par personne')
plt.xlabel('Nom')
plt.ylabel('Score')
plt.show()

"""

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

survived = df.groupby('Sex')['Survived'].mean() #  groupe les passagers par sexe, puis calcule la moyenne de survie pour chaque groupe
plt.bar(survived.index, survived.values)
plt.title('Taux de survie par sexe')
plt.xlabel('Sexe')
plt.ylabel('Taux de survie')
plt.show()