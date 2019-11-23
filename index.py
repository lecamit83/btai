D = [
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4]
]

from matrixfactorizontion import mf

if __name__ == '__main__' : 
    mf(D, K=2, b=0.01, stop_condition=2);