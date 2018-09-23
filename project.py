# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:08:41 2018

@author: mattg
"""
import pandas as pd

data = pd.read_csv("playerdata12-13.csv") #

data = pd.DataFrame(data)
features = []
for i in data:
    features.append(i)

tableData = pd.DataFrame(data[features])
for player in tableData['Player']:
        print(player)
