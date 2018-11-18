#!/usr/bin/env python3

import pandas as pd
import operator

if __name__ == '__main__':
	files = ['new_f1_cart.csv', 'new_f1_gnb.csv', 'new_f1_svc.csv']

	row_num = 9 #average difference row
	results = {}

	for f in files:
		data = pd.read_csv(f)
		col = list(data.columns.values[2:])
		df = pd.DataFrame(data, columns=col)

		diff = {}

		for index, c in enumerate(col):
			diff[index] = df[c][row_num]
	
		diff_sorted = sorted(diff.items(), key=operator.itemgetter(1))
		final_diff = [i[0] for i in diff_sorted]
		results[f] = final_diff

	print(results)
	 
