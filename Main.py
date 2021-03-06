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
"""

def main():
	# [harrison] determine launch context
	if (len(sys.argv) <= 1):
		print("\nTo use, type 'py Main.py <command>'.\nCommands include -mine or -train or -test")
	elif (sys.argv[1] == "-mine"):
		Scraper.StartCollectingData()
	elif (sys.argv[1] == "-train"):
		SVM.TrainOnData()
	else:
		print("unknown mode")
	
if __name__ == "__main__":
    main()


