#!/usr/bin/env python3

import pandas as pd
from sklearn.naive_bayes import GaussianNB
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
	teamData = pd.read_csv('../../../team_data/teamFiles.csv')
	ordered_cols = sorted.sortDiff()['gnb']
	l = list()
	for k in range(len(ordered_cols)):
		f1 = []
		for index, year in teamData.iterrows():
			train_data, train_label = extractData(year["Year1"], ordered_cols[:k+1])
			test_data, test_label = extractData(year["Year2"], ordered_cols[:k+1])
			gnb = GaussianNB()
			y_pred = gnb.fit(train_data,train_label)
			predictions = gnb.predict(test_data)
			eval= Evaluation(predictions, test_label)
			f1.append(round(eval.getF1(),5))

		average = numpy.mean(f1)
		l.append((ordered_cols[k], average))
	print(l)
