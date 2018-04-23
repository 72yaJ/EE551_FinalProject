#!/usr/bin/env python
# coding: utf-8
'''
File Name: direct_arID_trSc.py
Edit Time: 20180422 1926

Content:
    match the trackID in di_arID_trID to score from user_track

    func:
    match_ID_score(file_ID, file_score, file_out)
    change the ID in file_in1 to score in file_in2
    num1 
    
Version:
    1.0
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def match_ID_score(file_ID, file_score, file_out):

    f_ID = open(file_ID, 'r')
    f_score = open(file_score, 'r')
    score_line = f_score.readline()
    f_out = open(file_out, 'w')

    ID_line = f_ID.readline()
    arr_ID = ID_line.strip().split('|')
        # arr_ID[0] userID
        # arr_ID[1] albumID
        # arr_ID[2:] trackID

    lastUserID = arr_ID[0]
    ii = 1
    buff_score = [[]]
        # buff_score[y][0] userID
        # buff_score[y][1] item_ID
        # buff_score[y][2:] item_score
    buff_ID = []
    buff_ID.append(ID_line.strip().split('|'))
        # buff_ID[ii][0] userID
        # buff_ID[ii][1] albumID
        # buff_ID[ii][2:] trackID

    for ID_line in f_ID:  # find userID, albumID,  trackID
        arr_ID = ID_line.strip().split('|')
        userID = arr_ID[0]

        if userID != lastUserID:    #change user
            num = ii
            buff_score = [list([]) for i in xrange(num)]

#            pdb.set_trace()

            for y in xrange(0, num):
                buff_score[y][:] = ['None']*size(buff_ID[y])
                buff_score[y][0] = buff_ID[y][0]
                buff_score[y][1] = buff_ID[y][1]

            while (score_line):
                arr_score = score_line.strip().split('|')
                trainUserID = arr_score[0]
                trainItemID = arr_score[1]
                trainRating = arr_score[2]

                if int(trainUserID) > int(lastUserID):
                    for nn in xrange(0, num):
                        outStr = str(lastUserID)
                        for mm in buff_score[nn][1:]:
                            outStr = outStr+'|'+str(mm)
                        f_out.write(outStr + '\n')
                    break

                score_line = f_score.readline()

                if int(trainUserID) < int(lastUserID):
                    continue
                if trainUserID == lastUserID:   # find same user

#                    pdb.set_trace()

                    for nn in xrange(0, num):
                        y = size(buff_ID[nn][:])
                        for mm in xrange(2, y):
                            if trainItemID == buff_ID[nn][mm]:
                                buff_score[nn][mm] = trainRating
            ii = 0
            buff_ID = []

        buff_ID.append(ID_line.strip().split('|'))
        ii = ii + 1
        lastUserID = userID

    num = ii
    buff_score = [list([]) for i in xrange(num)]

#            pdb.set_trace()

    for y in xrange(0, num):
        buff_score[y][:] = ['None']*size(buff_ID[y])
        buff_score[y][0] = buff_ID[y][0]
        buff_score[y][1] = buff_ID[y][1]
    while (score_line):
        arr_score = score_line.strip().split('|')
        trainUserID = arr_score[0]
        trainItemID = arr_score[1]
        trainRating = arr_score[2]

        if int(trainUserID) > int(lastUserID):
            for nn in xrange(0, num):
                outStr = str(lastUserID)
                for mm in buff_score[nn][1:]:
                    outStr = outStr+'|'+str(mm)
                f_out.write(outStr + '\n')
            break

        score_line = f_score.readline()

        if int(trainUserID) < int(lastUserID):
            continue
        if trainUserID == lastUserID:   # find same user
            for nn in xrange(0, num):
                y = size(buff_ID[nn][:])
                for mm in xrange(2, y):
                    if trainItemID == buff_ID[nn][mm]:
                        buff_score[nn][mm] = trainRating

    f_ID.close()
    f_score.close()

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_ID = dataDir + 'di_arID_trID.txt'
    file_score = dataDir + 'user_track.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'di_arID_trSc'+t+'.txt'
    file_out = dataDir + title

    match_ID_score(file_ID, file_score, file_out)

if __name__ == '__main__':
    main()
