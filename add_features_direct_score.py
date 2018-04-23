#!/usr/bin/env python
# coding: utf-8
'''
File Name: add_features_direct_score.py
Edit Time: 20180422 1934

Content:
    add features to direct score
    file_in1: original file
    file_in2~: feature file
    file_out: file added feature

    1.0 input1: direct_scoreAAGsingle
                userID trackID albumScore artistScore genreMeanScore
        input2: di_alID_trSc_mean
                userID albumID trackScMean
        input3: di_arID_alSc_mean
                userID artistID albumScMean
        input4: di_arID_trSc_mean
                userID artistID trackScMean
        output: di_AAGsAltrmeanAralmeanArtrmean
                userID trackID albumScore artistScore genreMeanScore tracksInOneAlbumMean...
                albumsInOneArtistMean tracksInOneArtistMean

Version:
    1.0 
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in1 = dataDir + 'direct_score_AAGsingle.txt'
    file_in2 = dataDir + 'di_alID_trSc_mean.txt'
    file_in3 = dataDir + 'di_arID_alSc_mean.txt'
    file_in4 = dataDir + 'di_arID_trSc_mean.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'di_AAGsAltrmeanAralmeanArtrmean'+t+'.txt'
    file_out = dataDir + title

    f_in1 = open(file_in1, 'r')
    f_in2 = open(file_in2, 'r')
    f_in3 = open(file_in3, 'r')
    f_in4 = open(file_in4, 'r')
    f_out = open(file_out, 'w')

    for line1 in f_in1:
        arr_in1 = line1.strip().split('|')
        line2 = f_in2.readline()
        arr_in2 = line2.strip().split('|')
        line3 = f_in3.readline()
        arr_in3 = line3.strip().split('|')
        line4 = f_in4.readline()
        arr_in4 = line4.strip().split('|')

        out = arr_in1[:]
        out.append(arr_in2[2])
        out.append(arr_in3[2])
        out.append(arr_in4[2])
        
        outStr = str(out[0])
        for item in out[1:]:
            outStr = outStr+'|'+str(item)
        f_out.write(outStr+'\n')

    f_in1.close()
    f_in2.close()
    f_in3.close()
    f_in4.close()

if __name__ == '__main__':
    main()
