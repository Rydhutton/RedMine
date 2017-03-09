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
	Note: Before a section put '#yourname', so we can keep track of how much work each person is doing
	"""

	# harrison
	# determine launch context
	if (sys.argv[1] == "-mine"):
		do_MineData()
	elif (sys.argv[1] == "-train"):
		do_TrainOnCollectedData()
	elif (sys.argv[1] == "-test"):
		do_TestOnCollectedData()
	else:
		print("unknown mode")
	
def do_MineData():
	print("mine")
	return
	
def do_TrainOnCollectedData():
	print("train")
	return
	
def do_TestOnCollectedData():
	print("test")
	return
	
if __name__ == "__main__":
    main()


