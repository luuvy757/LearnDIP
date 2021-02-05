import numpy as np

class KNN():

    def train(self, x_train, y_train):
        self.Xtr = x_train
        self.Ytr = y_train
        
    def predict(self, x_pre):
        """

        x_pre: N x D
        """
        num_test = x_pre.shape[0]  # n

        Y_pre = np.zeros(num_test, dtype=self.Ytr.dtype)
        