#!/usr/bin/env python3

import pandas as pd
from sklearn import svm
import sorted
import sys
sys.path.insert(0, '../')
from evaluations import Evaluation
import numpy

def extractData(fileName, include):
	include.append("Playoff")
	df = pd.read_csv("../../../team_data/removed_col/" + fileName, usecols= include)
	columnsSelected = list(df.columns.values)
	columnsSelected = columnsSelected[:-1]
	data = df.loc[:, list(columnsSelected)]
	labels = df["Playoff"]
	return data, labels

if __name__ == '__main__':
    # read team data for a given year
	teamData = pd.read_csv('../../../team_data/teamFiles.csv')
	ordered_cols = sorted.sortDiff()['svc']
	l = list()
	for k in range(len(ordered_cols)):
		f1 = []
		for index, year in teamData.iterrows():
			train_data, train_label = extractData(year["Year1"], ordered_cols[:k+1])
			test_data, test_label = extractData(year["Year2"], ordered_cols[:k+1])
			clf = svm.SVC()
			y_pred = clf.fit(train_data,train_label)
			predictions = clf.predict(test_data)
			eval= Evaluation(predictions, test_label)
			f1.append(round(eval.getF1(),5))

		average = numpy.mean(f1)
		print(average)
		l.append((ordered_cols[k], average))
	print(l)
