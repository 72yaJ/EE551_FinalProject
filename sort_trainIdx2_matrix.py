#!/usr/bin/env python
# coding: utf-8
'''
File Name: sort_trainIdx2_matrix.py
Edit Time: 20180417 2017

Content:
    sort the trainIdx2_matrix from small to large
    add '00|00|00\n' as the last line of the file
    
Version:
    1.0
'''

import pdb # debug module
#from numpy import size
import numpy as np
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_name_train = dataDir + 'trainIdx2_matrix.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'trainIdx2_matrix'+t+'.txt'
    output_file = dataDir + title   # sorted train data

    fTrain = open(file_name_train, 'r')
    fOut = open(output_file, 'w')

    line = fTrain.readline()
    arr_train = line.strip().split('|')
    buff = np.asarray(list(map(int, arr_train)))

    lastUserID = '0'

    for line in fTrain:  # find train userID, itemID, score
        arr_train = line.strip().split('|')
            # arr_train[0] trainUserID
            # arr_train[1] trainItemID
            # arr_train[2] trainRating
        userID = arr_train[0]

#        if line == '40263|149734|90\n':
#            pdb.set_trace() #debug

        if userID != lastUserID:

#            print buff
#            pdb.set_trace() #debug

            buff = buff[np.argsort(buff[:, 1])]
#####            buff.sort(key=lambda x:(x[1])) # sort of list
            y = np.size(buff)/3
            for index in xrange(0, y):
                outStr = str(buff[index][0])+'|'+str(buff[index][1])+'|'+str(buff[index][2])
                fOut.write(outStr + '\n')
            buff = np.asarray(list(map(int, arr_train)))
            lastUserID = userID
            continue

        buff = np.vstack((buff, list(map(int, arr_train))))
        lastUserID = userID

    fTrain.close()

if __name__ == '__main__':
    main()
