#!/usr/bin/env python3

import pandas as pd
from sklearn import svm
from evaluations import Evaluation

def extractData(fileName, exclude):
	df = pd.read_csv("../../../team_data/" + fileName)
	columnsSelected = list(df.columns.values)
	columnsSelected = columnsSelected[2:18]
	possible_cols = [None]
	possible_cols += list(range(0, 16))
	popped = int(0)
	for x in possible_cols:
		if x is not None and x not in exclude:
			columnsSelected.pop(x-popped)
			popped += 1
	data = df.loc[:, list(columnsSelected)]
	labels = df["Playoff"]
	print(data)
	return data, labels

if __name__ == '__main__':
    # read team data for a given year
	teamData = pd.read_csv('../../../team_data/teamFiles.csv')
	dummy_exclude = [3, 5, 2, 7, 10, 14, 11, 1, 0, 6]
	exclusions = list()
	d = {} #will be converted to dataframe
	years = []
	for i in range(0,9):
		years.append(str(i+9) + "to" + str(i+10)) #add year column
	d["Testing Data Season"] = years

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
            #print(eval.getAccuracy())
            #print(eval.getPrecision())
            #print(eval.getRecall())
			f1.append(round(eval.getF1(),5))
			print("hmmmmmmm")
			if exclude is None:
				d["None"] = f1
			else:
				d[exclude] = f1 #f1 scores for each feature for a given year
	table = pd.DataFrame(d)

	table.to_csv('f1_svc.csv', sep=',', index=False)
