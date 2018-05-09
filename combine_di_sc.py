#!/usr/bin/env python
# coding: utf-8
'''
File Name: combine_di_sc.py
Edit Time: 20180508 1250

Content:
    combine all the result to get a better one
    
Version:
    1.0
'''

import pdb # debug module
#from numpy import size
from time import gmtime, strftime
import numpy as np

def get_median(data):
    data1 = data[:]
    data1.sort()
    half = len(data1) // 2
    return (data1[half] + data1[~half]) / 2

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file1 = dataDir + 'reference_result_8651.txt'
    file2 = dataDir + 'reference_result_8598.txt'
    file3 = dataDir + 'reference_result_8363.txt'
    file4 = dataDir + 'reference_result_8323.txt'

    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'reference_result'+t+'.txt'
    file_out = dataDir + title

    f1_in = open(file1, 'r')
    f2_in = open(file2, 'r')
    f3_in = open(file3, 'r')
    f4_in = open(file4, 'r')
    f_out = open(file_out, 'w')

    f1 = f1_in.readlines()
    M = float(len(f1)) # num of scores
    n = 4
    s = np.asmatrix(list(map(float, f1)))
    f2 = f2_in.readlines()
    s = np.vstack([s, list(map(float, f2))])
    f3 = f3_in.readlines()
    s = np.vstack([s, list(map(float, f3))])
    f4 = f4_in.readlines()
    s = np.vstack([s, list(map(float, f4))])

    s = s.T
    x = 2*s-1

    x_y = np.empty((n, 1))
    x_y[0] = M*0.8651*2-M
    x_y[1] = M*0.8598*2-M
    x_y[2] = M*0.8363*2-M
    x_y[3] = M*0.8323*2-M

#    pdb.set_trace()
    
    x_x = np.matrix.dot(x.T, x).I
    a = np.matrix.dot(x_x, x_y)
    y = np.matrix.dot(s, a)

    
    buff = []
    ii = 0

    for yy in y:
        buff.append(yy)
        ii = ii+1

        if ii == 6:
            ii = 0
            med = get_median(buff)

            n = 0 # main 0
            buff1 = np.zeros(6)
            for jj in xrange(0, 6):
                if buff[jj] > med:
                    buff1[jj] = 1
                    n = n+1
                else:
                    buff[jj] = 0
            for m in xrange(0, 6):
                if n == 3:
                    break
                if buff1[m] != 1:
                    buff1[m] = 1
                    n = n+1
            for item in buff1[:]:
                outStr = str(int(item))+'\n'
                f_out.write(outStr)
            buff = []    

    f1_in.close()
    f2_in.close()
    f3_in.close()
    f4_in.close()

if __name__ == '__main__':
    main()
