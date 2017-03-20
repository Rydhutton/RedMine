#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import pickle
import time
from time import gmtime, strftime

def TrainOnData():

	print("Running SVM on test data.")

	# [harrison] preprocessing - string attribute encoders
	subreddits_monitored = ['AskReddit', 'funny', 'todayilearned', 'science', 'worldnews', 'pics', 'IAmA', 'gaming', 'videos', 'movies', 'Music', 'aww', 'news', 'gifs', 'explainlikeimfive', 'askscience', 'EarthPorn', 'books', 'television', 'LifeProTips', 'mildlyinteresting', 'DIY', 'Showerthoughts', 'space', 'sports', 'InternetIsBeautiful', 'tifu', 'Jokes', 'history', 'gadgets', 'food', 'nottheonion', 'photoshopbattles', 'Futurology', 'Documentaries', 'personalfinance', 'dataisbeautiful', 'GetMotivated', 'UpliftingNews', 'listentothis']
	SUBREDDIT_ENCODER = preprocessing.LabelEncoder()
	SUBREDDIT_ENCODER.fit(subreddits_monitored)
	post_types = ['image', 'video', 'text', 'link']
	TYPE_ENCODER = preprocessing.LabelEncoder()
	TYPE_ENCODER.fit(post_types)
	
	# [harrison] transform data into a form usable by sklearn
	raw_data = pickle.load( open ('GIANT_DATA.pck', "rb") )
	inputs = []
	outputs = []
	intervals_to_use = 0 # up to 5
	for D in raw_data:
		arr = []
		arr.append(TYPE_ENCODER.transform(D['type']))
		arr.append(D['comment-karma'])
		arr.append(D['link-karma'])
		arr.append(SUBREDDIT_ENCODER.transform(D['subreddit']))
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
	
	# fit classifier
	#model = linear_model.LogisticRegression()
	model = KNeighborsClassifier(n_neighbors=3)
	
	# calculate accuracy (k-fold)
	average_acc = 0
	k_fold_size = 1000
	n_iters = int( len(inputs) / k_fold_size )
	for i in range(n_iters):	
		t = i*1000
		test_data = inputs[t:t+1000]
		test_labels = outputs[t:t+1000]
		train_data = inputs[0:t].copy() + inputs[t+1000:].copy()
		train_labels = outputs[0:t].copy() + outputs[t+1000:].copy()
		model.fit(train_data, train_labels)
		results = model.predict(test_data)
		accuracy = accuracy_score(test_labels, results)
		average_acc += accuracy
		print(str(i) + "," + str(accuracy))
	average_acc = average_acc / float(n_iters)
	print("TOTAL ACCURACY = "+str(average_acc))
	print("Complete.")
	
def TestOnData():

	print("Running SVM on test data.")
	print("Complete.")


