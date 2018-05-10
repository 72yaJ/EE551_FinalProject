#!/usr/bin/env python
# coding: utf-8
'''
File Name: cal_direct_score_1.3.py
Edit Time: 20180509 1714

Content:
    calculate all direct score to get signle score

    1.3
    file_in: di_AAGsAltrmAralmArtrmTrmAlmArmGemTre
            userID trackID...
            albumScore artistScore genreMeanScore...
            tracksInOneAlbumMean albumsInOneArtistMean tracksInOneArtistMean...
            trackMean albumMean artistMean genreMean...
            trackEstimate
    
Version:
    1.3
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in = dataDir + 'di_AAGsAltrmAralmArtrmTrmAlmArmGemTre.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'direct_score_result'+t+'.txt'
    file_out = dataDir + title

    f_in = open(file_in, 'r')
    f_out = open(file_out, 'w')

    w_al = 1 # the weight of album
    w_ar = 0.75 # the weight of artist
    w_ge = 0.5  # the weight of genre
    w_tr = 0.25 # the weight of track

    w_al_sc = 1 # the weight of direct album score, arr_in[2]
    w_al_trinal = 0.5 # the weight of track in album, arr_in[5]
    w_al_alm = 0.25 # the weight of all album mean, arr_in[9]

    w_ar_sc = 1 # the wwight of direct artist score, arr_in[3]
    w_ar_alinar = 0.3 # the weight of album in artist, arr_in[6]
    w_ar_trinar = 0.2 # the weight of track in artist, arr_in[7]
    w_ar_ares = w_ar_alinar+w_ar_trinar # the weight of artist estimated by items in artist
    w_ar_arm = 0.25 # the weight of all artist mean, arr_in[10]

    w_ge_sc = 1 # the weight of direct genre score, arr_in[4]
    w_ge_gem = 0.25 # the weight of all genre mean, arr_in[11]

    w_tr_trm = 0.25 # the weight of all track mean, arr_in[8]
    w_tr_tre = 0.1 # the weight of track estimated by matrix factorization, arr_in[12]
    
    d_norm_all = w_al+w_ar+w_ge+w_tr # denominator of normalization of all
    d_norm_al = w_al_sc+w_al_trinal+w_al_alm
    d_norm_ar = w_ar_sc+w_ar_ares+w_ar_arm
    d_norm_ge = w_ge_sc+w_ge_gem
    d_norm_tr = w_tr_trm+w_tr_tre

    for line in f_in:
        n_norm_all = 0  # the numerator of normalization
        n_norm_al = 0   # the numerator of album
        n_norm_ar = 0   # the numerator of artist
        n_norm_ge = 0   # the numerator of genre
        n_norm_tr = 0   # the numerator of track
        
        al_score = 0
        ar_score = 0
        ge_score = 0
        tr_score = 0

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
            # srr_in[12] TrackEstimate

#        if arr_in[0] == '32':
#        pdb.set_trace()

        if arr_in[2] != 'None':
            al_score = al_score+w_al_sc*float(arr_in[2])
            n_norm_al = n_norm_al+w_al_sc
        if arr_in[5] != 'None':
            al_score = al_score+w_al_trinal*float(arr_in[5])
            n_norm_al = n_norm_al+w_al_trinal
        if arr_in[9] != 'None':
            al_score = al_score+w_al_alm*float(arr_in[9])
            n_norm_al = n_norm_al+w_al_alm
        if n_norm_al != 0: 
            al_score = al_score/(n_norm_al/d_norm_al)
            al_score = w_al*al_score
            n_norm_all = n_norm_all+w_al

        if arr_in[3] != 'None':
            ar_score = ar_score+w_ar_sc*float(arr_in[3])
            n_norm_ar = n_norm_ar+w_ar_sc
        if arr_in[6] != 'None':
            ar_score = ar_score+w_ar_alinar*float(arr_in[6])
            n_norm_ar = n_norm_ar+w_ar_alinar
        if arr_in[7] != 'None':
            ar_score = ar_score+w_ar_trinar*float(arr_in[7])
            n_norm_ar = n_norm_ar+w_ar_trinar
        if arr_in[10] != 'None':
            ar_score = ar_score+w_ar_arm*float(arr_in[10])
            n_norm_ar = n_norm_ar+w_ar_arm
        if n_norm_ar != 0:
            ar_score = ar_score/(n_norm_ar/d_norm_ar)
            ar_score = w_ar*ar_score
            n_norm_all = n_norm_all+w_ar

        if arr_in[4] != 'None':
            ge_score = ge_score+w_ge_sc*float(arr_in[4])
            n_norm_ge = n_norm_ge+w_ge_sc
        if arr_in[11] != 'None':
            ge_score = ge_score+w_ge_gem*float(arr_in[11])
            n_norm_ge = n_norm_ge+w_ge_gem
        if n_norm_ge != 0:
            ge_score = ge_score/(n_norm_ge/d_norm_ge)
            ge_score = w_ge*ge_score
            n_norm_all = n_norm_all+w_ge

        if arr_in[8] != 'None':
            tr_score = tr_score+w_tr_trm*float(arr_in[8])
            n_norm_tr = n_norm_tr+w_tr_trm
        if arr_in[12] != 'None':
            tr_score = tr_score+w_tr_tre*float(arr_in[12])
            n_norm_tr = n_norm_tr+w_tr_tre
        if n_norm_tr != 0:
            tr_score = tr_score/(n_norm_tr/d_norm_tr)
            tr_score = w_tr*tr_score
            n_norm_all = n_norm_all+w_tr

        if n_norm_all == 0:
            outStr = arr_in[0]+'|None'
            f_out.write(outStr + '\n')
            continue
        score = (al_score+ar_score+ge_score+tr_score)/(n_norm_all/d_norm_all)
        outStr = arr_in[0]+'|'+str(score)
        f_out.write(outStr + '\n')

    f_in.close()

if __name__ == '__main__':
    main()
