####Method penalty (a)#####

x0 = [0, 0]
r0 = 1
c = 1.1
eps = 1E-3
k = 0

###for method###
eps1 = 0.005
eps2 = 1E-10
M = 1000

def f(x):
    return x[0] ** 2 + 8 * x[1] ** 2 - x[0] * x[1] + x[0]

def F(x, r):
    return f(x) + (r / 2) * (2 * x[0] + 3 * x[1] - 1) ** 2

def P(x, r):
    return (r / 2) * (2 * x[0] + 3 * x[1] - 1) ** 2

###### Method minimization #####
def nabla(x, r):
    res = []
    res.append(2 * x[0] - x[1] + 1 + 2 * r * (2 * x[0] + 3 * x[1] - 1))
    res.append(16 * x[1] - x[0] + 3 * r * (2 * x[0] + 3 * x[1] - 1))
    return res

def fi(x, t, r):
    nabla_res = nabla(x, r)
    return (x[0] - t * nabla_res[0]) ** 2 + 8 * (x[1] - t * nabla_res[1]) ** 2 - (x[0] - t * nabla_res[0]) * (x[1] - t * nabla_res[1]) + (x[0] - t * nabla_res[0]) + (r / 2) * (2 * (x[0] - t * nabla_res[0]) + 3 * (x[1] - t * nabla_res[1]) - 1)

def find_tk(x, r):
    interval = [0, 1]
    eps = 1E-4
    delta = 1E-5
    while abs(interval[0] - interval[1]) >= eps:
        mid = (interval[0] + interval[1]) / 2
        x1 = fi(x, mid - delta, r)
        x2 = fi(x, mid + delta, r)

        if x1 < x2:
            interval[1] = mid + delta
        else:
            interval[0] = mid - delta
        
    tk = (interval[0] + interval[1]) / 2
    return tk

def findX(x, r):
    count = 0
    xk = x[:]
    flag_pred = False
    while True:
        res_nabla = nabla(xk, r)

        norma = abs(max(res_nabla, key=abs))
        if norma < eps1:
            break
        
        if count >= M:
            break
        
        tk = find_tk(xk, r)

        xk_1 = []
        xk_1.append(xk[0] - tk * res_nabla[0])
        xk_1.append(xk[1] - tk * res_nabla[1])

        temp = []
        for i in range(len(xk)):
            temp.append(xk_1[i] - xk[i])

        norma_xk_xk_1 = abs(max(temp, key=abs))

        if (norma_xk_xk_1 < eps2) and (abs(F(xk_1, r) - F(xk, r)) < eps2) and flag_pred:
            break
        elif (norma_xk_xk_1 < eps2) and (abs(F(xk_1, r) - F(xk, r)) < eps2):
            flag_pred = True
            count += 1
            xk = xk_1[:]
        else:
            count += 1
            xk = xk_1[:]
    count += 1
    return xk

while True:
    xk = findX(x0,r0)
    if P(xk, r0) <= eps:
        break
    else:
        x0 = xk[:]
        r0 *= c
        k += 1
    
print('Ответ ', xk)
print('Кол-во итераций = ', k)