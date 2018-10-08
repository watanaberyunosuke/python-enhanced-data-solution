import pandas as pd
import numpy as np
import matplotlib as mp
import statistics as stat
from itertools import groupby

# Read Excel by Using pandas, File Name and Sheets Name to be filled
file = ''
xl = pd.ExcelFile(file)
print(xl.sheet_names)
df1 = xl.parse('sheTest.xlsxet1')
#Sorting
print("Sorted List:",sorted(data))
# Output
print("Minimum:",min(data))
print("Maximum:",max(data))
print("Sum:",sum(data))
print("Mean:",stat.mean(data))
print("Median",stat.median(data))
# Mode
Sortlist = data
# when the list is sorted, groupby groups by consecutive elements which are similar
for z, y in groupby(sorted(Sortlist)):
    #  list(y) returns all the occurences of item x
    if len(list(y)) > 1:
        print("Mode:", z)
    else:
        print("No Mode")
# Continue
print("Standard Deviation:",stat.stdev(data))
print("Variance:",stat.variance(data))
print("Range:",max(data) - min(data))
