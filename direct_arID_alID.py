#!/usr/bin/env python
# coding: utf-8
'''
File Name: direct_arID_alID.py
Edit Time: 20180421 1943

Content:
    get the list of user artistID contains which albums
    out:
    usrID artistID albumID ...

    func:
    user_ID1_contain_ID2(file_in1, file_in2, num1, num2, output)
    userID, file_in1 contains file_in2
    num1 is the position of ID1 in file_in1
    num2 is the position of ID1 in file_in2


Version:
    1.0
'''

import pdb # debug module
from numpy import size
from time import gmtime, strftime

def user_ID_contain_ID(file_in1, file_in2, num1, num2, output_file):
    f_in1 = open(file_in1, 'r')
    f_in2 = open(file_in2, 'r')
    f_out = open(output_file, 'w')

    for line1 in f_in1:
        buff1 = line1.strip().split('|')
        if buff1[num1] == 'None':
            outStr = str(buff1[0])+'|None\n'
            f_out.write(outStr)
            continue
        for line2 in f_in2:
            buff2 = line2.strip().split('|')
            if buff2[num2] == buff1[num1]:

#                if buff1[0] == '39':
#                    pdb.set_trace()

                outStr = str(buff1[0])+'|'+line2
                f_out.write(outStr)
                f_in2.seek(0)
                break
            if int(buff2[num2]) > int(buff1[num1]):
                outStr = str(buff1[0])+'|None\n'
                f_out.write(outStr)
                f_in2.seek(0)
                break


    f_in1.close()
    f_in2.close()

def main():
    
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    file_in1 = dataDir + 'testTrack_hierarchy.txt'
    file_in2 = dataDir + 'artistID_albumID.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'di_arID_alID'+t+'.txt'
    output_file = dataDir + title
    num1 = 3 # position of artistID in testTrack.txt
    num2 = 0 # position of artistID in artistID_albumID.txt

    user_ID_contain_ID(file_in1, file_in2, num1, num2, output_file)





if __name__ == '__main__':
    main()
