#!/usr/bin/env python
# coding: utf-8
'''
File Name: sort_estimate_score.py
Edit Time: 20180508 1703

Content:
    sort the estimate score in right order
    output is userID itemSc
    
Version:
    1.1
'''

import pdb # debug module
#from numpy import size
from time import gmtime, strftime
import numpy as np


def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file1_in = dataDir + 'mf_track_estimated.txt'
    file2_in = dataDir + 'testTrack_hierarchy.txt'

    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'mf_track_estimate_rightOrder'+t+'.txt'
    file_out = dataDir + title

    f1_in = open(file1_in, 'r')
    f2_in = open(file2_in, 'r')
    f_out = open(file_out, 'w')

    ii = 6
    es_lastUserID = '1'
    lastAdd = 0

    for line in f2_in:

        if ii == 6:
            buff = []        
            ii = 0
            for es_line in iter(f1_in.readline, ''):
                arr_es = es_line.strip().split('|')
                es_userID = arr_es[0]
                if es_lastUserID != es_userID:
                    f1_in.seek(lastAdd)
                    es_lastUserID = es_userID

                    break
                buff.append(arr_es)
                es_lastUserID = es_userID
                lastAdd = f1_in.tell()

        arr_in = line.strip().split('|')
        ii = ii+1
#        out = [arr_in[0], arr_in[1], 'None']
        out = [arr_in[0], 'None']
        for item in buff[:]:
            if item[0] == arr_in[0] and item[1] == arr_in[1]:
                out[1] = float(item[2])
                break
        outStr = str(out[0])+'|'+str(out[1])+'\n'
        f_out.write(outStr)

    f1_in.close()
    f2_in.close()

if __name__ == '__main__':
    main()
