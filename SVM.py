#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import praw
import pickle
import time
from time import gmtime, strftime

def TrainOnData():

	print("Running SVM on test data.")

	# loading one of our data files (ie. data0)
	data = pickle.load( open ('GIANT_DATA.pck', "rb") )
	n = 0
	for D in data:
		#print(D['final-score'])
		if (D['final-score'] > 700):
			n += 1
	print(n)

	print("Complete.")
	
def TestOnData():

	print("Running SVM on test data.")
	print("Complete.")


