#!/usr/bin/env python3

import numpy as np
import pandas as pd

# read team data for a given year
miscData = pd.read_csv('./miscFiles.csv')
for index, year in miscData.iterrows():
	df = pd.read_csv( year["Year1"])
	df = df.drop(["W", "L", "PW", "PL", "SRS", "ORtg", "DRtg", "FTr", "3PAr", "TS%", "eFG%-O", "TOV%-O", "ORB%-O", "FT/FGA-O", "eFG%-D", "TOV%-D", "DRB%-D", "FT/FGA-D", "Arena", "Attend."], axis=1)
	df.to_csv(year["Year1"], index= False, float_format='%g')

df = pd.read_csv("misc17-18.csv")
df = df.drop(["W", "L", "PW", "PL", "SRS", "ORtg", "DRtg", "FTr", "3PAr", "TS%", "eFG%-O", "TOV%-O", "ORB%-O", "FT/FGA-O", "eFG%-D", "TOV%-D", "DRB%-D", "FT/FGA-D", "Arena", "Attend."], axis=1)
df.to_csv("misc17-18.csv", index= False,float_format='%g')
