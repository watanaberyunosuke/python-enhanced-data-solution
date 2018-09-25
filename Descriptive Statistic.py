import pandas as pd
import numpy as np
import matplotlib as mp
import statistics as stat
from itertools import groupby
# Input Array to fill
x = list([3, 4, 2, 5, 1, 6, 7, 8, 0])
print("Input:",x)
#Sorting
print("Sorted List:",sorted(x))
# Output
print("Minimum:",min(x))
print("Maximum:",max(x))
print("Sum:",sum(x))
print("Mean:",stat.mean(x))
print("Median",stat.median(x))
# Mode
Sortlist = x
# when the list is sorted, groupby groups by consecutive elements which are similar
for z, y in groupby(sorted(Sortlist)):
    #  list(y) returns all the occurences of item x
    if len(list(y)) > 1:
        print("Mode:", z)
    else:
        (print("Mode not Find"))
# Continue
print("Standard Deviation:",stat.stdev(x))
print("Variance:",stat.variance(x))
print("Range:",max(x) - min(x))