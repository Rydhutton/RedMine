#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import praw
import pickle
import time
from time import gmtime, strftime

#from sklearn import tree # decision trees
#from sklearn import neighbors.KNeighborsClassifier # k-nearest-neighbors
#from sklearn import svm.SVC # support-vector machines
#from sklearn import naive_bayes.GaussianNB # naive bayes classifier
# sklearn has so many more classifiers to test out

reddit = praw.Reddit(client_id='03NILBqkPQPvsA', client_secret='RzIoDVk16sUdHv7wJqQjcjN7-o8', user_agent='CompSci474Project2:v1.0.1 (by /u/csc475_user2)')
def TrainOnData():

	print("Running SVM on test data.")

	N= 15
	most_points = [-1] * N
	most_points_id = ['?'] * N
	
	# loading one of our data files (ie. data0)
	n_popular = 0
	n_fail = 0
	n_oth = 0
	data = pickle.load( open ('GIANT_DATA.pck', "rb") )
	for D in data:
		print(D['final-score'])
	print("Complete.")
	
def TestOnData():

	print("Running SVM on test data.")
	print("Complete.")


