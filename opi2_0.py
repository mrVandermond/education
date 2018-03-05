x0 = [1.5, 0.1]
eps1 = 0.25
eps2 = 0.5
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
    
    tk = find_tk(xk)
    nabla_res = nabla(xk)

    xk_1 = []
    xk_1.append(xk[0] - tk * nabla_res[0])
    xk_1.append(xk[1] - tk * nabla_res[1])

    temp = []
    for i in range(len(xk)):
        temp.append(xk_1[i] - xk[i])

    norma_xk_xk_1 = abs(max(temp, key=abs))

    if (norma_xk_xk_1 < eps2) and (abs(f(xk_1) - f(xk)) < eps2) and flag_pred:
        str1 = '3 excaption'
        break
    elif (norma_xk_xk_1 < eps2) and (abs(f(xk_1) - f(xk)) < eps2):
        flag_pred = True
        count += 1
        xk = xk_1
    else:
        count += 1
        xk = xk_1
count += 1

print('Ответ: ', xk_1)
print('Количество итераций', count)
print(str1)