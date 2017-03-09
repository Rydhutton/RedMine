#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
	"""	
	This class serves as the entry point.
	Launching in different modes:
		"py Main.py -mine"
		"py Main.py -train"
		"py Main.py -test"
	Note: Before a section of code, put [yourname] so that we can keep track of how much work each person is doing
	"""

	# [harrison] determine launch context
	if (sys.argv[1] == "-mine"):
		do_MineData()
	elif (sys.argv[1] == "-train"):
		do_TrainOnCollectedData()
	elif (sys.argv[1] == "-test"):
		do_TestOnCollectedData()
	else:
		print("unknown mode")
	
def do_MineData():
	"""
	In this mode, you leave your computer to collect data (possibly over several days)
	Note : data should be stored in files "data1", "data2", "data3", etc ... so that if a crash occurs, not all data is lost
	This should make calls to Scraper.py
	"""
	print("mine")
	return
	
def do_TrainOnCollectedData():
	"""
	In this mode, any text files "data1", "data2", "data3", etc, are used to train the SVM.
	This should make calls to SVM.py
	"""
	print("train")
	return
	
def do_TestOnCollectedData():
	"""
	In this mode, the previously trained SVM should attempt to classify data files "test1", "test2", "test3", etc.. using the trained SVM
	It should print statistics like accuracy, etc.
	This should make calls to SVM.py
	"""
	print("test")
	return
	
if __name__ == "__main__":
    main()


