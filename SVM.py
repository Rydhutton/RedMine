#!/usr/bin/env python
# -*- coding: utf-8 -*-

def TrainOnData():
	#In this mode, any text files "data1", "data2", "data3", etc, are used to train the SVM.
	#TO-DO !!!
	print("Training SVM on collected data.")
	n_files_detected = 0
	n_samples = 0
	print("...found "+str(n_files_detected)+" data files for training")
	print("...loaded "+str(n_samples)+" data samples")
	print("Complete.")
	
def TestOnData():
	#In this mode, the previously trained SVM should attempt to classify data files "test1", "test2", "test3", etc.. using the trained SVM
	#TO-DO !!!
	print("Running SVM on test data.")
	accuracy = 0.0
	n_files_detected = 0
	n_samples = 0
	print("...found "+str(n_files_detected)+" data files for testing")
	print("...loaded "+str(n_samples)+" data samples")
	print("...SVM accuracy = "+str(accuracy))
	print("Complete.")


