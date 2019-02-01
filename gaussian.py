
import numpy as np


class GaussianModel:
    
    def __init__(self,X):
        self.X = X
        self.u = mean(X)
        self.sigma = covMatrix(X)
        self.det = np.linalg.det(self.sigma)
        self.inv_sigma = np.linalg.inv(self.sigma)

    def gx(self,y):

        return np.log(self.det) + (y - self.u) * self.inv_sigma * np.matrix((y - self.u)).T


def covMatrix(X):
    # X is a d-component column vecto
    # nx is the dimention of the each X in sample
    # ny is the number of the sample
    ny,nx = np.shape(X)
    u = []

    # compute u
    [u.append(np.sum(X[:,i]) / ny)for i in range(0,nx)]

    u = np.array(u)

    # compute covariance matirx
    Mat = np.matrix(X - u).T * np.matrix(X - u) / (ny - 1)
    return Mat

def mean(X):
    if len(np.shape(X)) == 1:
        ny = np.size
    else:
        ny,nx = np.shape(X)
    u = []
    # compute u
    [u.append(np.sum(X[:, i]) / ny) for i in range(0, nx)]
    u = np.array(u)
    return u
