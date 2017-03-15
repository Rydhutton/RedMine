#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [harrison] use 'sklearn' for this part

import pickle

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


