#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
from time import gmtime, strftime
import praw

# [harrison] we are using "PRAW" as an API to collect reddit data
# you can install it simply by typing "pip install praw" into the terminal
# you can see the app details (client_id/secret/etc) if you
#	1) log in to reddit as csc475_user (pass:asdfasdf)
#	2) go to 'preferences'
#	3) click on the 'apps' tab

n_data = 0
queue_incomplete = []
queue_complete = []

def StartCollectingData():	

	# [harrison]
	print("\nStarting in data-mine mode [press Ctrl+C to stop].")
	main_thread = threading.Thread(target=LogNewSubmissions)
	main_thread.daemon = True
	main_thread.start()
	
	for i in range(5):
		REv_thread = threading.Thread(target=ReEvaluateSubmission, args=(i,))
		REv_thread.daemon = True
		REv_thread.start()
	
	t = 0
	while True:
		t += 2
		print('Time elapsed : '+str(t))
		time.sleep(2)
	
def ReEvaluateSubmission(thread_index):
	while(True):
		time.sleep(1.0)
		print(thread_index)
	
def LogNewSubmissions():

	# [harrison] initialize session
	reddit = praw.Reddit(client_id='Er23cgYvVuqPHw', client_secret='uXfAKsBIUQ7JaR6Hy--RxQuF4eo', user_agent='CompSci474Project:v1.0.0 (by /u/csc475_user)')
	subreddits_to_monitor = ['AskReddit', 'funny', 'todayilearned', 'science', 'worldnews', 'pics', 'IAmA', 'gaming', 'videos', 'movies', 'Music', 'aww', 'news', 'gifs', 'explainlikeimfive', 'askscience', 'EarthPorn', 'books', 'television', 'LifeProTips', 'mildlyinteresting', 'DIY', 'Showerthoughts', 'space', 'sports', 'InternetIsBeautiful', 'tifu', 'Jokes', 'history', 'gadgets', 'food', 'nottheonion', 'photoshopbattles', 'Futurology', 'Documentaries', 'personalfinance', 'dataisbeautiful', 'GetMotivated', 'UpliftingNews', 'listentothis']
	cct = ''
	for i in range(len(subreddits_to_monitor)):
		cct = cct+subreddits_to_monitor[i]
		if (i != len(subreddits_to_monitor)-1):
			cct = cct+'+'
	to_stream = reddit.subreddit(cct)
	
	# [harrison] create a new instance for every new/fresh post
	for P in to_stream.stream.submissions():
		u = reddit.redditor(str(P.author)) # user
		CK = u.comment_karma
		LK = u.link_karma
		d = { }
		d['pid'] = P.id #book-keeping
		d['ts'] = time.time() #book-keeping & PARAM
		d['CK'] = CK #PARAM
		d['LK'] = LK #PARAM
		d['subr'] = str(P.subreddit)
		queue_incomplete.append(d)
		n_data += 1
		if (n_data = 100000): break
	return
		

	
