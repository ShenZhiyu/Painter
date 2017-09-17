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
    # # # # #

    # # # # #
    for l in cf.options('data'):
        ldata_np = np.fromstring(cf.get('data', l), dtype=float, sep=',')
        plt.bar(ldata_np[0::2], ldata_np[1::2])
        for x, y in zip(ldata_np[0::2], ldata_np[1::2]):
            # ha: horizontal alignment
            # va: vertical alignment
            plt.text(x + 0.0, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    plt.xticks(list(range(1,11)),[r'$m1$', r'$m2$', r'$m3$', r'$m4$', r'$m5$', r'$m6$', r'$m7$', r'$m8$', r'$m9$', r'$m10$',])
    # # # # #

    plt.savefig(filename.replace('txt', 'pdf'))