from sys import argv
import painter_reader
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    if len(argv) != 2:
        print('argv error!')
        exit()
    script, filename = argv
    
    cf = painter_reader.getcf(filename)

    # # # # #
    plt.figure(figsize=tuple(np.fromstring(cf.get('plot', 'figsize'), dtype=int, sep=',').tolist()))
    plt.title(cf.get('plot', 'title'))
    plt.xlabel(cf.get('plot', 'xlabel'))
    plt.ylabel(cf.get('plot', 'ylabel'))
    
    if cf.has_option('plot', 'ylim'):
        plt.ylim(tuple(np.fromstring(cf.get('plot', 'ylim'), dtype=float, sep=',').tolist()))
    # # # # #

    # # # # #
    xt1 = []
    xt2 = []
    for b in cf.options('data'):
        ldata_list = cf.get('data', b).split(',')
        plt.bar(list(map(float,ldata_list[1::3])), list(map(float,ldata_list[2::3])))
        for x, y in zip(list(map(float,ldata_list[1::3])), list(map(float,ldata_list[2::3]))):
            plt.text(x + 0.0, y + 0.05, '%.2f' % y, ha='center', va='bottom')
        xt1.extend(list(map(float, ldata_list[1::3])))
        xt2.extend(ldata_list[0::3])
    plt.xticks(xt1, xt2)
    # # # # #

    plt.savefig(filename.replace('txt', 'pdf'))
