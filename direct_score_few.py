#!/usr/bin/env python
# coding: utf-8
'''
File Name: direct_score_few.py
Edit Time: 20180417 1624

Content:
    get direct score of track of album, artist
Version:
    1.0
'''

import pdb # debug module
import numpy as np

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_name_test = dataDir + 'testTrack_hierarchy.txt'
    file_name_train = dataDir + 'trainIdx2_matrix.txt'
    output_file = dataDir + 'direct_score_AA.txt'  # direct score of track of 
                                                    # Album, Artist
    fTest = open(file_name_test, 'r')
    fTrain = open(file_name_train, 'r')
    Trainline = fTrain.readline()
    fOut = open(output_file, 'w')

    trackID_vec = [0]*6
    albumID_vec = [0]*6
    artistID_vec = [0]*6
    lastUserID = -1

    for line in fTest:  # find test userID, trackID, albumID
        arr_test = line.strip().split('|')
        userID = arr_test[0]
        trackID = arr_test[1]
        albumID = arr_test[2]
        artistID = arr_test[3]

        if userID != lastUserID:    #change user
            ii = 0
            user_rating_inTrain = np.full((6, 2, ), np.nan)

        trackID_vec[ii] = trackID   # ID for 6 tracks
        albumID_vec[ii] = albumID
        artistID_vec[ii] = artistID
        ii = ii + 1
        lastUserID = userID

        if ii == 6: # when the last track for this user
            while (Trainline):
                arr_train = Trainline.strip().split('|')    # try to find the same info in train
                trainUserID = arr_train[0]
                trainItemID = arr_train[1]
                trainRating = arr_train[2]

                if int(trainUserID) > int(userID):
                    for nn in range(0, 6):
                        outStr = str(userID) + '|' + str(trackID_vec[nn])+ '|' \
                        + str(user_rating_inTrain[nn,0]) + '|' + str(user_rating_inTrain[nn, 1])
                        fOut.write(outStr + '\n')
                    break

                Trainline = fTrain.readline()

#                pdb.set_trace() # debug

                if int(trainUserID) < int(userID):
                    continue
                if trainUserID == userID:   # find same user
                    for nn in range(0, 6):  # get the score
                        if trainItemID == albumID_vec[nn]:  
                            user_rating_inTrain[nn, 0] = trainRating    # score of album
                        if trainItemID == artistID_vec[nn]:
                            user_rating_inTrain[nn, 1] = trainRating    # score of artist
    fTest.close()
    fTrain.close()

if __name__ == '__main__':
    main()
