import numpy                            as np
from matplotlib import pyplot           as plt

#グラフ描画時のマーカー設定（適宜追加）
MARKER      = (('-o', '-*', '-v', '-D'),
               ('-o', '-*', '-v', '-D'))
#凡例のラベル（適宜追加）
LABEL       = (('0 mM', '1 mM', '3 mM', '5 mM'),
               ('0 mM', '1 mM', '3 mM', '5 mM'))
#軸のラベル
AXIS        = (('x-axis', 'y-axis'),
               ('xxxxxxxxxxxxxxxxxxxxxxxx', 'y-axis'))
#実験数
N           = (3, 3)
#csvファイルの名前
CSVFILE     = ('data1.csv', 'data2.csv')
#吐き出したいグラフの名前（読み込むファイルの数と同じにしておく）
GRAPHFILE   = ('data1.pdf', 'data2.pdf')

class AutoGraphDrawing():
    def __init__(self):
        #グラフ作成のパラメーターを取得
        self.settingParametersFORmakingGraph()

        #グラフの作成
        self.makingGraphProcess()


    def settingParametersFORmakingGraph(self):
        #マーカーのリスト
        self.markersFORgraph        = MARKER
        #データのラベル
        self.labelsOFdata           = LABEL
        #軸のラベル
        self.labelsOFaxes           = AXIS
        #実験数
        self.numberOFexperiment     = N
        #csvファイルのリスト
        self.namesOFcsvfiles        = CSVFILE
        #吐き出すグラフの名前
        self.namesOFgraphs          = GRAPHFILE
        #csvファイルの順番
        self.orderOFcsvfile         = np.arange(len(self.namesOFcsvfiles))

        #各パラメーターの数が揃っているかを判定（csfファイルの数を基準とする）
        correctNumber               = len(self.namesOFcsvfiles)
        if (len(self.markersFORgraph)   != correctNumber):
            print("The number of markers is incorrect.")
            exit()
        if (len(self.labelsOFdata)      != correctNumber):
            print("The number of labels of datas is inccorect.")
            exit()
        if (len(self.labelsOFaxes)      != correctNumber):
            print("The number of labels of axes is incorrect.")
            exit()
        if (len(self.numberOFexperiment)!= correctNumber):
            print("The number of N is incorrect.")
            exit()
        if (len(self.namesOFgraphs)     != correctNumber):
            print("The number of names of graphs is incorrect.")
            exit()

    def makingGraphProcess(self):
        for order in np.arange(len(CSVFILE)):
            GraphMaking(self.markersFORgraph[order],
                        self.labelsOFdata[order],
                        self.labelsOFaxes[order],
                        self.numberOFexperiment[order],
                        self.namesOFcsvfiles[order],
                        self.namesOFgraphs[order])

class GraphMaking():
    '''
    Essential argumants:
    1   N           the number of experiment on datas in csv file
    2   csvfile     the name with an extension (general one is csv) of csv file imported
    3   graphfile   the name with an extension (general one is pdf) of graph file exported
    '''
    def __init__(self, markers, labels, axes, numOFexp, csvfile, graphfile):
        #マーカーのリスト
        self.markers                = markers
        #データラベルのリスト
        self.labels                 = labels
        #軸ラベルのリスト
        self.axes                   = axes
        #実験数の代入
        self.numberOFexperiment     = numOFexp
        #読み込むcsvファイル名
        self.nameOFcsvfile          = csvfile
        #吐き出すgraphのファイル名
        self.nameOFgraphfile        = graphfile

        self.csvDataTOmatrix(self.numberOFexperiment, self.nameOFcsvfile)
        self.drawingGraph(self.markers, self.labels, self.axes, self.nameOFgraphfile)

    def csvDataTOmatrix(self, numOFexp, csvfile):
        '''
        Getting the horizonal and vertical datas in the graph from a csv data.
        '''
        #データを行列として取得
        data        = np.loadtxt(csvfile, delimiter=',', skiprows=1)

        #水平方向に使用するデータを取得
        self.x      = data[:, 0]
        #鉛直方向に使用するデータを取得
        vertical    = data[0:, 1:(data.shape[1])]
        self.y      = [vertical[:, int(numOFexp*i):int(numOFexp*(i+1))] for i in np.arange(int((data.shape[1]-1)/numOFexp))]

        #平均値と標準偏差の取得
        self.mean   = [self.y[i].mean(axis=1) for i in np.arange(int((data.shape[1]-1)/numOFexp))]
        self.std    = [self.y[i].std(axis=1) for i in np.arange(int((data.shape[1]-1)/numOFexp))]

    def drawingGraph(self, markers, labels, axes, graphfile):
        plt.figure(figsize=(9, 6))
        for i in np.arange(len(self.mean)):
            plt.errorbar(self.x, self.mean[i], yerr=self.std[i], c='Black', markersize=8, fmt=markers[i], ecolor='Black', label=labels[i])

        axesOption  = plt.gca()

        plt.xlabel(axes[0], fontsize=16)
        plt.ylabel(axes[1], fontsize=16)

        plt.tick_params(labelsize=12)

        plt.legend(loc='center', bbox_to_anchor=(0.5, -0.25), ncol=10, numpoints=1, frameon=False, fontsize=15)

        plt.subplots_adjust(top=0.95, bottom=0.25)

        plt.xlim([0, self.x.max()])
        plt.ylim([0, max([self.y[i].max() for i in np.arange(len(self.y))])])

        axesOption.xaxis.set_label_coords(0.5, -0.1)
        axesOption.yaxis.set_label_coords(-0.1, 0.5)

        plt.savefig(graphfile, format='pdf', dpi=300)

if __name__ == '__main__':
    AutoGraphDrawing()
