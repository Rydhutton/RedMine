#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import time
from time import gmtime, strftime

def TrainOnData():

	print("Running SVM on test data.")

	# [harrison] transform data into a form usable by sklearn
	raw_data = pickle.load( open ('GIANT_DATA.pck', "rb") )
	inputs = []
	outputs = []
	intervals_to_use = 3 # can use up to 5
	for D in raw_data:
		arr = []
		arr.append(D['type'])
		arr.append(D['comment-karma'])
		arr.append(D['link-karma'])
		arr.append(D['subreddit'])
		arr.append(time.gmtime(D['time-posted']).tm_hour)
		arr.append(D['num_words'])
		for X in range(intervals_to_use):
			pr = 't'+str(X)+'-'
			arr.append(D[pr+'comments'])
			arr.append(D[pr+'upvoteratio'])
			arr.append(D[pr+'upvotes'])
			arr.append(D[pr+'downvotes'])
			arr.append(D[pr+'num_gold'])
			arr.append(D[pr+'score'])
		inputs.append(arr)
		if (D['final-score'] > 700):
			outputs.append("popular") #popular post
		else:
			outputs.append("not popular") #unpopular post

	print("Complete.")
	
def TestOnData():

	print("Running SVM on test data.")
	print("Complete.")


