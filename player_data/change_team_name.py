#!/usr/bin/env python3

import pandas as pd

data = pd.read_csv("playerdata17-18.csv");

for index, team in enumerate(data['Tm']):
	if team == 'CHA':
		data['Tm'][index] = 'CHO'
	if team == 'BRK':
		data['Tm'][index] = 'BRO'
	if team == 'NOH':
		data['Tm'][index] = 'NOP'
		
data.to_csv("playerdata17-18.csv");
