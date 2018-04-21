# _*_ coding:utf-8 _*_
import numpy as np

class slp:
    def __init__(self,learningRate=0.03,epoch=100):
        self.learningRate=learningRate
        self.epoch=epoch

    def train(self,x,y):
        self.w=np.zeros(1+x.shape[1])
        for _ in range(self.epoch):
            for xi,target in zip(x,y):
                print(self.activate(x))
                update=self.learningRate*(target-self.activate(xi))
                print(update)
                print(self.w[1:]+xi*update)
                self.w[1:]+=update*xi
                self.w[0]+=update
        return self

    def net_input(self,x):
        return np.dot(x,self.w[1:])+self.w[0]

    def activate(self,x):
        return np.where(self.net_input(x)>=0.0,1,-1)


s=slp()
x=np.array([[1,0],[1,1],[0,1],[0,0]])
y=np.array([0,1,0,0])
s.train(x,y)
print(s.w)