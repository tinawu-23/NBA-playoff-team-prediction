#!/usr/bin/env python3

import numpy as np
import pandas as pd

# read team data for a given year
teamData = pd.read_csv('../teamFiles.csv')
for index, year in teamData.iterrows():
	df = pd.read_csv( year["Year1"])
	df = df.drop(["G", "MP", "FG%", "3P%", "2P%", "FT%", "TRB"], axis=1)
	df.to_csv(year["Year1"], index= False, float_format='%g')

df = pd.read_csv("team_data_17_18.csv")
df = df.drop(["G", "MP", "FG%", "3P%", "2P%", "FT%", "TRB"], axis=1)
df.to_csv("team_data_17_18.csv", index= False, float_format='%g')
