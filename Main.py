#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import Scraper
import SVM

"""	
[harrison] This class serves as the entry point.
Launching in different modes:
	"py Main.py -mine"
	"py Main.py -train"
	"py Main.py -test"
Note: Before a section of code, put [yourname] so that we can keep track of how much work each person is doing
"""

def main():
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
	Scraper.StartCollectingData()
	return
	
def do_TrainOnCollectedData():
	SVM.TrainOnData()
	return
	
def do_TestOnCollectedData():
	SVM.TestOnData()
	return
	
if __name__ == "__main__":
    main()


