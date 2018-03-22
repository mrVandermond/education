#method NewTon
import numpy

x0 = [1.5, 0.1]
eps1 = 0.05
eps2 = 0.25
M = 100

def nabla(x):
    res = []
    res.append(2 * x[0] - x[1] + 1)
    res.append(16 * x[1] - x[0])
    return res

def f(x):
    return x[0] ** 2 + 8 * x[1] ** 2 - x[0] * x[1] + x[0]

def fi(x, t):
    nabla_res = nabla(x)
    return (x[0] - t * nabla_res[0]) ** 2 + 8 * (x[1] - t * nabla_res[1]) ** 2 - (x[0] - t * nabla_res[0]) * (x[1] - t * nabla_res[1]) + (x[0] - t * nabla_res[0])

def find_tk(x):
    interval = [-5, 5]
    eps = 1E-3
    delta = 1E-4
    while abs(interval[0] - interval[1]) >= eps:
        mid = (interval[0] + interval[1]) / 2
        x1 = fi(x, mid - delta)
        x2 = fi(x, mid + delta)

        if x1 < x2:
            interval[1] = mid + delta
        else:
            interval[0] = mid - delta
        
    tk = (interval[0] + interval[1]) / 2
    return tk

count = 0
xk = x0
str1 = ''
Gesse = numpy.array([[2, -1], [-1, 16]])
inverse = numpy.linalg.inv(Gesse)
det = numpy.linalg.det(inverse)

flag_pred = False
while True:
    res_nabla = nabla(xk)

    norma = abs(max(res_nabla, key=abs))
    if norma < eps1:
        str1 = 'norma < eps1'
        break
    
    if count >= M:
        str1 = 'count >= M'
        break

    flag = True
    sobstv = numpy.linalg.eig(inverse)
    for i in range(len(sobstv[0])):
        if sobstv[0][i] < 0:
            flag = False
    
    dk = []
    xk_1 = []
    if flag:
        for i in range(len(Gesse)):
            temp = 0
            for j in range(len(Gesse)):
                temp += -1 * inverse[i][j] * res_nabla[j]
            dk.append(temp)
        
        for i in range(len(Gesse)):
            xk_1.append(xk[i] + dk[i])
    else:
        dk = [-item for item in res_nabla]
        tk = find_tk(xk)
        for i in range(len(Gesse)):
            xk_1.append(xk[i] + tk * dk[i])
    
    temp = []
    for i in range(len(xk)):
        temp.append(xk_1[i] - xk[i])

    norma_xk_xk_1 = abs(max(temp, key=abs))

    if (norma_xk_xk_1 < eps2) and (abs(f(xk_1) - f(xk)) < eps2) and flag_pred:
        str1 = '3 exception'
        break
    elif (norma_xk_xk_1 < eps2) and (abs(f(xk_1) - f(xk)) < eps2):
        flag_pred = True
        count += 1
        xk = xk_1
    else:
        count += 1
        xk = xk_1

count += 1
print(xk)
print(str1)
print(count)