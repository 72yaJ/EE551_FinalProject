#!/usr/bin/env python
# coding: utf-8
'''
File Name: sort_trackData2_album_by_artistID.py
Edit Time: 20180421 1906

Content:
    sort the trackData2.txt from small to large by artistID, row2
    and generate artist containing which albums
    artistID, albumID

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
    title = 'artistID_albumID_in_trackData2'+t+'.txt'
    output_file = dataDir + title   # sorted track data
    fOut = open(output_file, 'w')
    row_num = 2 # artistID is in row 2

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
            outStr = str(sort_list[ii][row_num])+'|'+str(sort_list[ii][1])
                # sort_list[ii][0] trackID
                # sort_list[ii][1] albumID
		# sort_list[ii][2] artistID
                # sort_list[ii][3:] genreID
            lastID = nowID
            continue
        outStr = outStr+'|'+str(sort_list[ii][1])
        lastID = nowID
    fOut.write(outStr+'\n')

if __name__ == '__main__':
    main()
