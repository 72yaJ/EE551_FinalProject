#!/usr/bin/env python
# coding: utf-8
'''
File Name: direct_score.py
Edit Time: 20180417 1545

Content:
    get direct score of track of album, artist and genre
Version:
    1.4
'''

#import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_name_test = dataDir + 'testTrack_hierarchy.txt'
    file_name_train = dataDir + 'trainIdx2_matrix.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'direct_score_AAG'+t+'.txt'
    output_file = dataDir + title   # direct score of track of 
                                    # Album, Artist and Genre
    fTest = open(file_name_test, 'r')
    fTrain = open(file_name_train, 'r')
    Trainline = fTrain.readline()
    fOut = open(output_file, 'w')

    lastUserID = -1

    for line in fTest:  # find test userID, trackID, albumID
        arr_test = line.strip().split('|')

        userID = arr_test[0]
        trackID = arr_test[1]

        if userID != lastUserID:    #change user
            ii = 0
            user_rating_inTrain = [list([]) for i in xrange(6)]
            testID = []

        testID.append(line.strip().split('|'))
            # testID[ii][0] userID
            # testID[ii][1] trackID
            # testID[ii][2] albumID
            # testID[ii][3] artistID
            # testID[ii][4:] genreID        

        ii = ii + 1
        lastUserID = userID

        if ii == 6: # when the last track for this user
            for y in xrange(0, 6):
                user_rating_inTrain[y][:] = ['None']*size(testID[y])
                user_rating_inTrain[y][0:2] = testID[y][0:2]
                    # user_rating_inTrain[y][0] userID
                    # user_rating_inTrain[y][1] trackID
                    # user_rating_inTrain[y][2] album_score
                    # user_rating_inTrain[y][3] artist_score
                    # user_rating_inTrain[y][4:] genre_score

            while (Trainline):
                arr_train = Trainline.strip().split('|')    # try to find the same info in train
                trainUserID = arr_train[0]
                trainItemID = arr_train[1]
                trainRating = arr_train[2]

                if int(trainUserID) > int(userID):
                    for nn in xrange(0, 6):
                        outStr = str(userID)+'|'
                        for mm in user_rating_inTrain[nn][1:]:
                            outStr = outStr+str(mm)+'|'
                        fOut.write(outStr + '\n')

#                        pdb.set_trace() # debug #3

                    break

                Trainline = fTrain.readline()

                if int(trainUserID) < int(userID):
                    continue
                if trainUserID == userID:   # find same user
                    for nn in xrange(0, 6):
                        y = size(testID[nn][2:])
                        for mm in xrange(0, y):
#                        for mm in xrange(0, y-1):
                            if trainItemID == testID[nn][2+mm]:
                                user_rating_inTrain[nn][2+mm] = trainRating

    fTest.close()
    fTrain.close()

if __name__ == '__main__':
    main()
