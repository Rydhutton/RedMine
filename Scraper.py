#!/usr/bin/env python
# -*- coding: utf-8 -*-

import queue
import time
from time import gmtime, strftime
import praw

# [harrison] we are using "PRAW" as an API to collect reddit data
# you can install it simply by typing "pip install praw" into the terminal
# you can see the app details (client_id/secret/etc) if you
#	1) log in to reddit as csc475_user (pass:asdfasdf)
#	2) go to 'preferences'
#	3) click on the 'apps' tab

def StartCollectingData():	
	
	# harrison is working on this as we speak
	# please do not touch lol
	
	print("Starting in data-mine mode [press Ctrl+C to stop].")
	reddit = praw.Reddit(client_id='Er23cgYvVuqPHw', client_secret='uXfAKsBIUQ7JaR6Hy--RxQuF4eo', user_agent='CompSci474Project:v1.0.0 (by /u/csc475_user)')
	subreddits_to_monitor = ['AskReddit', 'funny', 'todayilearned', 'science', 'worldnews', 'pics', 'IAmA', 'gaming', 'videos', 'movies', 'Music', 'aww', 'news', 'gifs', 'explainlikeimfive', 'askscience', 'EarthPorn', 'books', 'television', 'LifeProTips', 'mildlyinteresting', 'DIY', 'Showerthoughts', 'space', 'sports', 'InternetIsBeautiful', 'tifu', 'Jokes', 'history', 'gadgets', 'food', 'nottheonion', 'photoshopbattles', 'Futurology', 'Documentaries', 'personalfinance', 'dataisbeautiful', 'GetMotivated', 'UpliftingNews', 'listentothis']
	all_subreddits = ''
	for i in range(len(subreddits_to_monitor)):
		all_subreddits = all_subreddits+subreddits_to_monitor[i]
		if (i != len(subreddits_to_monitor)-1):
			all_subreddits = all_subreddits+'+'
	to_stream = reddit.subreddit(all_subreddits)
	
	queue_incomplete = queue.Queue()
	n_incomplete = 0
	queue_complete = queue.Queue()
	n_complete = 0
	
	for P in to_stream.stream.submissions():
		
		# create new instance for new post, put in incomplete_queue
		dict = { }
		T = time.time()
		dict['timestamp'] = T
		queue_incomplete.put(dict)
		n_incomplete += 1
		
		# print [debug]
		title = (P.title).encode('utf-8')
		print('\n'+str(title))
		print(P.subreddit)
		print(time.ctime(T))
		print('queue lenghts = ['+str(n_incomplete)+','+str(n_complete)+']\n')
