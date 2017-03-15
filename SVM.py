#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

#from sklearn import tree # decision trees
#from sklearn import neighbors.KNeighborsClassifier # k-nearest-neighbors
#from sklearn import svm.SVC # support-vector machines
#from sklearn import naive_bayes.GaussianNB # naive bayes classifier
# sklearn has so many more classifiers to test out

def TrainOnData():

	print("Running SVM on test data.")

	N= 15
	most_points = [-1] * N
	most_points_id = ['?'] * N
	
	# loading one of our data files (ie. data0)
	n_popular = 0
	n_fail = 0
	n_oth = 0
	complete_set = []
	for i in range(6):
		dataPoints = pickle.load( open ('data'+str(i)+'.pck', "rb") )
		for D in dataPoints:
			if D['final-score'] > 500:
				n_popular+=1
				print(D['id'])
			else:
				n_fail += 1

			"""
			# score greater than 2000?
			if D['label'] == 'POPULAR':
				n_popular+=1
			else:
				n_fail += 1
			"""
	
	print("S="+str(n_popular)+", F="+str(n_fail)+", O="+str(n_oth))
	print("Complete.")
	
def TestOnData():

	print("Running SVM on test data.")
	print("Complete.")


