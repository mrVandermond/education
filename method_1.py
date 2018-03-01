import random
eps = 1E-10

###Ввод###

# matr = [[17, 6], [6, 8]]
# dim = 2
# sigma = 19.9

fname = open('input.txt', 'r')

dim = int(fname.readline())
sigma = int(fname.readline())
matr = [string.split() for string in fname]

for i in range(len(matr)):
    matr[i] = [int(x) for x in matr[i]]

###Построение матрицы с приближением###

for i in range(dim):
    matr[i][i] -= sigma

###Разложение матрицы###
U = []
L = []

for i in range(dim):
    U.append([])
    L.append([])
    for j in range(dim):
        U[-1].append(0)
        L[-1].append(0)

for i in range(dim):
    for j in range(dim):
        if j >= i:
            temp = 0
            if (i - 1) >= 0:
                for k in range(i):
                    temp += L[i][k] * U[k][j]
            U[i][j] = matr[i][j] - temp
        else:
            temp = 0
            if (j - 1) >= 0:
                for k in range(j - 1):
                    temp += L[i][k] * U[k][j]
            L[i][j] = (matr[i][j] - temp) / U[j][j]

for i in range(dim):
    L[i][i] = 1

#########################

###Начало итераций###
x_0 = []
for i in range(dim):
    x_0.append(1)

x_k = x_0
lam_k_1 = random.uniform(-300, 300)
count = 0
while True:
    
    ###Решение системы обратной итерации###
    y = []
    for i in range(dim):
        temp = 0
        if (i - 1) >= 0:
            for k in range(i):
                temp += L[i][k] * y[k]
        y.append(x_k[i] - temp)

    iterC = dim - 1
    x = []
    while iterC >= 0:
        temp = 0
        for k in range(iterC + 1, dim):
            temp += U[iterC][k] * x[-k]
        x.append((y[iterC] - temp) * 1.0 / U[iterC][iterC])
        iterC -= 1
    
    #########################################
    x.reverse()
    y_k = x
    norm_y = max(y_k, key=abs)

    middle_val = 0
    for i in range(dim):
        middle_val += x_k[i] * 1.0 / y_k[i]

    middle_val /= dim
    lam_k = sigma + middle_val

    x_k = [elem / norm_y for elem in y_k]

    if abs(lam_k - lam_k_1) < eps:
        break
    else:
        lam_k_1 = lam_k
        count += 1

print(x_k)
print(lam_k)
print(count)