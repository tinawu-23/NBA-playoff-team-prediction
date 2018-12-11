#!/usr/bin/env python3
import numpy as np
from scipy import stats
import pandas as pd
from itertools import chain
import matplotlib.pyplot as plt

threePoint_list = []
assists_list = []
freeThrow_list = []

for i in range(8,18):
    year1 = str(i)
    year2 = str(i+1)
    if len(year1) == 1:
        year1 = "0"+year1
    if len(year2) == 1:
        year2 = "0"+year2
    csv_str = "C:\\Users\\ywu6\\Documents\\datascience\\NBA-playoff-team-prediction\\team_data\\team_data_{}_{}.csv".format(year1, year2)
    df = pd.read_csv(csv_str)
    threePoint_list.append(df["PF"].tolist())
    #assists_list.append(df["AST"].tolist())
    #freeThrow_list.append(df["FT"].tolist())

threePoint_list = list(chain.from_iterable(threePoint_list))
#assists_list = list(chain.from_iterable(assists_list))
#freeThrow_list = list(chain.from_iterable(freeThrow_list))

#print(assists_list)
#print(freeThrow_list)

plt.hist(threePoint_list, normed=True)
xt = plt.xticks()[0]
xmin, xmax = min(xt), max(xt)
lnspc = np.linspace(xmin, xmax, len(threePoint_list))

m, s = stats.norm.fit(threePoint_list)
pdf_g = stats.norm.pdf(lnspc, m, s)
plt.plot(lnspc, pdf_g)

plt.title("Personal Fouls")
plt.show()
