#method Fletcher-Rives
import numpy

x0 = [1.5, 0.1]
eps1 = 0.1
eps2 = 0.15
M = 100

def nabla(x):
    res = []
    res.append(2 * x[0] - x[1] + 1)
    res.append(16 * x[1] - x[0])
    return res

def f(x):
    return x[0] ** 2 + 8 * x[1] ** 2 - x[0] * x[1] + x[0]

def fi(x, t, d):
    return (x[0] + t * d[0]) ** 2 + 8 * (x[1] + t * d[1]) ** 2 - (x[0] + t * d[0]) * (x[1] + t * d[1]) + (x[0] + t * d[0])

def find_tk(x, d):
    interval = [-5, 5]
    eps = 1E-3
    delta = 1E-4
    while abs(interval[0] - interval[1]) >= eps:
        mid = (interval[0] + interval[1]) / 2
        x1 = fi(x, mid - delta, d)
        x2 = fi(x, mid + delta, d)

        if x1 < x2:
            interval[1] = mid + delta
        else:
            interval[0] = mid - delta
        
    tk = (interval[0] + interval[1]) / 2
    return tk


count = 0
xk = x0[:]
xk_1 = x0[:]
dk_1 = []
betta_k_1 = 0
str1 = ''
flag_pred = False

while True:
    flag6 = flag7 = False
    res_nabla = nabla(xk)
    res_nabla_xk_1 = nabla(xk_1)

    norma = abs(max(res_nabla, key=abs))
    if norma < eps1:
        str1 = 'norma < eps1'
        break
    
    if count >= M:
        str1 = 'count >= M'
    elif count == 0:
        flag6 = True
    elif count >= 1:
        flag7 = True

    dk = []

    if flag6:
        dk = [-item for item in res_nabla]

    if flag7:
        norma_nabla_xk = abs(max(res_nabla, key=abs))
        norma_nabla_xk_1 = abs(max(res_nabla_xk_1, key=abs))
        betta_k_1 = (norma_nabla_xk ** 2) / (norma_nabla_xk_1 ** 2)

        for i in range(len(xk)):
            dk.append(-res_nabla[i] + betta_k_1 * dk_1[i])
    
    tk = find_tk(xk, dk)

    xk1 = xk[:]
    for i in range(len(xk)):
        xk1[i] += tk * dk[i]

    temp = []
    for i in range(len(xk)):
        temp.append(xk1[i] - xk[i])

    norma_xk_xk_1 = abs(max(temp, key=abs))

    if (norma_xk_xk_1 < eps2) and (abs(f(xk1) - f(xk)) < eps2) and flag_pred:
        str1 = '3 exception'
        break
    elif (norma_xk_xk_1 < eps2) and (abs(f(xk1) - f(xk)) < eps2):
        flag_pred = True
        count += 1
        dk_1 = dk[:]
        xk_1 = xk[:]
        xk = xk1[:]
    else:
        flag_pred = False
        count += 1
        dk_1 = dk[:]
        xk_1 = xk[:]
        xk = xk1[:]

count += 1
print(xk1)
print(str1)
print('Количество итераций', count)    