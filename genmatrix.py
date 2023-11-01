import random

n = 2500
matrix = []

for row in range(n):    
    a = []
    for column in range(n):   
        a.append(random.randint(0, n))
    matrix.append(a)

with open("matrix.txt", "a+") as f:
    f.write(str(matrix))
