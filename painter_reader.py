#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:58:56 2017

@author: shenzy
"""

import configparser as cp

def getcf(filename):
    cf = cp.ConfigParser()
    try:
        cf.read(filename)
    except:
        cf = None
    return cf

if __name__ == '__main__':
    getcf('txt4plot_sample.txt')
