#!/usr/bin/env python
# coding: utf-8
'''
File Name: direct_score_AAGsingle.py
Edit Time: 20180420 1059

Content:
    calculate the genre of direct score to get signle score
    
Version:
    1.0
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in = dataDir + 'direct_score_AAG.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'direct_score_AAGsingle'+t+'.txt'
    output_file = dataDir + title

    fin = open(file_in, 'r')
    fOut = open(output_file, 'w')

    for line in fin:
        arr_in = line.strip().split('|')
            # arr_in[0] userID
            # arr_in[1] trackID
            # arr_in[2] albumScore
            # arr_in[3] artistScore
            # arr_in[4:] genreScore
        a = 0
        b = 0
        y = size(arr_in)
        for item in arr_in[4:y-1]:

#            pdb.set_trace()

            if item == 'None':
                continue
            a = a+float(item)
            b = b+1
        if b == 0:
            c = 'None'
        else:
            c = str(a/b)
        outStr = arr_in[0]+'|'+arr_in[1]+'|'+arr_in[2]+'|'+arr_in[3]+'|'+c
        fOut.write(outStr + '\n')

    fin.close()

if __name__ == '__main__':
    main()
