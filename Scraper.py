#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import praw

# we are using "PRAW" as an API to collect reddit data
# you can install it simply by typing "pip install praw"

def StartCollectingData():	
	print("Starting in data-mine mode [press Ctrl+C to stop].")
	
	incomplete_samples = 0 # since samples require data like '10 min', '20 min', '2 hours', some samples will be marked 'incomplete'
	complete_samples = 0
	
	time_elapsed = 0
	while(True):
		time_elapsed = time_elapsed+1
		print("...time elapsed : "+str(time_elapsed)+". incomplete samples : "+str(incomplete_samples)+". complete samples : "+str(complete_samples))
		time.sleep(1.0)
