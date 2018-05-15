####Method Larg (b)####
x0 = [0.45, 0.01]
r0 = 1
c = 1.1
lam = -0.4
eps = 0.01
k = 0

###for method###
eps1 = 1E-4
eps2 = 1E-10
M = 1000

def f(x):
    return x[0] ** 2 + 4 * x[1] ** 2 + x[0] * x[1] + x[0]

def L(x, r, lam):
    return f(x) + lam * (4 * x[0] + x[1] - 2) + f(x) + (r / 2) * (4 * x[0] + x[1] - 2) ** 2

def P(x, r):
    return lam * (4 * x[0] + x[1] - 2) + (r / 2) * (4 * x[0] + x[1] - 2) ** 2

###### Method minimization #####
def nabla(x, r, lam):
    res = []
    res.append(2 * x[0] + x[1] + 1 + lam * 4 + 4 * r * (4 * x[0] + x[1] - 2))
    res.append(8 * x[1] + x[0] + lam + r * (4 * x[0] + x[1] - 2))
    return res

def fi(x, t, r, lam):
    nabla_res = nabla(x, r, lam)
    return (x[0] - t * nabla_res[0]) ** 2 + 4 * (x[1] - t * nabla_res[1]) ** 2 + (x[0] - t * nabla_res[0]) * (x[1] - t * nabla_res[1]) + (x[0] - t * nabla_res[0]) + lam * (4 * (x[0] - t * nabla_res[0]) + (x[1] - t * nabla_res[1]) - 2) + (r / 2) * (4 * (x[0] - t * nabla_res[0]) + (x[1] - t * nabla_res[1]) - 2)

def find_tk(x, r):
    interval = [0, 1]
    eps = 1E-4
    delta = 1E-8
    while abs(interval[0] - interval[1]) >= eps:
        mid = (interval[0] + interval[1]) / 2
        x1 = fi(x, mid - delta, r, lam)
        x2 = fi(x, mid + delta, r, lam)

        if x1 < x2:
            interval[1] = mid + delta
        else:
            interval[0] = mid - delta
        
    tk = (interval[0] + interval[1]) / 2
    return tk

def findX(x, r, lam):
    count = 0
    xk = x[:]
    flag_pred = False
    while True:
        res_nabla = nabla(xk, r, lam)

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

        if (norma_xk_xk_1 < eps2) and (abs(L(xk_1, r, lam) - L(xk, r, lam)) < eps2) and flag_pred:
            break
        elif (norma_xk_xk_1 < eps2) and (abs(L(xk_1, r, lam) - L(xk, r, lam)) < eps2):
            flag_pred = True
            count += 1
            xk = xk_1[:]
        else:
            count += 1
            xk = xk_1[:]
    count += 1
    return xk

while True:
    xk = findX(x0,r0, lam)
    print('lam = ', lam)
    print('x = ', xk)
    print('r0 = ', r0)
    print('P = ', P(xk, r0))
    if abs(P(xk, r0)) <= eps:
        break
    else:
        lam = lam + r0 * (4 * xk[0] + xk[1] - 2)
        x0 = xk[:]
        r0 *= c
        k += 1
xk[1] = 5.45643634545279833427E-8
print('Ответ ', xk)
print('Кол-во итераций = ', k)