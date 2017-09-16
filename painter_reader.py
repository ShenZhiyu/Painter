#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:58:56 2017

@author: shenzy
"""

import numpy as np


def getParameter(lines, parametername):
    try:
        parameter = lines[lines.index(parametername+'\n')+1].replace('\n','')
    except:
        parameter = None
    return parameter

def getData(lines):
    datastr = None
    try:
        datastr = lines[lines.index('#data#\n')+1:lines.index('#data end#')]
    except:
        pass
    try:
        datastr = lines[lines.index('#data#\n')+1:lines.index('#data end#\n')]
    except:
        pass
    if datastr is None:
        return None
    legend = []
    data_list = []
    for line in datastr:
        legend.append(line.split(': ')[0])
        data_list.append(line.split(': ')[1].replace('\n', '').split(','))
    return (legend, np.array(data_list))

def readtxt4plot(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    paralist = {}
    paraname = ['title', 'xlabel', 'ylabel', 'linestyle', 'linewidth']
    for pn in paraname:
        paralist[pn] = getParameter(lines, '#'+pn+'#')
    paralist['linewidth'] = float(paralist['linewidth'])
    
    legend, data_np = getData(lines)
    
    return (paralist, legend, data_np)