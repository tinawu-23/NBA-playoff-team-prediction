#!/usr/bin/env python3

import numpy as np
import pandas as pd
from scipy.stats import zscore
from scipy.sparse.linalg import svds 
import matplotlib.pyplot as plt

# read team data for a given year
df = pd.read_csv('team_data_08_09.csv', nrows=30)

# add a column of whether team made playoff
df['Playoff'] = ' '
i = 0

for team in df['Team']:
	df.at[i,'Playoff'] = "Y" if '*' in team else "N"
	i += 1

print(df)

