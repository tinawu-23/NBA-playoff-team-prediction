#!/usr/bin/env python3

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import sys
sys.path.insert(0, '../clean_data/')
from evaluations import Evaluation
from join_data import join_data

def extractData(teamFileName, miscFileName, exclude):
	df = join_data(teamFileName, miscFileName, "NBA_Salary_History.csv")
	labels = df["Playoff"]
	df.drop('Playoff', axis=1, inplace=True)
	columnsSelected = list(df.columns.values)
	columnsSelected = columnsSelected[1:23]
	if exclude is not None:
		columnsSelected.pop(exclude)
	data = df.loc[:, list(columnsSelected)]
	return data, labels

if __name__ == '__main__':
    # read team data for a given year
	teamData = pd.read_csv('teamFiles.csv')
	exclusions = [None]
	exclusions += list(range(0,21))
	d = {} #will be converted to dataframe
	years = []
	for i in range(0,9):
		years.append(str(i+9) + "to" + str(i+10)) #add year column
	d["Testing Data Season"] = years

	for exclude in exclusions:
		#print(exclude)
		f1 = []
		for index, year in teamData.iterrows():
			train_data, train_label = extractData(year["Year1"], year["Misc1"], exclude)
			test_data, test_label = extractData(year["Year2"], year["Misc2"], exclude)
			clf = DecisionTreeClassifier()
			y_pred = clf.fit(train_data,train_label)
			predictions = clf.predict(test_data)
			# print(predictions)
			# print(test_label)
			eval= Evaluation(predictions, test_label)
	# 		# print(eval.getAccuracy())
	# 		# print(eval.getPrecision())
	# 		# print(eval.getRecall())
	# 		# print(eval.getF1())
			f1.append(round(eval.getF1(), 5))
			if exclude is None:
				d["None"] = f1
			else:
				d[exclude] = f1 #f1 scores for each feature for a given year

	table = pd.DataFrame(d)

	table.to_csv('f1_cart1.csv', sep=',', index=False)
