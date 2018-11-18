#!/usr/bin/env python3

import pandas as pd
import operator

def analysis(filename):
	print("\n"+filename+":")
	df = pd.read_csv(filename)
	lst = []
	diffdict = {}

	for i in range(df.shape[0]):
		for j in range(2,df.shape[1]):
			df.iloc[i,j] -= df.iloc[i,1]

	for i in range(2,df.shape[1]):
		c = str(i-2)
		lst.append(round(df[c].mean(),3))
		diffdict[c]=round(df[c].mean(),3)

	df.loc[df.shape[0]+1]=' '
	df.loc[df.shape[0],'Testing Data Season'] = 'Average Difference'
	for i in range(len(lst)):
		df.iloc[9,i+2] = lst[i]
	#print(df)
	#new_file = "new_"+filename
	#df.to_csv(new_file, index= False, float_format='%g')
	sorted_diffdict = sorted(diffdict.items(), key=operator.itemgetter(1))
	print(sorted_diffdict)

analysis('f1_cart.csv')
analysis('f1_gnb.csv')
analysis('f1_svc.csv')
