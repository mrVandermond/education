import random, math


###Примеры###
# def system(x):
#     res = []
#     res.append( x[1] )
#     res.append( 1 - x[1] )
#     return res


# h = 0.01
# start = 0
# end = 1

# def system(x):
#     res = []
#     res.append( x[1] )
#     res.append( x[1] + 2 * x[0] )
#     return res


# h = 0.01
# start = 0
# end = 1

def system(x, t):
    res = []
    res.append( x[1] )
    res.append( (-5 * t * x[1] - 3 * x[0]) / t ** 2 )
    return res


h = 0.1
start = 1
end = 4

fname = open('outputtest.txt', 'r+')
fname.truncate()


def RungeCutta(x, start, end):

    xk = x[:]

    while start < end:

        write_str = str(round(start, 6))
        for i in range(len(xk)):
            write_str += '\t' + str(xk[i])
        write_str += '\n'
        fname.write(write_str)
        
        start += h
        n1k = system( xk, start )
        
        temp = []
        for i in range(len(xk)):
            temp.append( xk[i] + (h / 2) * n1k[i] )
        n2k = system(temp, start)
        
        temp = []
        for i in range(len(xk)):
            temp.append( xk[i] + (h / 2) * n2k[i] )
        n3k = system(temp, start)
        
        temp = []
        for i in range(len(xk)):
            temp.append( xk[i] + h * n3k[i] )
        n4k = system(temp, start)

        delta_xk = []
        for i in range(len(xk)):
            delta_xk.append( (h / 6) * (n1k[i] + 2 * n2k[i] + 2 * n3k[i] + n4k[i]) )
        for i in range(len(xk)):
            xk[i] += delta_xk[i]

        write_str = str(round(start, 6))
        for i in range(len(xk)):
            write_str += '\t' + str(xk[i])
        write_str += '\n'
        fname.write(write_str)

    return xk


###Основа###

count = 0
nu_r = []
results = []
eps = 1E-3

while True:

    if count  < 2:
        nu = random.random()
        nu_r.append(nu)
        # x0 = [nu, -1]
        # x0 = [nu, 1]
        x0 = [nu, 3]
        result = RungeCutta(x0, start, end)
        results.append(result)

        print(result)
    else:
        # nu = nu_r[count - 1] - ( ((nu_r[count - 1] - nu_r[count - 2]) * (results[count - 1][0] - (2 * math.exp(-1) + 2))) / (results[count - 1][0] - results[count - 2][0]) )
        # nu = nu_r[count - 1] - ( ((nu_r[count - 1] - nu_r[count - 2]) * (results[count - 1][0] - (math.exp(-1) + math.exp(2)))) / (results[count - 1][0] - results[count - 2][0]) )
        nu = nu_r[count - 1] - ( ((nu_r[count - 1] - nu_r[count - 2]) * (results[count - 1][0] + math.pow(4, -3))) / (results[count - 1][0] - results[count - 2][0]) )
        nu_r.append(nu)
        # x0 = [nu, -1]
        # x0 = [nu, 1]
        x0 = [nu, 3]
        result = RungeCutta(x0, start, end)
        results.append(result)

        print(result)
        # if abs(result[0] - (2 * math.exp(-1) + 2)) < eps:
        # if abs(result[0] - (math.exp(-1) + math.exp(2))) < eps:
        if abs(result[0] + math.pow(4, -3)) < eps:
            break
    count += 1