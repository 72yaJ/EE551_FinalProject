#!/usr/bin/env python
# coding: utf-8
'''
File Name: matrix_factorization.py
Edit Time: 20180508 1106

Content:
    factorize the matrix by spark
    
Version:
    1.0
'''

import pdb # debug module
import numpy as np
from time import gmtime, strftime
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import SparkContext
import matplotlib.pyplot as plt

def main():

    sc = SparkContext()
    dataDir = '/home/z/Documents/python/EE627_project/data/data_in_matrixForm/'
    matrix_in_name = dataDir + 'user_track.txt'
    test_name = dataDir + 'testTrack_hierarchy.txt'
    t = strftime('%Y%m%d%H%M', gmtime())
    title = 'mf_track_estimated'+t+'.txt'
    output_file = dataDir + title
    f_out = open(output_file, 'w')

    data = sc.textFile(matrix_in_name)
    ratings = data.map(lambda l: l.split('|'))\
            .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))

    sc.setCheckpointDir('target') # need to add this!!!

    rank = 150
    numIter = 30

    model = ALS.train(ratings, rank, numIter) 
    # Save and load model
    model.save(sc, "target/tmp/album_rank150num30")
#    model = MatrixFactorizationModel.load(sc, "target/tmp/album_rank150num30")
        # rank30, numIter30: MSE150 "target/tmp/myCollaborativeFilter"
        # rank50, numIter30: MSE79.7 "target/tmp/rank50num30"
        # rank70, numIter30: MSE43.5 "target/tmp/rank70num30"
        # rank100, numIter30: MSE17.5 "target/tmp/rank100num30"
        # rank100, numIter30: MSE7.6 "target/tmp/album_rank100num30"
        # rank120, numIter30: MSE3.2 "target/tmp/album_rank120num30"
        # rank150, numIter30: MSE1.1 "target/tmp/album_rank150num30"

#    testdata = ratings.map(lambda p: (p[0], p[1]))
#    predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
#    ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
#    MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
#    print("Mean Squared Error = " + str(MSE))

#    testdata = sc.textFile(test_name)
#    testRating = testdata.map(lambda l: l.split('|'))
####            .map(lambda l: Rating(int(l[0]), int(l[1]), float(0)))
#    test = testRating.map(lambda p: (p[0], p[1])) # for track
#    print test.count()
#    predictions = model.predictAll(test).map(lambda r: (r[0], r[1], r[2]))
#    print predictions.count()
####    ratesAndPreds = testRating.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)

####    pre = ratesAndPreds.map(lambda x: x).collect()
#    pre = predictions.map(lambda x: x).collect()
#    pre.sort(key = lambda x:(x[0]))

#    pdb.set_trace()

#    for item in pre:
#        outStr = str(int(item[0]))+'|'+str(int(item[1]))+'|'+str(float(item[2]))+'\n'
#        f_out.write(outStr)

if __name__ == '__main__':
    main()
