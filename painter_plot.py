#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:52:04 2017

@author: shenzy
"""

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

#    plt.xlim((-1, 2))
#    plt.ylim((-2, 3))
#    new_ticks = np.linspace(-1, 2, 5)
#    plt.xticks(new_ticks)
#    plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

#    ax = plt.gca()
#    ax.spines['right'].set_color('red')
#    ax.spines['top'].set_color('blue')
#    ax.xaxis.set_ticks_position('bottom')
#    ax.spines['bottom'].set_position(('data', 0))
#    ax.yaxis.set_ticks_position('left')
#    ax.spines['left'].set_position(('data',0))
    # # # # #

    for l in cf.options('data'):
        ldata_np = np.fromstring(cf.get('data', l), dtype=float, sep=',')
        plt.plot(ldata_np[0::2], ldata_np[1::2],
                    linestyle=cf.get('datastyle', l+'.linestyle') if cf.has_option('datastyle', l+'.linestyle') else None,
                    linewidth=cf.getfloat('datastyle', l+'.linewidth') if cf.has_option('datastyle', l+'.linewidth') else None,
                    label=l
                )
    plt.legend(loc='best')
    
    plt.annotate(r'$x=y$', xy=(2, 93), xycoords='data', xytext=(+30, +30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
    
    plt.savefig(filename.replace('txt', 'pdf'))
#    plt.show()
