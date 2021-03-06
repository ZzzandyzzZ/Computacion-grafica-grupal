import numpy as np


class Camera(object):
    """ Class for representing pin-hole camera """

    def __init__(self, P=None, K=None, R=None, t=None):
        """ P = K[R|t] camera model. (3 x 4)
         Must either supply P or K, R, t """
        if P is None:
            try:
                self.extrinsic = np.hstack([R, t])
                P = np.dot(K, self.extrinsic)
            except TypeError as e:
                print('Invalid parameters to Camera. Must either supply P or K, R, t')
                raise

        self.P = P     # camera matrix
        self.K = K     # intrinsic matrix
        self.R = R     # rotation
        self.t = t     # translation
        self.c = None  # camera center

    def project(self, X):
        """ Project 3D homogenous points X (4 * n) and normalize coordinates.
            Return projected 2D points (2 x n coordinates) """
        x = np.dot(self.P, X)
        x[0, :] /= x[2, :]
        x[1, :] /= x[2, :]

        return x[:2, :]

    def qr_to_rq_decomposition(self):
        """ Convert QR to RQ decomposition with numpy.
        Note that this could be done by passing in a square matrix with scipy:
        K, R = scipy.linalg.rq(self.P[:, :3]) """
        Q, R = np.linalg.qr(np.flipud(self.P).T)
        R = np.flipud(R.T)
        return R[:, ::-1], Q.T[::-1, :]

    def factor(self):
        """ Factorize the camera matrix P into K,R,t with P = K[R|t]
          using RQ-factorization """
        if self.K is not None and self.R is not None:
            return self.K, self.R, self.t  # Already been factorized or supplied

        K, R = self.qr_to_rq_decomposition()
        # make diagonal of K positive
        T = np.diag(np.sign(np.diag(K)))
        if np.linalg.det(T) < 0:
            T[1, 1] *= -1

        self.K = np.dot(K, T)
        self.R = np.dot(T, R)  # T is its own inverse
        self.t = np.dot(np.linalg.inv(self.K), self.P[:, 3])

        return self.K, self.R, self.t

    def center(self):
        """  Compute and return the camera center. """
        if self.c is not None:
            return self.c
        elif self.R:
            # compute c by factoring
            self.c = -np.dot(self.R.T, self.t)
        else:
            # P = [M|−MC]
            self.c = np.dot(-np.linalg.inv(self.c[:, :3]), self.c[:, -1])
        return self.c


