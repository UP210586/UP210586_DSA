import random

n = int(input("Dimension de la matriz: "))

matriz = [[0 for x in range(n)] for y in range(n)]    
numbers = random.sample(range(1, n*n+1), n*n)

for i in range(n):
    for j in range(n):
        matriz[i][j] = numbers[i*n + j]

print(matriz)