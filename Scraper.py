#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
	subreddit = reddit.subreddit('all')
	
	queue_incomplete_samples = []
	
	for submission in subreddit.stream.submissions():
		# log data
		dict = { }
		
		# print
		print('\n'+strftime("%H:%M:%S", gmtime()))
		title = (submission.title).encode('utf-8')
		print('\tTitle: '+str(title)+'\n')
	
	#submission = reddit.submission(id='5yuvgo')
	#for top_level_comment in submission.comments:
	#	print(top_level_comment.body)