#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def StartCollectingData():	
	#In this mode, you leave your computer to collect data (possibly over several days)
	#Note : data should be stored in files "data1", "data2", "data3", etc ... should a crash occur, not all data is lost
	#TO-DO !!!
	print("Starting in data-mine mode [press Ctrl+C to stop]...")
	incomplete_samples = 0
	complete_samples = 0
	time_elapsed = 0
	while(True):
		time_elapsed = time_elapsed+1
		print("time elapsed : "+str(time_elapsed)+". incomplete samples : "+str(incomplete_samples)+". complete samples : "+str(complete_samples))
		time.sleep(1.0)
