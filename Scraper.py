#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import praw

# we are using "PRAW" as an API to collect reddit data
# you can install it simply by typing "pip install praw" into the terminal
# you can see the app details if you
#	1) log in to reddit as csc475_user (pass:asdfasdf)
#	2) go to 'preferences'
#	3) click on the 'apps' tab

def StartCollectingData():	
	print("Starting in data-mine mode [press Ctrl+C to stop].")
	
	reddit = praw.Reddit(client_id='Er23cgYvVuqPHw', client_secret='uXfAKsBIUQ7JaR6Hy--RxQuF4eo', user_agent='CompSci474Project:v1.0.0 (by /u/csc475_user)')
	
	submission = reddit.submission(id='5yuvgo')
	# iterate through top-level comments
	for top_level_comment in submission.comments:
		print(top_level_comment.body)