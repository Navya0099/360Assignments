# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:57:08 2021

@author: NAVYA .P
"""

import pandas as pd

# import file
df = pd.read_csv('C:/Users/NAVYA .P/Desktop/360digitmg_assignments/3rd assignment/DataSets-Data Pre Processing/DataSets/Iris.csv')


# APplying discretization for Sepal Length
df['sepallen_dis']=pd.cut(df['Sepal.Length'],4,labels=['very small','small','large','verylarge'])
df.head(10)

#Applying discretization for Sepal WIdth
df['sepalwid_dis']=pd.cut(df['Sepal.Width'],3,labels=['very Tiny','tiny','medium'])
df.head(10)

# Applying discretization for Petal.Width

df['petalwid_dis']=pd.cut(df['Petal.Width'],3,labels=['tiny ','medium','large'])
df.head(10)
