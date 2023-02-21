import os
import timeit
import pandas as pd
import csv
import glob
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('alpha.csv')
df1 = df.iloc[:,4]
df2  = df1.dropna()
df2.plot()
print(df2)
print(df2.shape)

#plt.plot(df3,len(df2))
#plt.show()















#================AUFGABE 2============================================================================================
"""names = ['alpha' , 'bravo' , 'charlie' , 'delta', 'echo', 'foxtrot' , 'golf']
df = pd.read_csv('beta_sun_deg.csv')
for i in names:
    plt.plot(df[str(i)])
names = [name.capitalize() for name in names]
plt.xticks([0,182,365], ['6/2/2018', 'B', '6/2/2019'])
plt.legend(names)
plt.show()"""
#======================================================================================================================






