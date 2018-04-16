#!/usr/bin/env python
# coding: utf-8
'''
File Name: direct_score.py
Edit Time: 20180415 1056

Content:
    get direct score of track of album, artist and genre
Version:
    1.2
'''

import pdb # debug module
import numpy as np
import copy

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_name_test = dataDir + 'testTrack_hierarchy.txt'
    file_name_train = dataDir + 'trainIdx2_matrix.txt'
    output_file = dataDir + 'direct_score_AAG.txt'  # direct score of track of 
                                                    # Album, Artist and Genre
    fTest = open(file_name_test, 'r')
    fTrain = open(file_name_train, 'r')
    Trainline = fTrain.readline()
    fOut = open(output_file, 'w')

#    trackID_vec = [0]*6
#    albumID_vec = [0]*6
#    artistID_vec = [0]*6
#    genreID_vec = np.array()
#    testID = []
    lastUserID = -1

#    user_rating_inTrain = np.zeros(shape = (6,3))
#    user_rating_inTrain = np.full((6, 2, ), np.nan)

    for line in fTest:  # find test userID, trackID, albumID
        arr_test = line.strip().split('|')

#        pdb.set_trace() # debug


        userID = arr_test[0]
        trackID = arr_test[1]
#        albumID = arr_test[2]
#        artistID = arr_test[3]
#        genreID = arr_test[4:]
#        m = np.size(genreID)   # the number of genres of this track
#        m = np.size(testID[ii])

        if userID != lastUserID:    #change user
            ii = 0
#            genreID_vec = np.full((6, m, ), np.nan)
#            user_rating_inTrain = np.full((6, 2+m, ), np.nan)
#            user_rating_inTrain = np.zeros(shape = (6,3))

#            pdb.set_trace() # debug

            user_rating_inTrain = [[userID]]*6
            testID = []


        testID.append(line.strip().split('|'))
            # testID[ii][0] userID
            # testID[ii][1] trackID
            # testID[ii][2] albumID
            # testID[ii][3] artistID
            # testID[ii][4:] genreID        


#        trackID_vec[ii] = trackID   # ID for 6 tracks
#        albumID_vec[ii] = albumID
#        artistID_vec[ii] = artistID
#        genreID_vec[ii] = np.array.append(genreID)

        ii = ii + 1
        lastUserID = userID

        if ii == 6: # when the last track for this user
#            user_rating_inTrain = copy.deepcopy(testID)
            for y in range(0, 6):

#                pdb.set_trace() # debug
                
                item1 = testID[y][0:2]
                item2 = ['None']*np.size(testID[y][2:])
                item1.extend(item2)
                user_rating_inTrain[y] = item1[:]

#                user_rating_inTrain[y][1] = testID[y][1]
#                user_rating_inTrain[y][2:] = ['None']*np.size(testID[y])


            while (Trainline):



                arr_train = Trainline.strip().split('|')    # try to find the same info in train
                trainUserID = arr_train[0]
                trainItemID = arr_train[1]
                trainRating = arr_train[2]

#                if trainUserID == '10':
#                        pdb.set_trace() # debug #2

                if int(trainUserID) > int(userID):

                    if trainUserID == '10':
                        pdb.set_trace() # debug #2

                    for nn in range(0, 6):
                        outStr = str(userID)+'|'
                        for mm in user_rating_inTrain[nn][1:]:
                            outStr = outStr+str(mm)+'|'

#                        outStr = str(userID) + '|' + str(trackID_vec[nn]) + '|'
#                        for mm in range(0, 2+m):
#                            outStr = outStr + '|' + str(user_rating_inTrain[nn,mm]) + '|'
#                        + str(user_rating_inTrain[nn,0]) + '|' + str(user_rating_inTrain[nn, 1])
                       
                        fOut.write(outStr + '\n')
#                        del user_rating_inTrain

                    if trainUserID == '10':
                        pdb.set_trace() # debug #3

                    break


                Trainline = fTrain.readline()   # to verify?????add or reduce the line

#                pdb.set_trace() # debug

                if int(trainUserID) < int(userID):
                    continue
                if trainUserID == userID:   # find same user

                    if userID=='9' and trainItemID=='274212':
                        pdb.set_trace() # debug #1

                    if userID == '10':
                        pdb.set_trace() # debug #4

#                    user_rating_inTrain = testID[:] # create a copy of testID
#                    user_rating_inTrain = list(testID) # create a copy of testID
#                    user_rating_inTrain = copy.deepcopy(testID) # create a copy of testID

#                    if trainItemID=='141075':
#                    if trainItemID=='161019':
#                        pdb.set_trace() # debug

                    for nn in range(0, 6):

#                        y = [userID]
#                        y.append(testID[nn][1])
#                        user_rating_inTrain[nn] = y
#                        user_rating_inTrain[nn].append(testID[nn][1])   # trackID
                        if trainItemID == testID[nn][2]:    # albumID

                            user_rating_inTrain[nn][2] = trainRating
#                        else:
#                            user_rating_inTrain[nn][2] = 'None'
                        if trainItemID == testID[nn][3]:    # artistID
                            user_rating_inTrain[nn][3] = trainRating

#                        else:
#                            user_rating_inTrain[nn][3] = 'None'

                        y = np.size(testID[nn][3:])
                        for mm in range(0, y-1):
#                        for index, mm in enumerate(testID[nn][4:]):

#                            pdb.set_trace() # debug

                            if trainItemID == testID[nn][mm]:
#                            if trainItemID == mm:
                                user_rating_inTrain[nn][4+mm] = trainRating
#                                user_rating_inTrain[nn][4+index] = trainRating
#                            else:
#                                user_rating_inTrain[nn][4+mm] = 'None'
#                                user_rating_inTrain[nn][4+index] = 'None'

#                        if nn==5 and userID =='9':
#                            pdb.set_trace() # debug


#                    for nn in range(0, 6):  # get the score
#                        if trainItemID == albumID_vec[nn]:  
#                            user_rating_inTrain[nn, 0] = trainRating    # score of album
#                        if trainItemID == artistID_vec[nn]:
#                            user_rating_inTrain[nn, 1] = trainRating    # score of artist
#                        for mm in range(0, m):
#                            if trainItemID == genreID_vec[nn, mm]:
#                                user_rating_inTrain[nn, 2+mm] = trainRating


    fTest.close()
    fTrain.close()

if __name__ == '__main__':
    main()
