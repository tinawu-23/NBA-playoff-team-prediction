#!/usr/bin/env python3

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from evaluations import Evaluation

def extractData(fileName, exclude):
	df = pd.read_csv("../../team_data/removed_col/" + fileName)
	columnsSelected = list(df.columns.values)
	columnsSelected = columnsSelected[2:18]
	if exclude is not None:
		columnsSelected.pop(exclude)
	data = df.loc[:, list(columnsSelected)]
	labels = df["Playoff"]
	return data, labels


if __name__ == '__main__':
    # read team data for a given year
	teamData = pd.read_csv('../../team_data/teamFiles.csv')
	exclusions = [None]
	exclusions += list(range(0,16))
	d = {} #will be converted to dataframe
	years = []
	for i in range(0,9):
		years.append(str(i+9) + "to" + str(i+10)) #add year column
	d["Testing Data Season"] = years

	for exclude in exclusions:
		#print(exclude)
		f1 = []
		for index, year in teamData.iterrows():
			train_data, train_label = extractData(year["Year1"], exclude)
			test_data, test_label = extractData(year["Year2"], exclude)
			gnb = GaussianNB()
			y_pred = gnb.fit(train_data,train_label)
			predictions = gnb.predict(test_data)
			eval= Evaluation(predictions, test_label)
            #print(eval.getAccuracy())
            #print(eval.getPrecision())
            #print(eval.getRecall())
			f1.append(round(eval.getF1(),5))
            #print("------------------------------")
			if exclude is None:
				d["None"] = f1
			else:
				d[exclude] = f1 #f1 scores for each feature for a given year 

	table = pd.DataFrame(d)

	table.to_csv('f1_gnb.csv', sep=',', index=False)
