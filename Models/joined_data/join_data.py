#!/usr/bin/env python3

import numpy as np
import pandas as pd
import re

def join_data(teamFileName, miscFileName, salaryFileName):
	dfTeam = pd.read_csv("../../team_data/removed_col/" + teamFileName)
	dfMisc = pd.read_csv("../../miscellaneous_data/" + miscFileName)
	dfSalary = pd.read_csv("../../salary-data/" + salaryFileName)

	dfTeam.drop('Rk', axis=1, inplace=True)
	dfMisc.drop('Rk', axis=1, inplace=True)


	dfJoined = pd.merge(dfTeam, dfMisc, left_on = 'Team', right_on='Team')
	dfJoined["Total Salary"] = ''
	# print(dfTeam_Misc)
	# print(dfSalary)

	year = re.findall(r".*([0-9][0-9]-[0-9][0-9]).csv",miscFileName)[0]
	year = "20" + year

	for index, col_name in dfJoined.iterrows():
		team_name = col_name["Team"]
		row = dfSalary.loc[(dfSalary['Team'] == team_name) & (dfSalary['Season'] == year)]
		if not row.empty:
			salary = row.iloc[0]["Total Salary"]
			dfJoined.at[index,"Total Salary"] = salary
	return dfJoined
