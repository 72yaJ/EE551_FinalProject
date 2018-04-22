#!/usr/bin/env python
# coding: utf-8
'''
File Name: cal_direct_score.py
Edit Time: 20180420 1139

Content:
    calculate all direct score to get signle score
    
Version:
    1.1
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in = dataDir + 'direct_score_AAGsingle.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'direct_score_result'+t+'.txt'
    output_file = dataDir + title

    fin = open(file_in, 'r')
    fOut = open(output_file, 'w')

    w_al = 1 # the weight of album
    w_ar = 0.75 # the weight of artist
    w_ge = 0.25    # the weight of genre
    d_norm = w_al+w_ar+w_ge # denominator of normalization

    for line in fin:
        n_norm = 0  # the numerator of normalization
        al_score = 0
        ar_score = 0
        ge_score = 0
        arr_in = line.strip().split('|')
            # arr_in[0] userID
            # arr_in[1] trackID
            # arr_in[2] albumScore
            # arr_in[3] artistScore
            # arr_in[4] genreScore

        if arr_in[2] != 'None':
            al_score = w_al*float(arr_in[2])
            n_norm = n_norm+w_al
        if arr_in[3] != 'None':
            ar_score = w_ar*float(arr_in[3])
            n_norm = n_norm+w_ar
        if arr_in[4] != 'None':
            ge_score = w_ge*float(arr_in[4])
            n_norm = n_norm+w_ge
        if n_norm == 0:
            outStr = arr_in[0]+'|None'
            fOut.write(outStr + '\n')
            continue
        score = (al_score+ar_score+ge_score)/(n_norm/d_norm)
        outStr = arr_in[0]+'|'+str(score)
        fOut.write(outStr + '\n')

    fin.close()

if __name__ == '__main__':
    main()
