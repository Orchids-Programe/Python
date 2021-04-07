import numpy as np

(T0, I0, V0) = (10000,10,1000);
(beta, delta, c,p) = (3,0.2,0.3, 0.1);
x0= np.array([T0, I0, V0]).T
t0=0; tf=10;
def F(t,X):
    value = [-beta * X[1] * X[3], beta * X[1] * X[3] - delta * X[2], p * X[2] - c * X[3]].T;
    return value
