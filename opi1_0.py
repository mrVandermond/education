#method dixotomii

delta = 0.2
eps = 0.5
interval = [-6, 4]
def f(x):
    return x ** 2 + 6 * x + 13

while abs(interval[0] - interval[1]) >= eps:
    mid = (interval[0] + interval[1]) / 2
    x1 = f(mid - delta)
    x2 = f(mid + delta)
    print('f(x1) = ', round(x1, 3), '\t', 'f(x2) = ', round(x2, 3))
    print('центральная точка', round(mid, 3))

    if x1 < x2:
        interval[1] = mid + delta
    else:
        interval[0] = mid - delta
    
    print('интервал ', round(interval[0], 3), '\t', round(interval[1], 3))

ans = f((interval[0] + interval[1]) / 2)
print(ans)