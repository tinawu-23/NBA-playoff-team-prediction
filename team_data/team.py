#!/usr/bin/env python3

import numpy as np
import pandas as pd
from scipy.stats import zscore
from scipy.sparse.linalg import svds
import matplotlib.pyplot as plt

# read team data for a given year
df = pd.read_csv('team_data_13_14.csv', nrows=30)

# add a column of whether team made playoff
# df['Playoff'] = ' '
# i = 0
#
# for team in df['Team']:
# 	df.at[i,'Playoff'] = "Y" if '*' in team else "N"
# 	df.at[i,'Team'] = str(df.at[i,'Team']).replace('*','')
# 	i += 1

for index, team in enumerate(df['Team']):
	if team == 'Charlotte Bobcats':
		df.at[index, 'Team'] = 'Charlotte Hornets'
	if team == 'New Jersey Nets':
		df.at[index, 'Team'] = 'Brooklyn Nets'
	if team == 'New Orleans Hornets':
		df.at[index, 'Team'] = 'New Orleans Pelicans'

df.to_csv("team_data_13_14.csv", index= False, float_format='%g')
# plot team based on two features; playoff in red; not playoff in blue
# n=0
# for team in df['Playoff']:
# 	if team == 'Y':
# 		plt.scatter(df.at[n,"FG%"],df.at[n,"AST"], marker='^', c='r')
# 	elif team == 'N':
# 		plt.scatter(df.at[n,"FG%"],df.at[n,"AST"], marker='+', c='b')
# 	n += 1
#
# plt.show()
