# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 10:48:22 2021

@author: NAVYA .P
"""

import pandas as pd

import statistics 


df = pd.read_csv('C:/Users/NAVYA .P/Desktop/360digitmg_assignments/3rd assignment/DataSets-Data Pre Processing/DataSets/Z_dataset.csv ')

df.head(10)

x = statistics.variance(df.squarelength) #0.6856935123042506

y = statistics.variance(df.squarebreadth) #0.189979418344519

z = statistics.variance(df.recLength) #3.1162778523489933

s = statistics.variance(df.recbreadth) #0.5810062639821029

# here squarelength, squarebreadth and recbreadth have variance near to zero.
# so we need to drop the columns or ignore them.

#drop the columns
df.drop(['squarelength','squarebreadth','recbreadth'],axis =1,inplace =True)
df
