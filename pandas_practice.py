import pandas as pd

"""
s = pd.Series([10, 20, 30, 40, 50])
print(s)

"""

"""
score = pd.Series([55, 89, 26], index=['Alice', 'John', 'Bob'])
print(score['Bob'])
print(score)

"""

#DataFrame

"""

data = {
    'nom': ['Alice', 'John', 'Bob'],
    'age': [17, 5, 45],
    'score': [55, 89, 26]
}

df = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df)

print(df['nom']) # une seul chrochet => une seul colonne 

print(df[['nom', 'score', 'age']]) #  deux crochet => plusieurs colonne

#print(df['nom', 'score']) # => erreur

print(df.loc['a']) # Une ligne par index

print(df.loc['c', 'score']) # Une valeur précise — ligne a, colonne 'score'

"""

"""
data = {
    'nom': ['Alice', 'John', 'Bob'],
    'age': [17, 5, 45],
    'score': [55, 89, 26]
}

df = pd.DataFrame(data)

print(df.shape)       # dimensions — (3, 3) → 3 lignes, 3 colonnes
print(df.dtypes)      # type de chaque colonne
print(df.info())      # résumé complet
print(df.describe())  # statistiques : moyenne, min, max, écart-type...
print(df.head(2))     # les 2 premières lignes
print(df.tail(2))     # les 2 dernières lignes

"""

#Filtreage
"""
data = {
    'nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28],
    'score': [90, 85, 92, 78]
}

df = pd.DataFrame(data)

print(df['age'] > 29)
print(df[df['age'] > 29])

# Les personnes avec un score supérieur à 85
print(df[df['score'] > 85])

"""

"""
data = {
    'nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28],
    'score': [90, 85, 92, 78]
}

df = pd.DataFrame(data)

# Ajouter une nouvelle colonne
df['mention'] = ['Bien', 'Assez Bien', 'Très Bien', 'Assez Bien']

# Créer une colonne à partir d'une autre
df['double_score'] = df['score'] * 2

# Modifier une colonne existante
df['age'] += 1 # OU df['age'] = df['age'] + 1

#df.loc['0'] = df['age'] * 2 => ERREUR
#modification specifique
df.loc[1, 'score'] *= 2 # OU df.loc[1, 'age'] = df.loc[0, 'age'] * 2

df.loc[0, 'age'] = 25

#Ajouter une nouvelle colonne dans une index specifique 
df.loc[0, 'prix'] =[1000]

# Supprimer une colonne
df.drop('prix', axis=1, inplace=True)

# Supprimer une ligne
df.drop(0, axis=0, inplace=True)

#axis=1 veut dire colonne, axis=0 veut dire ligne.



print(df)

"""

#Valeurs manquantes
"""
data = {
    'nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, None, 35, 28],
    'score': [90, 85, None, 78]
}

df = pd.DataFrame(data)

# Voir les valeurs manquantes
print(df.isnull()) #  retourne TRUE là où il manque une valeur.

# Compter les valeurs manquantes par colonne
print(df.isnull().sum())


# Supprimer les lignes avec des valeurs manquantes
df.dropna(inplace=True)

# Ou les remplacer par une valeur
df.fillna(0, inplace=True)

"""

#Charger un vrai fichier CSV

"""df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')"""

"""print(df.shape)
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Afficher les colonnes
print(df.columns)

# Les passagers qui ont survécu
print(df[df['Survived'] == 1])

# La moyenne d'age des passagers
print(df['Age'].mean())

# Les passagers de plus de 50 ans
print(df[df['Age'] > 50])

"""
"""

#********  groupby  =>  df.groupby('colonne_de_groupe')['colonne_a_calculer'].fonction()  ****************

# Moyenne d'age par sexe
print(df.groupby('Sex')['Age'].mean())

# Taux de survie par classe
print(df.groupby('Pclass')['Survived'].mean())

# Plusieurs calculs à la fois
print(df.groupby('Sex')['Age'].describe())

"""
#*********** merge => Ça combine deux DataFrames ensemble, comme un JOIN en SQL.  *************************

"""
df1 = pd.DataFrame({
    'nom': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

df2 = pd.DataFrame({
    'nom': ['Alice', 'Bob', 'David'],
    'score': [90, 85, 78]
})

result = pd.merge(df1, df2, on='nom') # on='nom' dit à Pandas de combiner les lignes qui ont le même nom. Charlie n'apparaît pas parce qu'il n'est pas dans df2, et David n'apparaît pas parce qu'il n'est pas dans df1.
print(result)

"""

# exercice
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# 1. Affiche le nombre de survivants par sexe
print(df.groupby('Sex')['Survived'].sum())

# 2. Affiche la moyenne d'age des survivants et des non survivants
print(df.groupby('Survived')['Age'].mean())

# 3. Affiche les passagers de première classe qui ont survécu
print(df[(df['Pclass'] == 1) & (df['Survived'] == 1)])

# 4. Supprime les lignes avec des valeurs manquantes
df.dropna(inplace=True)