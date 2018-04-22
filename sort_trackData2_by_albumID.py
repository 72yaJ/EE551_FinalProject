#!/usr/bin/env python
# coding: utf-8
'''
File Name: sort_trackData2_by_albumID.py
Edit Time: 20180420 1834

Content:
    sort the trackData2.txt from small to large by albumID, row1
    and generate album containing which tracks
    albumID, trackID

    func:
    sort_matrix_by_row(file_in, row_num)
        sort the file from small to large by extract row
        file_in: the file to sort
        row_num: which row to sort by

Version:
    1.0
'''

import pdb # debug module
#from numpy import size
#import numpy as np
from time import gmtime, strftime

def sort_matrix_by_row(file_in, row_num):

    f_in = open(file_in, 'r')

    line = f_in.readline()
    arr_in = line.strip().split('|')
    if arr_in[row_num] != 'None':
        arr_in[row_num] = int(arr_in[row_num])    # change albumID to int to sort
    buff = [arr_in]

    for line in f_in:
        arr_in = line.strip().split('|')
        if arr_in[row_num] != 'None':
            arr_in[row_num] = int(arr_in[row_num])    # change albumID to int to sort
        buff.append(arr_in)
    f_in.close()
    buff.sort(key=lambda x:(x[row_num])) # sort of list
    return buff

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in = dataDir + 'trackData2.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'albumID_trackID'+t+'.txt'
    output_file = dataDir + title   # sorted track data
    fOut = open(output_file, 'w')
    row_num = 1 # albumID is in row 1

    sort_list = sort_matrix_by_row(file_in, row_num)

    lastID = -1
    y = len(sort_list)
    outStr = []
    for ii in xrange(0, y):

#        pdb.set_trace()

        nowID = sort_list[ii][row_num]
        if nowID == 'None':
            break
        if lastID != nowID:
            if ii != 0:
                fOut.write(outStr+'\n')
            outStr = str(sort_list[ii][row_num])+'|'+str(sort_list[ii][0])
            lastID = nowID
            continue
        outStr = outStr+'|'+str(sort_list[ii][0])
        lastID = nowID
    fOut.write(outStr+'\n')

if __name__ == '__main__':
    main()
