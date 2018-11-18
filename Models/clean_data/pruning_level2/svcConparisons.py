#!/usr/bin/env python3

import pandas as pd
from sklearn import svm
from evaluations import Evaluation

def extractData(fileName, exclude):
	df = pd.read_csv("../../../team_data/Removed_col/" + fileName)
	columnsSelected = list(df.columns.values)
	columnsSelected = columnsSelected[2:18]
	possible_cols = [None]
	possible_cols += list(range(0, 16))
	popped = int(0)
	for x in possible_cols:
		if x is not None and x not in exclude:
			columnsSelected.pop(x-popped)
			popped += 1
	print(columnsSelected)
	data = df.loc[:, list(columnsSelected)]
	labels = df["Playoff"]
	return data, labels

if __name__ == '__main__':
    # read team data for a given year
	teamData = pd.read_csv('../../../team_data/teamFiles.csv')
	dummy_exclude = [3, 1, 2, 8, 15, 4, 7, 10, 13, 5, 11, 9, 12, 14, 6, 0]
	exclusions = list()
	no_inclusions = [None]
	no_inclusions = list(range(0, 16))
	d = {} #will be converted to dataframe
	years = []
	for i in range(0,9):
		years.append(str(i+9) + "to" + str(i+10)) #add year column
	d["Testing Data Season"] = years
	f1 = []
	for index, year in teamData.iterrows():
		train_data, train_label = extractData(year["Year1"], no_inclusions)
		test_data, test_label = extractData(year["Year2"], no_inclusions)
		clf = svm.SVC()
		y_pred = clf.fit(train_data,train_label)
		predictions = clf.predict(test_data)
		eval= Evaluation(predictions, test_label)
		f1.append(round(eval.getF1(),5))
		d["None"] = f1

	for exclude in dummy_exclude:
		exclusions.append(exclude)
		f1 = []
		for index, year in teamData.iterrows():
			train_data, train_label = extractData(year["Year1"], exclusions)
			test_data, test_label = extractData(year["Year2"], exclusions)
			clf = svm.SVC()
			y_pred = clf.fit(train_data,train_label)
			predictions = clf.predict(test_data)
			eval= Evaluation(predictions, test_label)
			f1.append(round(eval.getF1(),5))
			d[exclude] = f1 #f1 scores for each feature for a given year
	table = pd.DataFrame(d)

	table.to_csv('f1_svc.csv', sep=',', index=False)
