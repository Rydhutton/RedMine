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
	print("Complete.")

	# loading one of our data files (ie. data0)
	dataPoints = pickle.load( open ('data0.pck', "rb") )
	for D in dataPoints:
		print(D)
	
	print("Complete.")
	
def TestOnData():

	print("Running SVM on test data.")
	print("Complete.")


