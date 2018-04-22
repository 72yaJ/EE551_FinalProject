#!/usr/bin/env python
# coding: utf-8
'''
File Name: meanScore_TrInAl.py
Edit Time: 20180421 1749

Content:
    get mean score of tracks rated in one album
    
Version:
    1.0
'''

import pdb # debug module
from numpy import mean
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in = dataDir + 'di_alID_trSc.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'di_alID_trSc_mean'+t+'.txt'
    output_file = dataDir + title

    f_in = open(file_in, 'r')
    f_out = open(output_file, 'w')

    for line in f_in:
        ii = 0
        buff = []
        arr_in = line.strip().split('|')
        for item in arr_in[2:]:
            if item == 'None':
                continue
            buff.append(float(item))
            ii = ii+1
        if ii == 0:
            outStr = arr_in[0]+'|'+arr_in[1]+'|'+'None\n'
            f_out.write(outStr)
        else:
            outStr = arr_in[0]+'|'+arr_in[1]+'|'+str(mean(buff))+'\n'
            f_out.write(outStr)

    f_in.close()

if __name__ == '__main__':
    main()
