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
		Scraper.StartCollectingData()
	elif (sys.argv[1] == "-train"):
		SVM.TrainOnData()
	elif (sys.argv[1] == "-test"):
		SVM.TestOnData()
	else:
		print("unknown mode")
	
if __name__ == "__main__":
    main()


