#!/usr/bin/env python
# coding: utf-8
'''
File Name: train_dataID.py
Edit Time: 20180417 1644

Content:
    get training data ID for response
    userID, trackID, albumID, artistID, genreID
    
Version:
    1.0
'''

#import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_name_track = dataDir + 'trackData2.txt'
    file_name_train = dataDir + 'trainIdx2_matrix.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'trainingDataID'+t+'.txt'
    output_file = dataDir + title   # direct score of track of 
                                    # Album, Artist and Genre
    fTrack = open(file_name_track, 'r')
    fTrain = open(file_name_train, 'r')
#    Trackline = fTrack.readline()
    fOut = open(output_file, 'w')

    lastTrackID = 0

    for line in fTrain:  # find train userID, itemID, score
        arr_train = line.strip().split('|')
            # arr_train[0] trainUserID
            # arr_train[1] trainItemID
            # arr_train[2] trainRating

#        trainUserID = arr_train[0]  # change to arr_ !!!!!
#        trainItemID = arr_train[1]
#        trainRating = arr_train[2]
        
        fTrack.seek(0)
        Trackline = fTrack.readline()
        while(Trackline):
            arr_track = Trackline.strip().split('|')
                # arr_track[0] trackID
                # arr_track[1] traclAlbumID
                # arr_track[2] trackArtistID
                # arr_track[3:] trackGenreID

#            if arr_track[0] == trainItemID:
            if arr_track[0] == arr_train[1]:
                outStr = str(arr_train[0])+'|'

                y = size(arr_track[:])
                for mm in xrange(0,y):
                    outStr = outStr+arr_track[mm]+'|'
                        
                fOut.write(outStr + '\n')

    fTrack.close()
    fTrain.close()

if __name__ == '__main__':
    main()
