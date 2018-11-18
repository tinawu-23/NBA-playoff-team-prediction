#!/usr/bin/env python3

import pandas as pd
import operator

if __name__ == '__main__':
	files = ['f1_cart_differences.csv', 'f1_gnb_differences.csv', 'f1_svc_differences.csv']
	names = ['cart', 'gnb', 'svc']
	features = {0 : 'FG', 1 : 'FGA', 2 : '3P', 3 : '3PA', 4 : '2P', 5 : '2PA', 6 : 'FT', 7 : 'FTA' , 8 : 'ORB' , 9 : 'DRB', 10 : 'AST', 11: 'STL', 12 : 'BLK', 13 : 'TOV', 14 : 'PF', 15: 'PTS'}
	row_num = 9 #average difference row
	results = {}
	n = 0

	for f in files:
		data = pd.read_csv(f)
		col = list(data.columns.values[2:]) #feature columns
		df = pd.DataFrame(data, columns=col)

		diff = {}

		for index, c in enumerate(col):
			diff[index] = df[c][row_num] #get avg diff
	
		diff_sorted = sorted(diff.items(), key=operator.itemgetter(1)) #sort differences from lowest to highest
		final_diff = [features[i[0]] for i in diff_sorted] #return the features corresponding to each difference
		results[names[n]] = final_diff #dictionary of all sorted features for each model

		n+=1

	print(results)
	 
