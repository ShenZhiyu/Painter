#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:52:04 2017

@author: shenzy
"""

from sys import argv
import painter_reader
import matplotlib.pyplot as plt


if __name__ == '__main__':
    if len(argv) != 2:
        print('argv error!')
        exit()
    script, filename = argv
    para, legend, data = painter_reader.readtxt4plot(filename)
    
    plt.figure(figsize=(8, 5))
    plt.title(para['title'])
    plt.xlabel(para['xlabel'])
    plt.ylabel(para['ylabel'])

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

    for y in range(0,len(data[1:])):
        plt.plot(data[0], data[y+1], linestyle=para['linestyle'], linewidth=para['linewidth'], label=legend[y+1])
    plt.legend(loc='best')
    
    plt.annotate(r'$x=y$', xy=(2, 93), xycoords='data', xytext=(+30, +30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
    
    plt.show()