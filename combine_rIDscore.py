#!/usr/bin/env python
# coding: utf-8
'''
File Name: combine_rIDscore.py
Edit Time: 20180418 1744

Content:
    combine ID and score of response from traindata
    
Version:
    1.0
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_r_ID = dataDir + 'responseID.txt'
    file_r_score = dataDir + 'response_score.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'response_IDscore'+t+'.txt'
    output_file = dataDir + title

    fID = open(file_r_ID, 'r')
    fscore = open(file_r_score, 'r')
    fOut = open(output_file, 'w')

    for line in fID:
        buff_ID = line.strip().split('|')
        s_line = fscore.readline()
        buff_score = s_line.strip().split('|')

#        pdb.set_trace()

        y = size(buff_ID[:])
        outStr = str(buff_ID[0])+'|'
        for i in xrange(1,y):
            outStr = outStr+str(buff_ID[i])+'|'+str(buff_score[i])+'|'
        fOut.write(outStr + '\n')
    fID.close()
    fscore.close()

if __name__ == '__main__':
    main()
