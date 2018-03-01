import random
import math

delta = 1E-5
eps = 1E-7
#matr = [[17, 6], [6, 8]]
#matr = [[3, 4], [4, 3]]
#matr = [[4, 1, -1], [1, 4, -1], [-1, -1, 4]]
#matr = [[-1 ,-6], [2, 6]]
#matr = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
matr = [[-3, 4, -2], [1, 0, 1], [6, -6, 5]]
y_0 = []
x_0 = []
x_k = []
norm_y0 = 0

for i in range(len(matr)):
    y_0.append(random.uniform(-5000, 5000))

norm_y0 = abs(max(y_0, key=abs))
x_0 = [y_0[i] / norm_y0 for i in range(len(y_0))]

x_k = x_0
count_iter = 0
lam_k = 0
lam_0 = random.uniform(-5000, 5000)
while True:
    y_k = []
    for i in range(len(matr)):
        temp = 0
        for j in range(len(matr)):
            temp += (matr[i][j] * x_k[j])
        y_k.append(temp)
    
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

print(round(lam_k, 4))
x_k  = [round(x, 4) for x in x_k]
print(x_k)
print(count_iter)