#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import tree

from sklearn.ensemble import RandomForestClassifier

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import pickle
import time
from time import gmtime, strftime

def TrainOnData():

	print("\nRunning SVM on test data.")

	# [harrison] config
	normalize = False
	intervals_to_use = 0 # up to 6
	remove_noise = 19500
	k_fold_size = 10
	
	#model = linear_model.LogisticRegression()
	#model = GaussianNB()
	#model = KNeighborsClassifier(n_neighbors=10)
	model = RandomForestClassifier(max_depth = 4)
	
	# [harrison] preprocessing - string attribute encoders
	subreddits_monitored = ['AskReddit', 'funny', 'todayilearned', 'science', 'worldnews', 'pics', 'IAmA', 'gaming', 'videos', 'movies', 'Music', 'aww', 'news', 'gifs', 'explainlikeimfive', 'askscience', 'EarthPorn', 'books', 'television', 'LifeProTips', 'mildlyinteresting', 'DIY', 'Showerthoughts', 'space', 'sports', 'InternetIsBeautiful', 'tifu', 'Jokes', 'history', 'gadgets', 'food', 'nottheonion', 'photoshopbattles', 'Futurology', 'Documentaries', 'personalfinance', 'dataisbeautiful', 'GetMotivated', 'UpliftingNews', 'listentothis']
	SUBREDDIT_ENCODER = preprocessing.LabelEncoder()
	SUBREDDIT_ENCODER.fit(subreddits_monitored)
	post_types = ['image', 'video', 'text', 'link']
	TYPE_ENCODER = preprocessing.LabelEncoder()
	TYPE_ENCODER.fit(post_types)
	raw_data = pickle.load( open ('GIANT_DATA.pck', "rb") )
	
	# [harrison] preprocessing - calculate maxes for normalization
	max_statics = [1.0] * 3
	max_T = [1.0] * intervals_to_use * 5
	if (normalize):
		for D in raw_data:
			if (D['comment-karma'] > max_statics[0]):
				max_statics[0] = float(D['comment-karma'])
			if (D['link-karma'] > max_statics[1]):
				max_statics[1] = float(D['link-karma'])
			if (D['num_words'] > max_statics[2]):
				max_statics[2] = float(D['num_words'])
			for i in range(intervals_to_use):
				offset = (5*i)
				pr = 't'+str(i)+'-'
				if (D[pr+'comments'] > max_T[0+offset]):
					max_T[0+offset] = D[pr+'comments']
				if (D[pr+'upvotes'] > max_T[1+offset]):
					max_T[1+offset] = D[pr+'upvotes']
				if (D[pr+'downvotes'] > max_T[2+offset]):
					max_T[2+offset] = D[pr+'downvotes']
				if (D[pr+'num_gold'] > max_T[3+offset]):
					max_T[3+offset] = D[pr+'num_gold']
				if (D[pr+'score'] > max_T[4+offset]):
					max_T[4+offset] = D[pr+'score']
	
	# [harrison] transform data into a form usable by sklearn
	inputs = []
	outputs = []
	for D in raw_data:
	
		if (D['final-score'] > 700):
			outputs.append("popular") #popular post
		else:
			if (remove_noise > 0):
				remove_noise -= 1
				continue
			else:
				outputs.append("not popular") #unpopular post
	
		arr = []
		arr.append(TYPE_ENCODER.transform(D['type']))
		arr.append(SUBREDDIT_ENCODER.transform(D['subreddit']))
		if (normalize):
			arr.append(D['comment-karma']/max_statics[0])
			arr.append(D['link-karma']/max_statics[1])
			arr.append(time.gmtime(D['time-posted']).tm_hour/24)
			arr.append(D['num_words']/max_statics[2])
		else:
			arr.append(D['comment-karma'])
			arr.append(D['link-karma'])
			arr.append(time.gmtime(D['time-posted']).tm_hour)
			arr.append(D['num_words'])
		
		for X in range(intervals_to_use):
			pr = 't'+str(X)+'-'
			offset = 5*X
			arr.append(D[pr+'upvoteratio'])
			if (normalize):
				arr.append(D[pr+'comments']/max_T[0+offset])
				arr.append(D[pr+'upvotes']/max_T[1+offset])
				arr.append(D[pr+'downvotes']/max_T[2+offset])
				arr.append(D[pr+'num_gold']/max_T[3+offset])
				arr.append(D[pr+'score']/max_T[4+offset])
			else:
				arr.append(D[pr+'comments'])
				arr.append(D[pr+'upvotes'])
				arr.append(D[pr+'downvotes'])
				arr.append(D[pr+'num_gold'])
				arr.append(D[pr+'score'])
		inputs.append(arr)
		
	# [harrison] calculate accuracy (k-fold cross validation)
	average_acc = 0
	n_iters = int( len(inputs) / k_fold_size )
	for i in range(n_iters):	
		t = i*k_fold_size
		test_data = inputs[t:t+k_fold_size]
		test_labels = outputs[t:t+k_fold_size]
		train_data = inputs[0:t].copy() + inputs[t+k_fold_size:].copy()
		train_labels = outputs[0:t].copy() + outputs[t+k_fold_size:].copy()
		model.fit(train_data, train_labels)
		results = model.predict(test_data)
		accuracy = accuracy_score(test_labels, results)
		average_acc += accuracy
		print('fold' + str(i) + "," + str(accuracy))
	average_acc = average_acc / float(n_iters)
	print("TOTAL ACCURACY = "+str(average_acc))
	print("Complete.")


