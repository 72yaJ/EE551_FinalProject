#!/usr/bin/env python
# coding: utf-8
'''
File Name: cal_direct_score_1.2.py
Edit Time: 20180422 2345

Content:
    calculate all direct score to get signle score

    1.2
    file_in: di_AAGsAltrmAralmArtrmTrmAlmArmGem
            userID trackID...
            albumScore artistScore genreMeanScore...
            tracksInOneAlbumMean albumsInOneArtistMean tracksInOneArtistMean...
            trackMean albumMean artistMean genreMean
    
Version:
    1.2
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in = dataDir + 'di_AAGsAltrmAralmArtrmTrmAlmArmGem.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'direct_score_result'+t+'.txt'
    file_out = dataDir + title

    f_in = open(file_in, 'r')
    f_out = open(file_out, 'w')

    w_al = 1 # the weight of album
    w_ar = 0.75 # the weight of artist
    w_ge = 0.25    # the weight of genre
    w_es = 0.9 # the weight of estimate
    w_TrInAl = w_es*w_al #the weight of mean track score in one album
    w_AlInAr = w_es*0.5 #the weight of mean album score in one artist
    w_TrInAr = w_es*(w_ar-w_AlInAr) #the weight of mean track score in one artist
            # w_TrInAl/w_es = w_al
            # (w_AlInAr+w_TrInAr)/w_es = w_ar
    w_es_mean = 1 # the weight of mean estimate
    w_tr_mean = w_es_mean*1 # the weight of track mean
    w_al_mean = w_es_mean*w_al  # the weight of album mean
    w_ar_mean = w_es_mean*w_ar  # the weight of artist mean
    w_ge_mean = w_es_mean*w_ge  # the weight of genre mean

    d_norm_all = w_al+w_ar+w_ge # denominator of normalization of all
    d_norm_al = w_al+w_TrInAl
    d_norm_ar = w_ar+w_AlInAr+w_TrInAr

    for line in f_in:
        n_norm_all = 0  # the numerator of normalization
        n_norm_al = 0   # the numerator of album
        n_norm_ar = 0   # the numerator of artist
        al_score = 0
        ar_score = 0
        ge_score = 0
        TrInAl_score = 0
        AlInAr_score = 0
        TrInAr_score = 0
        al_score_all = 0
        ar_score_all = 0
        arr_in = line.strip().split('|')
            # arr_in[0] userID
            # arr_in[1] trackID
            # arr_in[2] albumScore
            # arr_in[3] artistScore
            # arr_in[4] genreScore
            # arr_in[5] TrInAl
            # arr_in[6] AlInAr
            # arr_in[7] TrInAr
            # arr_in[8] TrackMean
            # arr_in[9] AlbumMean
            # arr_in[10] ArtistMean
            # arr_in[11] GenreMean

#        if arr_in[0] == '32':
#            pdb.set_trace()


        if arr_in[2] != 'None':
            al_score = w_al*float(arr_in[2])
            n_norm_al = n_norm_al+w_al
        if arr_in[5] != 'None':
            TrInAl_score = w_TrInAl*float(arr_in[5])
            n_norm_al = n_norm_al+w_TrInAl
        if n_norm_al != 0: 
            al_score_all = (al_score+TrInAl_score)/(n_norm_al/d_norm_al)
            n_norm_all = n_norm_all+w_al
        if n_norm_all == 0 and arr_in[9] != 'None':
            al_score_all = w_al_mean*float(arr_in[9])
            n_norm_all = n_norm_all+w_al

        if arr_in[3] != 'None':
            ar_score = w_ar*float(arr_in[3])
            n_norm_ar = n_norm_ar+w_ar
        if arr_in[6] != 'None':
            AlInAr_score = w_AlInAr*float(arr_in[6])
            n_norm_ar = n_norm_ar+w_AlInAr
        if arr_in[7] != 'None':
            TrInAr_score = w_TrInAr*float(arr_in[7])
            n_norm_ar = n_norm_ar+w_TrInAr
        if n_norm_ar != 0:
            ar_score_all = (ar_score+AlInAr_score+TrInAr_score)/(n_norm_ar/d_norm_ar)
            n_norm_all = n_norm_all+w_ar
        if n_norm_all == 0 and arr_in[10] != 'None':
            ar_score_all = w_ar_mean*float(arr_in[10])
            n_norm_all = n_norm_all+w_ar

        if arr_in[4] != 'None':
            ge_score = w_ge*float(arr_in[4])
            n_norm_all = n_norm_all+w_ge
        if n_norm_all == 0 and arr_in[11] != 'None':
            ge_score_all = w_ar_mean*float(arr_in[11])
            n_norm_all = n_norm_all+w_ar

        if n_norm_all == 0 and arr_in[8] != 'None':
            score = w_tr_mean*float(arr_in[8])
            outStr = arr_in[0]+'|'+str(score)
            f_out.write(outStr + '\n')
            continue
        if n_norm_all == 0:
            outStr = arr_in[0]+'|None'
            f_out.write(outStr + '\n')
            continue
        score = (al_score_all+ar_score_all+ge_score)/(n_norm_all/d_norm_all)
        outStr = arr_in[0]+'|'+str(score)
        f_out.write(outStr + '\n')

    f_in.close()

if __name__ == '__main__':
    main()
