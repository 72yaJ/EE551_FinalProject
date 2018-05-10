#!/usr/bin/env python
# coding: utf-8
'''
File Name: reference_result.py
Edit Time: 20180421 1549

Content:
    get reference result
    
Version:
    1.0
'''

import pdb # debug module
import numpy as np
from time import gmtime, strftime

def get_median(data):
    data1 = data[:]
    data1.sort()
    half = len(data1) // 2
    return (data1[half] + data1[~half]) / 2

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
#    file_in = dataDir + 'mf_track_estimate_rightOrder.txt'
    file_in = dataDir + 'direct_score_result201805101837.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'reference_result'+t+'.txt'
    output_file = dataDir + title

    f_in = open(file_in, 'r')
    f_out = open(output_file, 'w')
    buff = []
    ii = 0

    for line in f_in:
        arr_in = line.strip().split('|')
        if arr_in[1] == 'None':
            arr_in[1] = '0'
        buff.append(float(arr_in[1]))
        ii = ii+1

#        pdb.set_trace()

        if ii == 6:
            ii = 0
            med = get_median(buff)
#            for jj in xrange(0, 6):
#                if buff[jj] > med:
##                    outStr = arr_in[0]+'|'+'1\n'
#                    outStr = '1\n'
#                    f_out.write(outStr)
#                if buff[jj] < med:
##                    outStr = arr_in[0]+'|'+'0\n'
#                    outStr = '0\n'
#                    f_out.write(outStr)
#                if buff[jj] == med:
#                    outStr = 'None\n'
#                    f_out.write(outStr)
#            buff = []


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

#            n = 0 # main 1
#            buff1 = np.ones(6)
#            for jj in xrange(0, 6):
#                if buff[jj] < med:
#                    buff1[jj] = 0
#                    n = n+1
#                else:
#                    buff[jj] = 1
#            for m in xrange(0, 6):
#                if n == 3:
#                    break
#                if buff1[m] != 0:
#                    buff1[m] = 0
#                    n = n+1
#            for item in buff1[:]:
#                outStr = str(int(item))+'\n'
#                f_out.write(outStr)
#            buff = []

    f_in.close()

if __name__ == '__main__':
    main()
