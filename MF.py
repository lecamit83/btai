import numpy 
class MF():
    def __init__(self,R,K,apha,beta,iter):
        self.R = R
        self.rows,self.columns = R.shape
        self.K= K
        self.apha = apha
        self.beta = beta
        self.iter = iter

    def train(self):
        self.P = numpy.random.normal(scale=1./self.K,size =(self.rows,self.K))
        self.Q = numpy.random.normal(scale =1./self.K, size=(self.K,self.columns))
        #create a list of training dtata
        self.sapmles=[ (i,j,self.R[i,j])
        for i in range(self.rows)
        for j in range(self.columns)
        if (self.R[i,j]>0)
        ]

        for i in range(self.iter*self.columns*self.rows):
            numpy.random.shuffle(self.sapmles)
            a=0
            for j in range(self.K):
                a += self.P[u][k]*self.Q[k][i]
            e = self.sapmles[u][i] - a
            for k in range(self.K):
                self.P[u][k] = self.P[u][k] + self.beta(e*self.Q[k][i] - self.apha*self.P[u][i])
                self.Q[k][i] = self.Q[k][i] +self.beta(e*self.P[u][k]) - self.apha.self.Q[k][i]

    def full_matrix(self):
        return numpy.matmul(self.P, self.Q)            

R = numpy.array([[5,3,0,1],
[4,0,0,1],
[1,1,0,5],
[1,1,0,4],
[0,1,5,4]])

mf = MF(R,2,0.1,0.01,20)
mf.train()
print(mf.full_matrix(),'hihi')