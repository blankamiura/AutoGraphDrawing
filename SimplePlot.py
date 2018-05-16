import numpy                as np
import matplotlib.pyplot    as plt
import seaborn              as sbn

# 珍しくclassじゃない．
# 最近classだと醜いことに気付き始めた．

def simplePlot() :
    # seabornはあった方がグラフがちょっと綺麗になる気がする
    sbn.set_style("ticks")
    # figureの描画カンバスを指定
    plt.figure(figsize=(8, 6))

    # 読み込みたいmeanとstdをcsvから抽出
    # これに関しては，日頃はPython上で生データから算出している
    mean    = np.loadtxt('ODmean.csv', delimiter=",", skiprows=1)
    std     = np.loadtxt('ODstd.csv', delimiter=",", skiprows=1)

    # graphのパラメータ
    ## colors of markers and lines
    color  = ('black', 'crimson', 'royalblue', 'limegreen', 'darkorchid')
    ## shape of markers
    marker = ('-o', '-o', '-o', '-o', '-o')
    ## labels of groups
    label  = ('0 mM', '1 mM', '3 mM', '5 mM', '10 mM')
    ## y軸に表示したいラベル
    ## 詳しくは下の方
    ytick  = ['0', '0.2', '0.4', '0.6', '0.8', '1.0']

    # 誤差棒突きプロットの描画
    # この際，ラベルは指定しない．ここで指定してしまうと，凡例に誤差棒付きのマーカーが設定されてしまう．
    for i in np.arange(5) :
        plt.errorbar(mean[:, 0], mean[:, i+1], yerr=std[:, i+1], c=color[i], markersize=6, fmt=marker[i], ecolor=color[i])

    # 凡例だけ指定するためのプロット
    # データはなんでもよく，カンバス外にくる様にして隠す．
    # matplotlibが最高にイカしていないと思うところ．
    for i in range(5) :
        plt.plot(-10, -10, c=color[i], markersize=6, marker='o', label=label[i])

    # x，y軸の表示幅の指定
    plt.xlim([0, 14])
    plt.ylim([0, 1])

    # y軸に表示させたい軸メモリの刻み方と，実際に表示させるラベル（ytick）
    # plt.xticksにすればx軸の設定ができる．
    # 上の方で指定したytickは，
    ## ytick = [0] + [str(i/10) for i in range(2, 11, 2)]
    # とかでも良いと思います．
    plt.yticks(np.arange(0, 1.1, 0.2), ytick)

    #illustratorで軸ラベルとかを付けることがあるので，plt.xlabel()とかは今回コメントアウト
    #plt.xlabel('Fxxk', fontsize=16)
    #plt.ylabel('Usahara bitch festival', fontsize=16)

    # メモリの数字の大きさ
    plt.tick_params(labelsize=16)
    # 凡例のあれやこれ
    plt.legend(loc='upper left', frameon=False, fontsize=16)

    # 発射
    plt.show()

    # 書き出しをする際は，ファイル名に拡張子を忘れない．
    #plt.savefig('axxlfxxk.pdf', format='pdf', dpi=300)

if __name__ == '__main__' :
    simplePlot()
