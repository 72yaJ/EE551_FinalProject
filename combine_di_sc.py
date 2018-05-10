#!/usr/bin/env python
# coding: utf-8
'''
File Name: combine_di_sc.py
Edit Time: 20180509 1246

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
    file5 = dataDir + 'reference_result_8699.txt'
    file6 = dataDir + 'reference_result_6696.txt'
    file7 = dataDir + 'reference_result_6627.txt'
    file8 = dataDir + 'reference_result_5001.txt'
    file9 = dataDir + 'reference_result_8700.txt'
    file10 = dataDir + 'reference_result_8069.txt'
    file11 = dataDir + 'reference_result_8140.txt'
    file12 = dataDir + 'reference_result_7952.txt'
    file13 = dataDir + 'reference_result_8651_05101432.txt'
    file14 = dataDir + 'reference_result_8655.txt'
    file15 = dataDir + 'reference_result_7872.txt'
    file16 = dataDir + 'reference_result_8700_05101520.txt'
    

    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'reference_result'+t+'.txt'
    file_out = dataDir + title

    f1_in = open(file1, 'r')
    f2_in = open(file2, 'r')
    f3_in = open(file3, 'r')
    f4_in = open(file4, 'r')
    f5_in = open(file5, 'r')
    f6_in = open(file6, 'r')
    f7_in = open(file7, 'r')
    f8_in = open(file8, 'r')
    f9_in = open(file9, 'r')
    f10_in = open(file10, 'r')
    f11_in = open(file11, 'r')
    f12_in = open(file12, 'r')
    f13_in = open(file13, 'r')
    f14_in = open(file14, 'r')
    f15_in = open(file15, 'r')
    f16_in = open(file16, 'r')
    n = 16
    f_out = open(file_out, 'w')

    f1 = f1_in.readlines()
    M = float(len(f1)) # num of scores
    s = np.asmatrix(list(map(float, f1)))
    f2 = f2_in.readlines()
    s = np.vstack([s, list(map(float, f2))])
    f3 = f3_in.readlines()
    s = np.vstack([s, list(map(float, f3))])
    f4 = f4_in.readlines()
    s = np.vstack([s, list(map(float, f4))])
    f5 = f5_in.readlines()
    s = np.vstack([s, list(map(float, f5))])
    f6 = f6_in.readlines()
    s = np.vstack([s, list(map(float, f6))])
    f7 = f7_in.readlines()
    s = np.vstack([s, list(map(float, f7))])
    f8 = f8_in.readlines()
    s = np.vstack([s, list(map(float, f8))])
    f9 = f9_in.readlines()
    s = np.vstack([s, list(map(float, f9))])
    f10 = f10_in.readlines()
    s = np.vstack([s, list(map(float, f10))])
    f11 = f11_in.readlines()
    s = np.vstack([s, list(map(float, f11))])
    f12 = f12_in.readlines()
    s = np.vstack([s, list(map(float, f12))])
    f13 = f13_in.readlines()
    s = np.vstack([s, list(map(float, f13))])
    f14 = f14_in.readlines()
    s = np.vstack([s, list(map(float, f14))])
    f15 = f15_in.readlines()
    s = np.vstack([s, list(map(float, f15))])
    f16 = f16_in.readlines()
    s = np.vstack([s, list(map(float, f16))])





    s = s.T
    x = 2*s-1

    x_y = np.empty((n, 1))
    x_y[0] = M*0.8651*2-M
    x_y[1] = M*0.8598*2-M
    x_y[2] = M*0.8363*2-M
    x_y[3] = M*0.8323*2-M
    x_y[4] = M*0.8699*2-M
    x_y[5] = M*0.6696*2-M
    x_y[6] = M*0.6627*2-M
    x_y[7] = M*0.5001*2-M
    x_y[8] = M*0.8700*2-M
    x_y[9] = M*0.8069*2-M
    x_y[10] = M*0.8140*2-M
    x_y[11] = M*0.7952*2-M
    x_y[12] = M*0.8651*2-M
    x_y[13] = M*0.8655*2-M
    x_y[14] = M*0.7872*2-M
    x_y[15] = M*0.8700*2-M

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
    f5_in.close()
    f6_in.close()
    f7_in.close()
    f8_in.close()
    f9_in.close()
    f10_in.close()
    f11_in.close()
    f12_in.close()
    f13_in.close()
    f14_in.close()
    f15_in.close()
    f16_in.close()

if __name__ == '__main__':
    main()
