#!/usr/bin/env python
# coding: utf-8
'''
File Name: response_score.py
Edit Time: 20180418 1508

Content:
    get direct score of response from traindata
    
Version:
    1.0
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_name_test = dataDir + 'responseID.txt'
    file_name_train = dataDir + 'trainIdx2_matrix_sorted.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'response_score'+t+'.txt'
    output_file = dataDir + title

    fTest = open(file_name_test, 'r')
    fTrain = open(file_name_train, 'r')
    Trainline = fTrain.readline()
    fOut = open(output_file, 'w')

    line = fTest.readline()
    arr_test = line.strip().split('|')
    lastUserID = arr_test[0]
    ii = 1
    user_rating_inTrain = [[]]
    testID = []
    testID.append(line.strip().split('|'))

    for line in fTest:  # find test userID, trackID, albumID
        arr_test = line.strip().split('|')

        userID = arr_test[0]
#        trackID = arr_test[1]

#        pdb.set_trace() # debug

        if userID != lastUserID:    #change user
            num = ii
            user_rating_inTrain = [list([]) for i in xrange(num)]

#            pdb.set_trace()

            for y in xrange(0, num):
                user_rating_inTrain[y][:] = ['None']*size(testID[y])
                user_rating_inTrain[y][0] = testID[y][0]
                    # user_rating_inTrain[y][0] userID
                    # user_rating_inTrain[y][1] track_score
                    # user_rating_inTrain[y][2] album_score
                    # user_rating_inTrain[y][3] artist_score
                    # user_rating_inTrain[y][4:] genre_score

            while (Trainline):
                arr_train = Trainline.strip().split('|')    # try to find the same info in train
                trainUserID = arr_train[0]
                trainItemID = arr_train[1]
                trainRating = arr_train[2]

                if int(trainUserID) > int(lastUserID):
                    for nn in xrange(0, num):
                        outStr = str(lastUserID)+'|'
                        for mm in user_rating_inTrain[nn][1:]:
                            outStr = outStr+str(mm)+'|'
                        fOut.write(outStr + '\n')
                    break

                Trainline = fTrain.readline()

                if int(trainUserID) < int(lastUserID):
                    continue
                if trainUserID == lastUserID:   # find same user
                    for nn in xrange(0, num):
                        y = size(testID[nn][1:])
                        for mm in xrange(0, y):
                            if trainItemID == testID[nn][1+mm]:
                                user_rating_inTrain[nn][1+mm] = trainRating
            ii = 0
            testID = []

        testID.append(line.strip().split('|'))
            # testID[ii][0] userID
            # testID[ii][1] trackID
            # testID[ii][2] albumID
            # testID[ii][3] artistID
            # testID[ii][4:] genreID        

        ii = ii + 1
        lastUserID = userID

    while (Trainline):
        arr_train = Trainline.strip().split('|')    # try to find the same info in train
        trainUserID = arr_train[0]
        trainItemID = arr_train[1]
        trainRating = arr_train[2]

        if int(trainUserID) > int(lastUserID):
            for nn in xrange(0, num):
                outStr = str(lastUserID)+'|'
                for mm in user_rating_inTrain[nn][1:]:
                    outStr = outStr+str(mm)+'|'
                fOut.write(outStr + '\n')
            break

        Trainline = fTrain.readline()

        if int(trainUserID) < int(lastUserID):
            continue
        if trainUserID == lastUserID:   # find same user
            for nn in xrange(0, num):
                y = size(testID[nn][1:])
                for mm in xrange(0, y):
                    if trainItemID == testID[nn][1+mm]:
                        user_rating_inTrain[nn][1+mm] = trainRating



    fTest.close()
    fTrain.close()

if __name__ == '__main__':
    main()
