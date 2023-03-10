
from itertools import combinations
from math import comb
import numpy as np
import pandas as pd


# number of maturity dates
m = 7
sub = 3
subch2 = comb(sub, 2)
# generate indices for subsets of four maturity dates
a = np.array(list(combinations(range(1, m + 1), sub)))
scomb = [str(a[i]).strip('[]') for i in range(len(a))]
scomb = [scomb[i].split() for i in range(len(a))]
scomb = [' '.join(scomb[i]) for i in range(len(a))]
scomb = ['[' + scomb[i] + ']' for i in range(len(a))]
print(scomb[m - 1])

print(a[1])
print(len(a))

sveny = pd.read_csv("data/FED-SVENY-20230224.csv")
num_days = max(sveny.count())#int(sveny.shape[0]/1)
print(num_days)
print(sveny.head(10))
print(num_days)

print(sveny.iloc[1:10, a[0]])
d = {}
for i in scomb:
    d[i] = ["[" for x in range(num_days)]
for h in range(len(a)):
    i = a[h]
    l = scomb[h]
    c = np.array(list(combinations(i, 2)))
    for j in range(num_days):
        for k in range(subch2):
            b = np.array(sveny.iloc[j, c[k]])
         #   print(b)
            if b[0] < b[1]:
                d[l][j] += " " + str(c[k][1])
            else:
                d[l][j] += " " + str(c[k][0])
        d[l][j] += "]"
        d[l][j] = d[l][j].replace(" ", "", 1)
r = pd.DataFrame(d)
r.rename(sveny['Date'], axis='index', inplace =True)
s = "data/" + str(m) + "choose" + str(sub) 
r.to_csv(s + "rankings.csv")
print("done")
countof = {}
for h in range(len(a)):
    l = scomb[h]
    countof[l] = np.zeros(num_days, dtype=int)
    for j in range(num_days):
        countof[l][j] = r[l][0:j].nunique()

countof = pd.DataFrame(countof)
countof.to_csv(s + "countof.csv")
