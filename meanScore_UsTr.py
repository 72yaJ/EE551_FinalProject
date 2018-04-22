#!/usr/bin/env python
# coding: utf-8
'''
File Name: meanScore_UsTr.py
Edit Time: 20180421 1812

Content:
    get mean score of tracks rated by one user
    
Version:
    1.0
'''

import pdb # debug module
from numpy import mean
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in = dataDir + 'user_track.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'di_UsID_trSc_mean'+t+'.txt'
    output_file = dataDir + title

    f_in = open(file_in, 'r')
    f_out = open(output_file, 'w')
 
    line = f_in.readline()
    arr_in = line.strip().split('|')
    lastUserID = arr_in[0]
    buff = [float(arr_in[2])]

    for line in f_in:
        arr_in = line.strip().split('|')
        userID = arr_in[0]

        if lastUserID != userID:
            outStr = str(lastUserID)+'|'+str(mean(buff))+'\n'
            f_out.write(outStr)
            buff = []
        buff.append(float(arr_in[2]))
        lastUserID = userID

    outStr = str(lastUserID)+'|'+str(mean(buff))+'\n'
    f_out.write(outStr)

    f_in.close()

if __name__ == '__main__':
    main()
