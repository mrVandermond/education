import random

delta = 1E-5
eps = 1E-7
#matr = [[17, 6], [6, 8]]
#matr = [[3, 4], [4, 3]]
#matr = [[4, 1, -1], [1, 4, -1], [-1, -1, 4]]
matr = [[-1 ,-6], [2, 6]]
y_0 = []
x_0 = []
x_k = []
norm_y0 = 0

####Разложение матрицы###

N = len(matr)

U = []
L = []

for i in range(N):
    U.append([])
    L.append([])
    for j in range(N):
        U[-1].append(0)
        L[-1].append(0)

for i in range(N):
    for j in range(N):
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

for i in range(N):
    L[i][i] = 1

#########################

for i in range(len(matr)):
    y_0.append(random.uniform(-5000, 5000))

norm_y0 = abs(max(y_0, key=abs))
x_0 = [y_0[i] / norm_y0 for i in range(len(y_0))]

x_k = x_0
y_k = y_0
count_iter = 0
lam_k = 0
lam_0 = random.uniform(-5000, 5000)
while True:

    ###Решение системы обратной итерации###

    temp_x_k = []
    for i in range(len(matr)):
        temp = 0
        if (i - 1) >= 0:
            for k in range(i):
                temp += L[i][k] * y_k[k]
        temp_x_k.append(y_k[i] - temp)
    
    iterC = len(matr) - 1
    while iterC >= 0:
        temp = 0
        for k in range(iterC + 1, len(matr)):
            temp += U[iterC][k] * temp_x_k[k]
        y_k[iterC] = (temp_x_k[iterC] - temp) / U[iterC][iterC]
        iterC -= 1

    #######################################
    # for i in range(len(matr)):
    #     temp = 0
    #     for j in range(len(matr)):
    #         temp += (matr[i][j] * x_k[j])
    #     y_k.append(temp)
    
    count = 0
    temp = 0
    for i in range(len(matr)):
        if abs(x_k[i]) > delta:
            temp += y_k[i] / x_k[i]
            count += 1
    lam_k = temp / count
    
    norm_yk = abs(max(y_k, key=abs))
    x_k = [y_k[i] / norm_yk for i in range(len(matr))]

    if abs(lam_k - lam_0) < eps:
        break
    else:
        lam_0 = lam_k
        count_iter += 1

print(lam_k)
print(x_k)
print(count_iter)