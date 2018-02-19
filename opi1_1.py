#method golden ratio

import math

delta = 0.2
eps = 0.5
interval = [-6, 4]
def f(x):
    return x ** 2 + 6 * x + 13

yk = interval[0] + ((3 - math.sqrt(5)) / 2) * (interval[1] - interval[0])
zk = interval[0] + interval[1] - yk

while abs(interval[0] - interval[1]) >= eps:
    print('yk = ', round(yk, 4))
    print('zk = ', round(zk, 4))

    fyk = f(yk)
    fzk = f(zk)
    print('f(yk) = ', round(fyk, 4))
    print('f(zk) = ', round(fzk, 4))

    if fyk <= fzk:
        interval[1] = zk
        zk = yk
        yk = interval[0] + interval[1] - yk
    else:
        interval[0] = yk
        yk = zk
        zk = interval[0] + interval[1] - zk

    print('Интервал ', round(interval[0], 4), '\t', round(interval[1], 4))
        
ans = (interval[0] + interval[1]) / 2
ansfunc = f(ans)
print('Ответ:')
print('x* = ', ans)
print('f(x*) = ', ansfunc)