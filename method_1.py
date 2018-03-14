import random
import numpy
eps = 1E-5
N = 1000



# matr = [[-3., 4., -2.], [1., 0., 1.], [6., -6., 5.]]
# matr = numpy.array(matr)
# dim = 3
# sigma = -1.1

fname = open('input.txt', 'r') #lam1 = 20, lam2 = 5
#fname = open('input2.txt', 'r') #lam1 = 2, lam2 = 3
#fname = open('input3.txt', 'r')

dim = int(fname.readline())
sigma = float(fname.readline())
matr = [string.split() for string in fname]

for i in range(dim):
    for j in range(dim):
        matr[i][j] = float(matr[i][j])

matr = numpy.array(matr)


for i in range(dim):
    matr[i][i] -= sigma


x_0 = [1.]
for i in range(1, dim):
    x_0.append(0)
    
x_k = numpy.array(x_0)
lam_k_1 = random.uniform(-300, 300)
count = 0
while True:

    x = numpy.linalg.solve(matr, x_k)

    y_k = x
    norm_y = abs(max(y_k, key=abs))

    middle_val = 0
    for i in range(dim):
        middle_val += x_k[i] / float(y_k[i])

    middle_val /= dim
    lam_k = sigma + middle_val

    x_k = [elem / norm_y for elem in y_k]
    
    if abs(lam_k - lam_k_1) < eps:
        break
    else:
        lam_k_1 = lam_k
        count += 1
    if count > N:
        break

x_k = [round(x, 4) for x in x_k]
print(x_k)
print(lam_k)
print(count)