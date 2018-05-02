#!/usr/bin/env python
# coding: utf-8
'''
File Name: matrix_fctorize_spark.py
Edit Time: 20180501 1819

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
    data = sc.textFile('/home/z/Documents/python/EE627_HW8/re_u.data')

    pdata = sc.parallelize(data.take(100000))
    ratings = pdata.map(lambda l: l.split(','))\
            .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))\

#    pdb.set_trace()

    sc.setCheckpointDir('target') # need to add this!!!

    rank = 20
    numIter = 30
    model = ALS.train(ratings, rank, numIter)   
    testdata = ratings.map(lambda p: (p[0], p[1]))
    predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
    ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
    MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
    print("Mean Squared Error = " + str(MSE))

if __name__ == '__main__':
    main()
