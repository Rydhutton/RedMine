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

queue_incomplete = []
queue_complete = []

def StartCollectingData():	

	print("\nStarting in data-mine mode [press Ctrl+C to stop].")
	
	# [harrison] initialize session
	reddit = praw.Reddit(client_id='Er23cgYvVuqPHw', client_secret='uXfAKsBIUQ7JaR6Hy--RxQuF4eo', user_agent='CompSci474Project:v1.0.0 (by /u/csc475_user)')
	subreddits_to_monitor = ['AskReddit', 'funny', 'todayilearned', 'science', 'worldnews', 'pics', 'IAmA', 'gaming', 'videos', 'movies', 'Music', 'aww', 'news', 'gifs', 'explainlikeimfive', 'askscience', 'EarthPorn', 'books', 'television', 'LifeProTips', 'mildlyinteresting', 'DIY', 'Showerthoughts', 'space', 'sports', 'InternetIsBeautiful', 'tifu', 'Jokes', 'history', 'gadgets', 'food', 'nottheonion', 'photoshopbattles', 'Futurology', 'Documentaries', 'personalfinance', 'dataisbeautiful', 'GetMotivated', 'UpliftingNews', 'listentothis']
	cct = ''
	for i in range(len(subreddits_to_monitor)):
		cct = cct+subreddits_to_monitor[i]
		if (i != len(subreddits_to_monitor)-1):
			cct = cct+'+'
	to_stream = reddit.subreddit(cct)
		
	for P in to_stream.stream.submissions():
		
		# [harrison] create new instance for new post, put in incomplete_queue
		d = { }
		d['timestamp'] = time.time()
		d['pid'] = P.id
		queue_incomplete.append(d)
		
		# [harrison] check if old data needs to be updated
		
		
		# [harrison] debug
		print('\n'+str((P.title).encode('utf-8'))+' [id='+P.id+']')
		print(P.subreddit)
		print(time.ctime(time.time()))
		print('queue lenghts = ['+str(len(queue_incomplete))+','+str(len(queue_complete))+']\n')
