import numpy                    as np
from matplotlib import pyplot   as plt

MARKER      = ('-o', '-*', '-v', '-D')
LABEL       = ('a', 'b', 'c', 'd')

class GraphMaking():
    def __init__(self, N):
        self.N  = N
        self.dataSet()
        #self.graphDraw()

    def dataSet(self):
        '''
        Getting the horizonal and vertical datas in a graph from csv data.
        '''
        #データを行列として取得
        data        = np.loadtxt('data.csv', delimiter=',', skiprows=1)

        #水平方向に使用するデータを取得
        self.x      = data[:, 0]
        #鉛直方向に使用するデータを取得
        vertical    = data[0:, 1:(data.shape[1])]
        self.y      = []
        self.y.append(map(lambda i: vertical[:, self.N*i:self.N*(i+1)], np.arange((data.shape[1]-1/self.N))))

        print(self.y[0])

        #平均値及び標準偏差の算出
        self.mean   = np.empty([0, self.x.shape[0]]) #平均値
        for i in np.arange(len(self.y)):
            self.mean   = np.append(self.mean, [self.y[i].mean(axis=1)], axis=0)

    def graphDraw(self):
        for i in np.arange(len(self.mean)):
            plt.errorbar(self.x, self.mean[i], yerr=self.std[i], c='Black', markersize=8, fmt=MARKER[i], ecolor='Black', label=LABEL[i])

        plt.xlim([0, 144])
        plt.ylim([0, 36])
        #plt.show()

if __name__ == '__main__':
    GraphMaking(3)
