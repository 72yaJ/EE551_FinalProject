#!/usr/bin/env python
# coding: utf-8
'''
File Name: user_album.py
Edit Time: 20180418 1929

Content:
    get album ID, score for each user from traindata
    userID, albumID, score
    
Version:
    1.0
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_album = dataDir + 'albumData2.txt'
    file_name_train = dataDir + 'trainIdx2_matrix_sorted.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'user_album'+t+'.txt'
    output_file = dataDir + title
    title1 = 'train_noAlbum'+t+'.txt'
    output_file1 = dataDir + title1

    fAlbum = open(file_album, 'r')
    fTrain = open(file_name_train, 'r')
    fOut = open(output_file, 'w')
    fOut1 = open(output_file1, 'w')

    lastUserID = -1

    for line in fTrain:  # find train userID, itemID, score
        arr_train = line.strip().split('|')
            # arr_train[0] trainUserID
            # arr_train[1] trainItemID
            # arr_train[2] trainRating

        userID = arr_train[0]
        
#        pdb.set_trace()

        if userID != lastUserID:
            fAlbum.seek(0)
            albumline = fAlbum.readline()
        lastUserID = userID

#        fAlbum.seek(0)
#        albumline = fAlbum.readline()
        while(albumline):
            arr_album = albumline.strip().split('|')
                # arr_album[0] albumID
                # arr_album[1] artistID
                # arr_album[2:] GenreID
            
#            if arr_album[0]=='28340':
#               pdb.set_trace() #debug

#            if arr_train[1]=='211' and arr_train[0]=='3':

#                pdb.set_trace() #debug

            if arr_album[] > arr_train[1]:
                fOut1.write(line)
                break

            if arr_album[0] == arr_train[1]:

#                pdb.set_trace()    # debug

                fOut.write(line)
                break

#            if int(arr_album[0]) > int(arr_train[1]):
#                pdb.set_trace() # debug
#                break
            albumline = fAlbum.readline()

            if int(arr_album[0]) < int(arr_train[1]):
                continue

    fAlbum.close()
    fTrain.close()

if __name__ == '__main__':
    main()
