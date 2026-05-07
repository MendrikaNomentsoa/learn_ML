import numpy as np
"""
arr = np.array([1, 2, 3, 4, 5])

print(arr[0]) # premiere element
print(arr[-1]) # derniere element
print(arr[1:4]) # index 1 au index 3
print(arr[::2]) # un element sur deux 

"""

"""
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(mat[0, :]) # 1er ligne entier
print(mat[:, 1]) # 2eme colonne entier
print(mat[:, :]) 
print(mat[1, 2]) # ligne 1 , colonne 2
print(mat[1, 1])
print(mat[-2, -1])

"""

"""
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)
print(a ** 2)
print(a - 5)
"""

"""
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

print(np.sum(arr))      # somme de tous les éléments → 31
print(np.mean(arr))     # moyenne → 3.875
print(np.max(arr))      # valeur max → 9
print(np.min(arr))      # valeur min → 1
print(np.std(arr))      # écart-type → mesure la dispersion des valeurs
print(np.sort(arr))     # trie → [1 1 2 3 4 5 6 9]
print(np.argmax(arr))   # index du max → 5

"""

"""
arr = np.arange(12)
print(arr)

mat = arr.reshape(3, 4)
print(mat)

"""

"""
arr = np.array([10, 25, 3, 47, 8, 52])

print(arr > 20) # teste chaque élément et retourne un array de True/False
print(arr[arr > 20]) # utilise ce résultat pour garder uniquement les éléments qui sont True.
print(arr[arr % 2 == 0])

"""
#exercice

arr = np.arange(1,21)
resh = arr.reshape(4, 5)
print(resh)
print(resh[resh > 10])
print(resh.mean())

