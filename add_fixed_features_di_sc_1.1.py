#!/usr/bin/env python
# coding: utf-8
'''
File Name: add_fixed_features_di_sc_1.1.py
Edit Time: 20180509 1708

Content:
    add fixed features to direct score
    file_in1: original file
    file_in2~: feature file
    file_out: file added feature

    1.0
    input1: di_AAGsAltrmAralmArtrmTrmAlmArmGem
            userID trackID albumScore artistScore genreMeanScore...
            tracksInOneAlbumMean albumsInOneArtistMean tracksInOneArtistMean...
            trackScMean albumScMean artistScMean genreScMean

    input2: mf_track_estimate_rightOrder_rank120
            userID trackScEstimate

    output: di_AAGsAltrmAralmArtrmTrmAlmArmGemTre
            userID trackID albumScore artistScore genreMeanScore...
            tracksInOneAlbumMean albumsInOneArtistMean tracksInOneArtistMean...
            trackScMean albumScMean artistScMean genreScMean...
            trackScEstimate

Version:
    1.1
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in1 = dataDir + 'di_AAGsAltrmAralmArtrmTrmAlmArmGem.txt'
    file_in2 = dataDir + 'mf_track_estimate_rightOrder_rank120.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'di_AAGsAltrmAralmArtrmTrmAlmArmGemTre'+t+'.txt'
    file_out = dataDir + title

    f_in1 = open(file_in1, 'r')
    f_in2 = open(file_in2, 'r')
    f_out = open(file_out, 'w')

    for line1 in f_in1:
        arr_in1 = line1.strip().split('|')
        out = arr_in1

        line2 = f_in2.readline()

#        pdb.set_trace()

        arr_in2 = line2.strip().split('|')

        out.append(arr_in2[1])
        outStr = str(out[0])
        for item in out[1:]:
            outStr = outStr+'|'+str(item)
        f_out.write(outStr+'\n')

    f_in1.close()
    f_in2.close()

if __name__ == '__main__':
    main()
