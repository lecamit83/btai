import numpy

def matrix_factorization (R, H, W, K, steps, beta) : 
    step = 0
    while (step < steps) :
        for i in range(0, len(R)): 
            for j in range(0, len(R[0])) : 
                if(R[i][j] > 0) :
                    eij = R[i][j] - numpy.dot(H[i,:], W[:,j])
                    for k in range(0, K) :
                        H[i][k] += beta * (eij * W[k][j])
                        W[k][j] += beta * (eij * H[i][k])
        step += 1

    return numpy.dot(H, W)

R = [
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4]
]

M = len(R)
N = len(R[0])
K = 3
H = numpy.random.rand(M, K);
W = numpy.random.rand(K, N);


res = matrix_factorization (R, H, W, K, 3000, 0.1)
print(R)
print(res)

R = [[(round(res[i][j])) for j in range(0, len(res[0]))] for i in range(0, len(res))]
# for i in
print(R)