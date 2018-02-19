#method Fibonachi

import math

delta = 0.2
eps = 0.5
interval = [-6, 4]
def f(x):
    return x ** 2 + 6 * x + 13

length_interval = interval[1] - interval[0]

F = [1, 1]
F1 = F2 = Fn = 1

while Fn < (length_interval / eps):
    Fn = F1 + F2
    F.append(Fn)
    F1 = F2
    F2 = Fn

print(F)
print(len(F))

yk = interval[0] + (F[-3] / F[-1]) * (interval[1] - interval[0])
zk = interval[0] + (F[-2] / F[-1]) * (interval[1] - interval[0])

count = 0
while abs(interval[0] - interval[1]) > eps:
    print('yk = ', round(yk, 4))
    print('zk = ', round(zk, 4))

    fyk = f(yk)
    fzk = f(zk)
    print('f(yk) = ', round(fyk, 4))
    print('f(zk) = ', round(fzk, 4))

    if fyk <= fzk:
        interval[1] = zk
        zk = yk
        yk = interval[0] + (F[-count - 4] / F[-count - 2]) * (interval[1] - interval[0])
    else:
        interval[0] = yk
        yk = zk
        zk = interval[0] + (F[-count - 3] / F[-count - 2]) * (interval[1] - interval[0])

    count += 1
    print('Интервал ', round(interval[0], 4), '\t', round(interval[1], 4))
    if count == (len(F) - 3):
        yn_2 = zn_2 = (interval[0] + interval[1]) / 2
        yn_1 = yn_2
        zn_1 = yn_1 + delta

        print('yk = ', round(yn_1, 4))
        print('zk = ', round(zn_1, 4))

        fyn_1 = f(yn_1)
        fzn_1 = f(zn_1)
        print('f(yk) = ', round(fyn_1, 4))
        print('f(zk) = ', round(fzn_1, 4))

        if fyn_1 <= fzn_1:
            interval[1] = zn_1
        else:
            interval[0] = yn_1

        print('Интервал ', round(interval[0], 4), '\t', round(interval[1], 4))
        break

ans = (interval[0] + interval[1]) / 2
ansfunc = f(ans)
print('Ответ:')
print('x* = ', ans)
print('f(x*) = ', ansfunc)