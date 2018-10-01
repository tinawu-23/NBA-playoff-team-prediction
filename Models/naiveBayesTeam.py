#!/usr/bin/env python3

import numpy as np
import pandas as pd

def extractData(fileName):
    df = pd.read_csv("../team_data/" + fileName)
    data = df[df.columns[2:25]]
    labels = df["Playoff"]
    return data, labels


if __name__ == '__main__':
    # read team data for a given year
    teamData = pd.read_csv('../team_data/teamFiles.csv')

    for index, year in teamData.iterrows():
        train_data, train_label = extractData(year["Year1"])
        test_data, test_label = extractData(year["Year2"])
