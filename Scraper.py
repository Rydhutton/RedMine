#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import praw
import time
from time import gmtime, strftime

# [harrison] we are using the reddit PRAW API
# you can install it simply by typing "pip install praw" into the terminal
# you can see the app details (client_id/secret/etc) if you
#	1) log in to reddit as csc475_user (pass:asdfasdf)
#	2) go to 'preferences'
#	3) click on the 'apps' tab

max_in_sys = 2000
queues = []
interval = 5 #5.0 * 60
n_reevals = 5
n_saved_to_disk = 0

reddit = praw.Reddit(client_id='Er23cgYvVuqPHw', client_secret='uXfAKsBIUQ7JaR6Hy--RxQuF4eo', user_agent='CompSci474Project:v1.0.0 (by /u/csc475_user)')
def StartCollectingData():	
	# [harrison] Initialize threads
	print("\n\n== Starting in data-mine mode [press Ctrl+C to stop] ==")
	for i in range(n_reevals+1): queues.append( [] )
	main_thread = threading.Thread(target=LogNewSubmissions)
	main_thread.daemon = True
	main_thread.start()
	for i in range(n_reevals):
		REv_thread = threading.Thread(target=ReEvaluateSubmission, args=(i,))
		REv_thread.daemon = True
		REv_thread.start()
	#TODO, a thread for saving data to text files
	
	# [harrison] Control loop
	time_elapsed = 0
	while True:
		time_elapsed += 1
		p = ''
		for i in range(n_reevals+1): p = p+str(len(queues[i]))+','
		print('TimeElapsed=['+str(time_elapsed)+'] ProcessingQueues=['+p+'] SavedToDisk=['+str(n_saved_to_disk)+']')
		time.sleep(1)
		
def ReEvaluateSubmission(thread_index):
	# [harrison]
	while(True):
		time.sleep(1.0)
		if (len((queues[thread_index])) != 0):
			t = time.time()
			while(((queues[thread_index])[0])['ts']+(interval*(thread_index+1))<t):
				#TODO op on data
				queues[thread_index+1].append(((queues[thread_index])[0]))
				del queues[thread_index][0]
				if (len((queues[thread_index])) == 0): break
		
def LogNewSubmissions():
	# [harrison] initialize session with PRAW
	subreddits_to_monitor = ['AskReddit', 'funny', 'todayilearned', 'science', 'worldnews', 'pics', 'IAmA', 'gaming', 'videos', 'movies', 'Music', 'aww', 'news', 'gifs', 'explainlikeimfive', 'askscience', 'EarthPorn', 'books', 'television', 'LifeProTips', 'mildlyinteresting', 'DIY', 'Showerthoughts', 'space', 'sports', 'InternetIsBeautiful', 'tifu', 'Jokes', 'history', 'gadgets', 'food', 'nottheonion', 'photoshopbattles', 'Futurology', 'Documentaries', 'personalfinance', 'dataisbeautiful', 'GetMotivated', 'UpliftingNews', 'listentothis']
	cct = ''
	for i in range(len(subreddits_to_monitor)):
		cct = cct+subreddits_to_monitor[i]
		if (i != len(subreddits_to_monitor)-1):
			cct = cct+'+'
	to_stream = reddit.subreddit(cct)
	
	# [harrison] create a new instance for every new/fresh post (this happens several times per second)
	for P in to_stream.stream.submissions():
		u = reddit.redditor(str(P.author))
		d = { }
		d['pid'] = P.id
		d['ts'] = time.time()
		d['CK'] = u.comment_karma
		d['LK'] = u.link_karma
		d['subr'] = str(P.subreddit)
		if (len(queues[0]) < max_in_sys):
			queues[0].append(d)

	
