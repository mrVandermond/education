import math
######EXAMPLE01#######
# h = 0.0025
# t = 0
# end = 2
# xk = [3, 0]
# fname = open('output1.txt', 'r+')
# fname.truncate()

# def f(x):
#     res = []
#     res.append(-2 * x[0] + 4 * x[1])
#     res.append(-x[0] + 3 * x[1])
#     return res

######EXAMPLE02#######
# h = 0.025
# t = 0
# end = 5
# xk = [-0.75, 1.25]

# fname = open('output2.txt', 'r+')
# fname.truncate()
# def f(x):
#     res = []
#     res.append( (x[0] ** 2 - x[1] ** 2 + 1) / (2 * x[1]) )
#     res.append( x[0] + x[1] )
#     return res

######EXAMPLE03#######
h = 0.0025
t = 1
end = 4
xk = [1, 0, 1]

fname = open('output3.txt', 'r+')
fname.truncate()
def f(x):
    res = []
    res.append( -1 * (x[0] ** 2) )
    res.append( x[0] * x[1] - 2 * (x[2] ** 2) )
    res.append( x[0] * x[2] )
    return res

while t < end:
    n1k = f( xk )
    
    temp = []
    for i in range(len(xk)):
        temp.append( xk[i] + (h / 2) * n1k[i] )
    n2k = f(temp)
    
    temp = []
    for i in range(len(xk)):
        temp.append( xk[i] + (h / 2) * n2k[i] )
    n3k = f(temp)
    
    temp = []
    for i in range(len(xk)):
        temp.append( xk[i] + h * n3k[i] )
    n4k = f(temp)

    delta_xk = []
    for i in range(len(xk)):
        delta_xk.append( (h / 6) * (n1k[i] + 2 * n2k[i] + 2 * n3k[i] + n4k[i]) )
    for i in range(len(xk)):
        xk[i] += delta_xk[i]
    t += h

    write_str = str(round(t, 6))
    for i in range(len(xk)):
        write_str += '\t' + str(xk[i])
    write_str += '\n'
    fname.write(write_str)