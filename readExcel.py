#!/usr/bin/python

from pandas import DataFrame, read_csv
import pandas as pd

file = r'/home/tanveer/Documents/test.csv'
df = pd.read_csv(file)
print df.head()

#print (df)

