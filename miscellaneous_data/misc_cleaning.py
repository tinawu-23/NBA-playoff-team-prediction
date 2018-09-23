#!/usr/bin/env python3

import numpy as np
import pandas as pd
from scipy.stats import zscore
from scipy.sparse.linalg import svds
import matplotlib.pyplot as plt

# read team data for a given year
df = pd.read_csv('misc17-18.csv', nrows=30)

for i, team in enumerate(df['Team']):
	df.at[i,'Team'] = str(df.at[i, 'Team']).replace('*', '')
	df.at[i, 'Attend.'] = int(df.at[i,'Attend.'].replace(',',''))
	df.at[i, 'Attend./G'] = int(df.at[i,'Attend./G'].replace(',',''))

print(df)

df.to_csv("misc17-18.csv", index= False, float_format='%g')
