#!/usr/bin/env python
# coding: utf-8
'''
File Name: add_fixed_features_di_sc.py
Edit Time: 20180422 2140

Content:
    add fixed features to direct score
    file_in1: original file
    file_in2~: feature file
    file_out: file added feature

    1.0
    input1: di_AAGsAltrmeanAralmeanArtrmean
            userID trackID albumScore artistScore genreMeanScore...
            tracksInOneAlbumMean albumsInOneArtistMean tracksInOneArtistMean
    input2: di_UsID_trSc_mean
            userID trackScMean
    input3: di_UsID_alSc_mean
            userID albumScMean
    input4: di_UsID_arSc_mean
            userID artistScMean
    input5: di_UsID_geSc_mean
            userID genreScMean
    output: di_AAGsAltrmeanAralmeanArtrmean
            userID trackID albumScore artistScore genreMeanScore...
            tracksInOneAlbumMean albumsInOneArtistMean tracksInOneArtistMean...
            trackScMean albumScMean artistScMean genreScMean

Version:
    1.0 
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in1 = dataDir + 'di_AAGsAltrmeanAralmeanArtrmean.txt'
    file_in2 = dataDir + 'di_UsID_trSc_mean.txt'
    file_in3 = dataDir + 'di_UsID_alSc_mean.txt'
    file_in4 = dataDir + 'di_UsID_arSc_mean.txt'
    file_in5 = dataDir + 'di_UsID_geSc_mean.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'di_AAGsAltrmAralmArtrmTrmAlmArmGem'+t+'.txt'
    file_out = dataDir + title

    f_in1 = open(file_in1, 'r')
    f_in2 = open(file_in2, 'r')
    f_in3 = open(file_in3, 'r')
    f_in4 = open(file_in4, 'r')
    f_in5 = open(file_in5, 'r')
    f_out = open(file_out, 'w')

    line1 = f_in1.readline()
    arr_in1 = line1.strip().split('|')
    out = [arr_in1]
    lastUserID = arr_in1[0]

    line2 = f_in2.readline()
    line3 = f_in3.readline()
    line4 = f_in4.readline()
    line5 = f_in5.readline()

    for line1 in f_in1:

#        pdb.set_trace()

        arr_in1 = line1.strip().split('|')
        userID = arr_in1[0]
        if userID == lastUserID:
            out.append(arr_in1)
            continue

        while(line2):
            arr_in2 = line2.strip().split('|')
            if int(arr_in2[0]) > int(lastUserID):
                for ii in xrange(0, 6):
                    out[ii].append('None')
                break
            line2 = f_in2.readline()
            if arr_in2[0] == lastUserID:
                for ii in xrange(0, 6):
                    out[ii].append(arr_in2[1])
                break
            if int(arr_in2[0]) < int(lastUserID):
                continue

        while(line3):
            arr_in3 = line3.strip().split('|')
            if int(arr_in3[0]) > int(lastUserID):
                for ii in xrange(0, 6):
                    out[ii].append('None')
                break
            line3 = f_in3.readline()
            if arr_in3[0] == lastUserID:
                for ii in xrange(0, 6):
                    out[ii].append(arr_in3[1])
                break
            if int(arr_in3[0]) < int(lastUserID):
                continue

        while(line4):
            arr_in4 = line4.strip().split('|')
            if int(arr_in4[0]) > int(lastUserID):
                for ii in xrange(0, 6):
                    out[ii].append('None')
                break
            line4 = f_in4.readline()
            if arr_in4[0] == lastUserID:
                for ii in xrange(0, 6):
                    out[ii].append(arr_in4[1])
                break
            if int(arr_in4[0]) < int(lastUserID):
                continue

        while(line5):
            arr_in5 = line5.strip().split('|')
            if int(arr_in5[0]) > int(lastUserID):
                for ii in xrange(0, 6):
                    out[ii].append('None')
                break
            line5 = f_in5.readline()
            if arr_in5[0] == lastUserID:
                for ii in xrange(0, 6):
                    out[ii].append(arr_in5[1])
                break
            if int(arr_in5[0]) < int(lastUserID):
                continue

        for ii in xrange(0, 6):
            outStr = str(out[ii][0])
            for item in out[ii][1:]:
                outStr = outStr+'|'+str(item)
            f_out.write(outStr+'\n')
        out = [arr_in1]
        lastUserID = userID

    while(line2):
        arr_in2 = line2.strip().split('|')
        if int(arr_in2[0]) > int(lastUserID):
            for ii in xrange(0, 6):
                out[ii].append('None')
            break
        line2 = f_in2.readline()
        if arr_in2[0] == lastUserID:
            for ii in xrange(0, 6):
                out[ii].append(arr_in2[1])
            break
        if int(arr_in2[0]) < int(lastUserID):
            continue

    while(line3):
        arr_in3 = line3.strip().split('|')
        if int(arr_in3[0]) > int(lastUserID):
            for ii in xrange(0, 6):
                out[ii].append('None')
            break
        line3 = f_in3.readline()
        if arr_in3[0] == lastUserID:
            for ii in xrange(0, 6):
                out[ii].append(arr_in3[1])
            break
        if int(arr_in3[0]) < int(lastUserID):
            continue

    while(line4):
        arr_in4 = line4.strip().split('|')
        if int(arr_in4[0]) > int(lastUserID):
            for ii in xrange(0, 6):
                out[ii].append('None')
            break
        line4 = f_in4.readline()
        if arr_in4[0] == lastUserID:
            for ii in xrange(0, 6):
                out[ii].append(arr_in4[1])
            break
        if int(arr_in4[0]) < int(lastUserID):
            continue

    while(line5):
        arr_in5 = line5.strip().split('|')
        if int(arr_in5[0]) > int(lastUserID):
            for ii in xrange(0, 6):
                out[ii].append('None')
            break
        line5 = f_in5.readline()
        if arr_in5[0] == lastUserID:
            for ii in xrange(0, 6):
                out[ii].append(arr_in5[1])
            break
        if int(arr_in5[0]) < int(lastUserID):
            continue

    for ii in xrange(0, 6):
        outStr = str(out[ii][0])
        for item in out[ii][1:]:
            outStr = outStr+'|'+str(item)
        f_out.write(outStr+'\n')

    f_in1.close()
    f_in2.close()
    f_in3.close()
    f_in4.close()
    f_in5.close()

if __name__ == '__main__':
    main()
