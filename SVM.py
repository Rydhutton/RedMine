#!/usr/bin/env python
# -*- coding: utf-8 -*-

# we are using "PRAW" as an API to collect reddit data
# you can install it simply by typing "pip install praw"

def TrainOnData():
	print("Training SVM on collected data.")
	n_files_detected = 0
	n_samples = 0
	print("...found "+str(n_files_detected)+" data files for training")
	print("...loaded "+str(n_samples)+" data samples from files")
	print("Complete.")
	
def TestOnData():
	print("Running SVM on test data.")
	accuracy = 0.0
	n_files_detected = 0
	n_samples = 0
	print("...found "+str(n_files_detected)+" data files for testing")
	print("...loaded "+str(n_samples)+" data samples from files")
	print("...SVM accuracy = "+str(accuracy))
	print("Complete.")


