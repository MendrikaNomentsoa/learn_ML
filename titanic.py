import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 1. Charge le dataset
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# 2. Affiche les infos générales (shape, dtypes, valeurs manquantes)
print(df.shape)
print(df.dtypes)
print(df.isnull()) 

# 3. Nettoie les valeurs manquantes

df.dropna(inplace=True)

# 4. Affiche la distribution des ages avec un histogram

plt.hist(df['Age'], bins=10)
plt.title('Distribution des ages')
plt.xlabel('Age')
plt.ylabel('Nombre de personnes')
plt.show()

# 5. Affiche le taux de survie par classe avec un bar chart

survived = df.groupby('Pclass')['Survived'].mean()

plt.bar(survived.index, survived.values)
plt.title('Taux de survie par classe')
plt.xlabel('Classe')
plt.ylabel('Taux de survie')
plt.show()

# 6. Affiche la relation entre age et prix du billet avec un scatter plot

plt.scatter(df['Age'], df['Fare'])
plt.title('Scatter plot')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

# 7. Affiche les statistiques générales avec describe()

print(df.describe())